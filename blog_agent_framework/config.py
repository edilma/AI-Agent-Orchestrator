import os

# Get the API key from the environment once.
api_key = os.getenv("OPENAI_API_KEY")

# Define a list that contains your model configuration.
config_list_openai = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": api_key,  
    }
]

# The llm_config that will be passed to your agents
llm_config = {
    "config_list": config_list_openai,
    "cache_seed": 42  # Use a seed for caching and reproducibility
}