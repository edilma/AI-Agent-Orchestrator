import os
from .config import create_model_client
from .agents.writer import create_writer
from .agents.critic import create_critic
from .agents.reviewers import (
    create_digital_marketer_reviewer,
    create_seo_reviewer,
    create_legal_reviewer,
    create_meta_reviewer,
)
# Import the new GroupChat components
from autogen_agentchat.groups import GroupChat, GroupChatManager

# The main function, refactored for the new Autogen version
def generate_blog_post_with_review(topic, model="gpt-3.5-turbo"):
    # 1. Create the model client
    model_client = create_model_client(model=model)

    # 2. Create all the agents by passing the model client
    writer = create_writer(model_client)
    critic = create_critic(model_client)
    digital_marketer_reviewer = create_digital_marketer_reviewer(model_client)
    legal_reviewer = create_legal_reviewer(model_client)
    seo_reviewer = create_seo_reviewer(model_client)
    meta_reviewer = create_meta_reviewer(model_client)

    # 3. Define the list of agents for the group chat
    agent_list = [
        writer,
        critic,
        digital_marketer_reviewer,
        legal_reviewer,
        seo_reviewer,
        meta_reviewer,
    ]

    # 4. Create the GroupChat object
    group_chat = GroupChat(
        agents=agent_list,
        messages=[],
        max_round=10,
        # The 'speaker_selection_method' can be customized for more complex workflows
        speaker_selection_method="auto" 
    )

    # 5. Create the GroupChatManager
    # This agent manages the conversation flow in the group chat
    group_chat_manager = GroupChatManager(
        groupchat=group_chat, 
        model_client=model_client
    )

    # 6. Start the conversation
    # The writer agent initiates the chat with the manager, providing the topic
    chat_result = writer.run(
        recipient=group_chat_manager, 
        task=f"Write a blog post about the following topic: {topic}"
    )

    # 7. Return the summary of the chat, which should be the final post
    return chat_result.summary