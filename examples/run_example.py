# examples/run_example.py

import asyncio
import os
from dotenv import load_dotenv

# Import the main function from the library
from blog_agent_framework import generate_blog_post_with_review

# This is the crucial line that loads the API key from the .env file
# into the environment, so the library can use it automatically.
load_dotenv()


async def main():
    """
    An example function to demonstrate how to use the blog_agent_framework library.
    """
    # --- 1. Check for API Key ---
    if not os.getenv("OPENAI_API_KEY"):
        print("\033[91mError: OPENAI_API_KEY not found.\033[0m")
        print("Please create a .env file from the .env.example template and add your key.")
        return

    # --- 2. Define the Topic ---
    topic = "How to use AI for business ideas generation"
    model = "gpt-3.5-turbo"

    print(f"--- Starting blog post generation for topic: '{topic}' using model: {model} ---")

    # --- 3. Run the Agent Workflow ---
    try:
        full_agent_response = await generate_blog_post_with_review(topic=topic, model=model)
    except Exception as e:
        print(f"\033[91mAn error occurred during generation: {e}\033[0m")
        return

    # --- 4. Clean the Final Output ---
    clean_post = full_agent_response
    if "Final Version:" in full_agent_response:
        clean_post = full_agent_response.split("Final Version:", 1)[1].strip()
    else:
        print("\n\033[93mWarning: 'Final Version:' marker not found in the response. Displaying the full output.\033[0m")


    # --- 5. Display the Result ---
    print("\n\033[92m--- Generated Blog Post ---\033[0m")
    print(clean_post)


if __name__ == "__main__":
    asyncio.run(main())
