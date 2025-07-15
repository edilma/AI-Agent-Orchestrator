# In blog_agent_framework/config.py
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient

# This function creates and returns the model client object
def create_model_client(model="gpt-3.5-turbo"):
    return OpenAIChatCompletionClient(
        model=model,
        api_key=os.getenv("OPENAI_API_KEY"),
        project=os.getenv("OPENAI_PROJECT_ID"),
    )