import os


api_key = os.getenv("OPENAI_API_KEY")

# --- THIS IS THE DEBUGGING LINE ---
print(f"--- DEBUG: Key loaded from environment: [{api_key}] ---")
# ------------------------------------


config_list_openai = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY"),
    }
]

# The llm_config that will be passed to your agents
llm_config = {
    "config_list": config_list_openai,
    "cache_seed": 42  # Use a seed for caching and reproducibility
}