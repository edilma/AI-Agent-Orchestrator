from autogen_agentchat.agents import AssistantAgent

def create_critic(model_client):
    critic = AssistantAgent(
        name="Critic",
        is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
        model_client=model_client,
        system_message="You are a critic. You review the work of "
            "the writer and provide constructive feedback to help improve the quality of the content.",
    )
    return critic

