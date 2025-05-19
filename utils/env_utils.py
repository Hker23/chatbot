from dotenv import load_dotenv
import os


def validate_env():
    """
    Load environment variables from a .env file and validate required keys.

    Ensures that necessary LangChain and LangSmith environment variables are set.
    Raises:
        EnvironmentError: If a required environment variable is missing.
    """
    # Load from .env
    load_dotenv()

    # Required environment variables
    required_vars = [
        "API_KEY",
        "LANGCHAIN_API_KEY",
        "LANGCHAIN_PROJECT",
    ]

    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    # Set OS environment variables for LangChain and LangSmith
    os.environ["API_KEY"] = os.getenv("API_KEY")
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = os.getenv(
        "LANGCHAIN_TRACING_V2", "true"
    )
    os.environ["LANGCHAIN_TRACING_BACKEND"] = os.getenv(
        "LANGCHAIN_TRACING_BACKEND", "langsmith"
    )
    os.environ["LANGSMITH_ENDPOINT"] = os.getenv(
        "LANGSMITH_ENDPOINT", "https://api.smith.langchain.com"
    )
    os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

    # Optional: Initialize LangSmith client if needed
    # from langsmith import Client
    # client = Client()

    print("Environment variables loaded and validated.")
