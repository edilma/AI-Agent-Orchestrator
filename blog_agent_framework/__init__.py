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

#function that will generate a blog post with reviews
#This function will create a team of agents, including the writer, critic, and various reviewers
async def generate_blog_post_with_review(topic, model="gpt-3.5-turbo"):
    model_client = create_model_client(model=model)
    writer = create_writer(model_client)
    critic = create_critic(model_client)
    digital_marketer_reviewer = create_digital_marketer_reviewer(model_client)
    legal_reviewer = create_legal_reviewer(model_client)
    seo_reviewer = create_seo_reviewer(model_client)
    meta_reviewer = create_meta_reviewer(model_client)

    # Set the termination condition for the team
    # The meta reviewer will signal the end of the blog post review process
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
    
    # Start the team chat
    chat_result = await team.run(
        task=f"Generate a complete, reviewed, and finalized blog post on the topic: {topic}."
    )
     # Check if there are enough messages to get the final post
    if chat_result.messages and len(chat_result.messages) > 1:
        # Return the content of the second to last message (the writer's final version)
        return chat_result.messages[-2].content
    
    
    return "The conversation ended before a blog post could be finalized."