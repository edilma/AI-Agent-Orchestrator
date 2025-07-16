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
# Use the correct import paths based on your research
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination


async def generate_blog_post_with_review(topic, model="gpt-3.5-turbo"):
    model_client = create_model_client(model=model)
    writer = create_writer(model_client)
    critic = create_critic(model_client)
    digital_marketer_reviewer = create_digital_marketer_reviewer(model_client)
    legal_reviewer = create_legal_reviewer(model_client)
    seo_reviewer = create_seo_reviewer(model_client)
    meta_reviewer = create_meta_reviewer(model_client)

    # Use your new, more robust termination phrase
    # The chat will only end when the 'writer' agent's message includes this phrase
    
    termination_condition = TextMentionTermination(text="END_OF_BLOG_POST", sources=[meta_reviewer.name])
    # Create a SelectorGroupChat with all agents
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
        task=f"Generate a complete, reviewed, and finalized blog post on the topic: {topic}."
    )
    
    return chat_result.summary