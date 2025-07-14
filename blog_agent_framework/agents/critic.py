import autogen

llm_config = {"model": "gpt-3.5-turbo"}

def create_critic():
    critic = autogen.AssistantAgent(
        name="Critic",
        is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
        llm_config=llm_config,
        system_message="You are a critic. You review the work of "
            "the writer and provide constructive feedback to help improve the quality of the content.",
    )
    return critic

