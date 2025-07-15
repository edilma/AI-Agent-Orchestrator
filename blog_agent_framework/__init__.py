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
# Import from the new 'teams' module
from autogen_agentchat.teams import SelectorGroupChat

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

   # 3. Create the SelectorGroupChat team
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
    )

     # 4. Run the chat
    # The new, simpler way to start and run the entire conversation
    chat_result = team.run(
        task=f"Write a blog post about the following topic: {topic}. Get feedback and reviews, then provide the final version."
    )

    # 5. Return the summary
    return chat_result.summary