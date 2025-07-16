import os
import asyncio
from .config import create_model_client
from .agents.writer import create_writer
from .agents.critic import create_critic
from .agents.reviewers import (
    create_digital_marketer_reviewer,
    create_seo_reviewer,
    create_legal_reviewer,
    create_meta_reviewer,
)

from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination

# The main function, refactored for the new Autogen version using async selector group chat
async def generate_blog_post_with_review(topic, model="gpt-3.5-turbo"):
    model_client = create_model_client(model=model)
    writer = create_writer(model_client)
    critic = create_critic(model_client)
    digital_marketer_reviewer = create_digital_marketer_reviewer(model_client)
    legal_reviewer = create_legal_reviewer(model_client)
    seo_reviewer = create_seo_reviewer(model_client)
    meta_reviewer = create_meta_reviewer(model_client)

    # Create a termination condition
    # This will stop the chat when any agent says the word "TERMINATE"
    termination_condition = TextMentionTermination("TERMINATE")

    team = SelectorGroupChat(
        [
            writer,
            critic,
            digital_marketer_reviewer,
            legal_reviewer,
            seo_reviewer,
            meta_reviewer,
        ],
        model_client=model_client,
       
        termination_condition=termination_condition,
    )

    chat_result = await team.run(
        task=f"Write a blog post about the following topic: {topic}. Get feedback and reviews, then provide the final, refined version. Conclude your final message with the word TERMINATE."
    )
    
    # Return the content of the very last message in the chat
    if chat_result.messages:
        return chat_result.messages[-1].content
    return "No result was generated."