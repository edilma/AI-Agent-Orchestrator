import autogen

llm_config = {"model": "gpt-3.5-turbo"}

def create_writer():
    writer = autogen.AssistantAgent(
        name="Writer",
        system_message="You are a writer. You write engaging and concise " 
            "blogpost (with title) on given topics. You must polish your "
            "writing based on the feedback you receive and give a refined "
            "version. Only return your final work without additional comments.",
        llm_config=llm_config,
    )
    return writer
