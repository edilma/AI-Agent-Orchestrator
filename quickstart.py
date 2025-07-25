# 1. Define a topic for the blog post
import asyncio 
import os 
from blog_agent_framework import generate_blog_post_with_review


async def main():
    topic = "The Future of Renewable Energy"

    # Initialize the orchestrator
    orchestrator = await generate_blog_post_with_review(topic)

    # Run the agent workflow
    print(f"Generating post for topic: {topic}...")
    final_post = await orchestrator.run_workflow(topic)

    print("\n--- Generated Blog Post ---")
    print(final_post)

if __name__ == "__main__":
    asyncio.run(main())