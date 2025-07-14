import autogen

#checking if the git ignore is tracking this 

llm_config = {"model": "gpt-3.5-turbo"}

def create_seo_reviewer():
    return autogen.AssistantAgent(
        name="SEO Reviewer",
        system_message="You are an SEO reviewer, known for "
        "your ability to optimize content for search engines, "
        "ensuring that it ranks well and attracts organic traffic. " 
        "Make sure your suggestion is concise (within 3 bullet points), "
        "concrete and to the point. "
        "Begin the review by stating your role.",
        llm_config=llm_config,
    )

def create_legal_reviewer():
    return autogen.AssistantAgent(
        name="Legal Reviewer",
        system_message="You are a legal reviewer, known for "
        "your ability to ensure that content is legally compliant "
        "and free from any potential legal issues. "
        "Make sure your suggestion is concise (within 3 bullet points), "
        "concrete and to the point. "
        "Begin the review by stating your role.",
        llm_config=llm_config,
    )

# def create_ethics_reviewer():
#     return autogen.AssistantAgent(
#         name="Ethics Reviewer",
#         system_message= "You are an ethics reviewer, known for "
#         "your ability to ensure that content is ethically sound "
#         "and free from any potential ethical issues. " 
#         "Make sure your suggestion is concise (within 3 bullet points), "
#         "concrete and to the point. "
#         "Begin the review by stating your role. ",
#         llm_config=llm_config,
#     )

def create_digital_marketer_reviewer():
    return autogen.AssistantAgent(
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
        llm_config=llm_config,
    )














def marketer_reviewer():
    return autogen.AssistantAgent(
        name="digital and content marketer",
        system_message= "You are a seasoned digital marketer"
        "with expertise in SEO and content optimization. "
        "Review the following blog post to ensure it includes"
        "effective calls to action, is optimized for online marketing,"
        "and follows best SEO practices. "
        "Provide detailed feedback and suggestions for improvement.",
        llm_config=llm_config,
    )


def create_meta_reviewer():
    return autogen.AssistantAgent(
        name="Meta Reviewer",
        system_message= "You are a meta reviewer, you aggragate and review "
    "the work of other reviewers and give a final suggestion on the content.", 
        llm_config=llm_config,
    )
