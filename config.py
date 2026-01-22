"""
MGA AI Agent Configuration
Supports multiple LLM providers: Groq (default), Gemini, OpenAI, Anthropic
Supports both .env (local) and st.secrets (Streamlit Cloud)
"""

import os
from dotenv import load_dotenv

# Load .env for local development
load_dotenv()

# --- Helper function to get secrets ---
def get_secret(key: str, default: str = "") -> str:
    """
    Get secret from Streamlit secrets (Cloud) or environment variable (local).
    Priority: st.secrets > os.environ > default
    """
    value = default
    
    # Try Streamlit secrets first (for Cloud deployment)
    try:
        import streamlit as st
        # Check standard top-level secrets
        if hasattr(st, 'secrets') and key in st.secrets:
            value = st.secrets[key]
        # Check nested sections (e.g. st.secrets["connections"]["key"])? No, simple flat structure usually.
    except:
        pass
    
    # Fall back to environment variable if not found in secrets
    if value == default:
        value = os.getenv(key, default)
    
    # Sanitize value (remove quotes/spaces potentially added by TOML formatting)
    if value and isinstance(value, str):
        return value.strip().strip('"').strip("'")
    
    return value

# --- LLM Configuration ---
# Default to Groq for fast and free inference
LLM_PROVIDERS = {
    "groq": {
        "name": "Groq (Rápido)",
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "env_key": "GROQ_API_KEY",
    },
    "groq_llama": {
        "name": "Groq Llama (Extracción)",
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",  # Higher rate limits
        "env_key": "GROQ_API_KEY",
    },
    "gemini": {
        "name": "Google Gemini",
        "model": "gemini-2.0-flash",
        "env_key": "GOOGLE_API_KEY",
    },
    "gemini_flash": {
        "name": "Gemini Flash (Barato)",
        "model": "gemini-2.0-flash",
        "env_key": "GOOGLE_API_KEY",
    },
    "openai": {
        "name": "OpenAI GPT-4",
        "model": "gpt-4-turbo-preview",
        "env_key": "OPENAI_API_KEY",
    },
    "anthropic": {
        "name": "Anthropic Claude",
        "model": "claude-3-sonnet-20240229",
        "env_key": "ANTHROPIC_API_KEY",
    },
}

DEFAULT_PROVIDER = "groq"

# --- API Keys (loaded from secrets or env) ---
GOOGLE_API_KEY = get_secret("GOOGLE_API_KEY")
OPENAI_API_KEY = get_secret("OPENAI_API_KEY")
ANTHROPIC_API_KEY = get_secret("ANTHROPIC_API_KEY")
GROQ_API_KEY = get_secret("GROQ_API_KEY")

# --- Database ---
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "database", "mga_agent.db")

# --- App Settings ---
APP_TITLE = "Agente IA para Proyectos MGA"
APP_DESCRIPTION = "Herramienta de apoyo para formulación de proyectos públicos en la plataforma MGA del DNP"

# --- Document Templates ---
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_available_providers():
    """Return list of providers that have API keys configured"""
    available = []
    for provider_id, config in LLM_PROVIDERS.items():
        # USE get_secret() instead of os.getenv() to ensure Cloud works
        api_key = get_secret(config["env_key"], "")
        if api_key:
            available.append({
                "id": provider_id,
                "name": config["name"],
                "model": config["model"]
            })
    return available


def get_llm(provider: str = None):
    """Get LLM instance for the specified provider"""
    provider = provider or DEFAULT_PROVIDER
    
    if provider == "groq":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=LLM_PROVIDERS["groq"]["model"],
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",
            temperature=0.3,
        )
    elif provider == "groq_llama":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=LLM_PROVIDERS["groq_llama"]["model"],
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",
            temperature=0.1,  # Lower temp for extraction accuracy
        )
    elif provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=LLM_PROVIDERS["gemini"]["model"],
            google_api_key=GOOGLE_API_KEY,
            temperature=0.3,
        )
    elif provider == "gemini_flash":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=LLM_PROVIDERS["gemini_flash"]["model"],
            google_api_key=GOOGLE_API_KEY,
            temperature=0.1,  # Lower temp for extraction
        )
    elif provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=LLM_PROVIDERS["openai"]["model"],
            api_key=OPENAI_API_KEY,
            temperature=0.3,
        )
    elif provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(
            model=LLM_PROVIDERS["anthropic"]["model"],
            api_key=ANTHROPIC_API_KEY,
            temperature=0.3,
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")
