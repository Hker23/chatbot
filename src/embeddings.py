from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils.env_utils import validate_env
import os
def get_embeddings():
    """
    Initialize and return GoogleGenerativeAIEmbeddings after validating env vars.
    """
    # Ensure environment variables are loaded
    validate_env()
    api_key = os.getenv("API_KEY")
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )