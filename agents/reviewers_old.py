import autogen

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
def marketer_reviewer():
    return autogen.AssistantAgent(
        name="digital and content marketer",
        system_message= "You are a seasoned digital marketer"
        "with expertise in SEO and content optimization. "
        "Review the following blog post to ensure it includes"
        "effective and relevant calls to action, seo optimization,"
        "including keyword usage, meta tags and readability "
        "Alignment with best practices in content marketing and SEO." 
        "Provide detailed feedback and actionable suggestions for improvement.",
        llm_config=llm_config,
    )


def create_meta_reviewer():
    return autogen.AssistantAgent(
        name="Meta Reviewer",
        system_message= "You are a meta reviewer, you aggragate and review "
    "the work of other reviewers and give a final suggestion on the content.", 
        llm_config=llm_config,
    )
