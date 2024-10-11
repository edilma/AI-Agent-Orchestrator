# Imports from the agents module
import json
from agents.writer import create_writer
from agents.critic import create_critic
from utils.helpers import create_task, save_blog_post
from agents.reviewers import create_seo_reviewer, create_legal_reviewer, create_ethics_reviewer, create_meta_reviewer

# Function to load topics from the JSON file
def load_topics_from_json(filename):
    with open(filename, 'r') as file:
        topics = json.load(file)
    return topics

def reflection_message(recipient, messages, sender, config):
    return f'''Review the following content. 
            \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}'''


# Function to generate a blog post with nested reviewers
def generate_blog_post_with_review(topic):
    writer = create_writer()
    critic = create_critic()
    seo_reviewer = create_seo_reviewer()
    legal_reviewer = create_legal_reviewer()
    ethics_reviewer = create_ethics_reviewer()
    meta_reviewer = create_meta_reviewer()

    task = create_task(topic)
    reply = writer.generate_reply(messages=[{"content": task, "role": "user"}])

    # Define the nested review process
    review_chats = [
        {
         "recipient": seo_reviewer, 
         "message": reflection_message, 
         "summary_method": "reflection_with_llm",
         "summary_args": {
            "summary_prompt" : "Return review into as JSON object only:{'Reviewer': '', 'Review': ''}. Here Reviewer should be your role",
         },
         "max_turns": 1
        },
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
        "recipient": ethics_reviewer, 
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

if __name__ == "__main__":
     # Load topics from the JSON file
    topics = load_topics_from_json("topics.json")

    # Iterate through each topic and generate blog posts
    for i, topic_data in enumerate(topics):
        topic = topic_data['title']
        blog_post = generate_blog_post_with_review(topic)
        
        # Print and save each blog post
        print(f"Blog post for topic '{topic}':\n{blog_post}\n")
        save_blog_post(blog_post, f"blog_post_{i+1}.md")