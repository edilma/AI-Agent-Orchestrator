# blog_agent_framework/config.py
import os

# Define a config list containing the model configuration
config_list_openai = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY"),
        # Pass the Project ID directly as a parameter
        "project": os.getenv("OPENAI_PROJECT_ID"),
    }
]

# The llm_config that will be passed to the agents
llm_config = {
    "config_list": config_list_openai,
    "cache_seed": 42
}