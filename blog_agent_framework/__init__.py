import json
from agents.writer import create_writer
from agents.critic import create_critic
from utils.helpers import create_task, save_blog_post
from agents.reviewers import create_digital_marketer_reviewer, create_seo_reviewer, create_legal_reviewer, create_meta_reviewer


# Function to generate a blog post with nested reviewers
def generate_blog_post_with_review(topic):
    writer = create_writer()
    critic = create_critic()
    digital_marketer_reviewer = create_digital_marketer_reviewer()
    legal_reviewer = create_legal_reviewer()
    #ethics_reviewer = create_ethics_reviewer()
    meta_reviewer = create_meta_reviewer()

    task = create_task(topic)
    reply = writer.generate_reply(messages=[{"content": task, "role": "user"}])

    # Define the nested review process
    review_chats = [
        {
        "recipient": legal_reviewer, 
         "message": reflection_message, 
         "summary_method": "reflection_with_llm",
         "summary_args": {
            "summary_prompt" : "Return review into as JSON object only:{'Reviewer': '', 'Review': ''}.",
         },
         "max_turns": 1
        },
        {
        "recipient": digital_marketer_reviewer, 
         "message": reflection_message, 
         "summary_method": "reflection_with_llm",
         "summary_args": {
            "summary_prompt" : "Return review into as JSON object only:{'Reviewer': '', 'Review': ''}",
         },
         "max_turns": 1
        },
                {
            "recipient": seo_reviewer, 
            "message": reflection_message, 
            "summary_method": "reflection_with_llm",
            "summary_args": {
                "summary_prompt" : "Return review into as JSON object only:{'Reviewer': '', 'Review': ''}",
            },
            "max_turns": 1
        },
        {
         "recipient": meta_reviewer, 
         "message": "Aggregate feedback from all reviewers and give final suggestions on the writing.", 
         "max_turns": 1
        }
    ]

       # Register the nested review chats 
    critic.register_nested_chats(review_chats, trigger=writer)

    # Critic reviews the post and initiates nested reviews
    res = critic.initiate_chat(
        recipient=writer,
        message=task,
        max_turns=2,
        summary_method="last_msg"
    )

    return res.summary