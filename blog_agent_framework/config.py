import os

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Set up the LLM configuration
llm_config = {
    "model": "gpt-3.5-turbo",
    "api_key": api_key
}
