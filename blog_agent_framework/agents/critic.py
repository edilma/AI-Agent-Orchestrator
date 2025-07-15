import autogen

def create_critic(llm_config):
    critic = autogen.AssistantAgent(
        name="Critic",
        is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
        llm_config=llm_config,
        system_message="You are a critic. You review the work of "
            "the writer and provide constructive feedback to help improve the quality of the content.",
    )
    return critic

