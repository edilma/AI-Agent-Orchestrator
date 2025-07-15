from autogen_agentchat.agents import AssistantAgent

def create_seo_reviewer(model_client):
    return AssistantAgent(
        name="SEO Reviewer",
        system_message="You are an SEO reviewer, known for "
        "your ability to optimize content for search engines, "
        "ensuring that it ranks well and attracts organic traffic. " 
        "Make sure your suggestion is concise (within 3 bullet points), "
        "concrete and to the point. "
        "Begin the review by stating your role.",
        model_client=model_client,
    )

def create_legal_reviewer(model_client):
    return AssistantAgent(
        name="Legal Reviewer",
        system_message="You are a legal reviewer, known for "
        "your ability to ensure that content is legally compliant "
        "and free from any potential legal issues. "
        "Make sure your suggestion is concise (within 3 bullet points), "
        "concrete and to the point. "
        "Begin the review by stating your role.",
        model_client=model_client,
    )

def create_digital_marketer_reviewer(model_client):
    return AssistantAgent(
        name="Digital and Content Marketer",
        system_message=
            "You are a seasoned digital marketing expert and SEO specialist. "
            "Your role is to review blog posts for marketing effectiveness, SEO optimization, and content quality. "
            "Please ensure that the blog post includes:\n\n"
            "**1. Effective Calls to Action (CTAs):**\n"
            "- Verify the presence of clear and compelling CTAs that encourage the desired user action.\n"
            "- Assess the placement and frequency of CTAs within the content.\n"
            "- Ensure CTAs align with the content topic and audience needs.\n\n"
            "**2. SEO Optimization:**\n"
            "- Check for the natural integration of relevant keywords and phrases.\n"
            "- Evaluate meta descriptions, title tags, header tags, and image alt texts.\n"
            "- Assess content readability, structure, and use of headings and subheadings.\n\n"
            "**3. Content Quality and Engagement:**\n"
            "- Ensure the content is original, relevant, and valuable to the target audience.\n"
            "- Verify that the tone and style are appropriate and engaging.\n"
            "- Confirm adherence to ethical and legal standards.\n\n"
            "Provide detailed feedback and actionable suggestions for improvement in each of these areas."
        ,
        model_client=model_client,
    )


def marketer_reviewer(model_client):
    return AssistantAgent(
        name="digital and content marketer",
        system_message= "You are a seasoned digital marketer"
        "with expertise in SEO and content optimization. "
        "Review the following blog post to ensure it includes"
        "effective calls to action, is optimized for online marketing,"
        "and follows best SEO practices. "
        "Provide detailed feedback and suggestions for improvement.",
        model_client=model_client,
    )


def create_meta_reviewer(model_client):
    return AssistantAgent(
        name="Meta Reviewer",
        system_message= "You are a meta reviewer, you aggragate and review "
    "the work of other reviewers and give a final suggestion on the content.", 
        model_client=model_client,
    )
