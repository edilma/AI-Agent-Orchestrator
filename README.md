# Blog Agent Framework
An advanced framework for building AI-powered content generation pipelines. This project uses a multi-agent system, powered by Microsoft Autogen, to autonomously write, critique, and review articles for quality, compliance, and SEO.

## 🔧 Features
Modular Agent Architecture: Easily configurable agents for writing, legal review, marketing, and SEO.

Flexible Orchestration: A modern group chat structure allows for complex and intelligent review loops.

Installable as a Library: Designed to be used as a package in other Python applications.

Extensible by Design: Add new agent roles and capabilities by extending the core classes.

## 📁 Project Structure
The project is structured as a standard Python package, making it easy to install and use.

```
.
├── blog_agent_framework/
│   ├── __init__.py          # Exposes the main generation function
│   ├── config.py            # Handles model client configuration
│   ├── agents/
│   └── utils/
│
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## 🚀 Installation
Install the framework directly from GitHub using pip:

Bash

pip install git+https://github.com/edilma/AI-Agent-Orchestrator.git

## ✍️ Basic Usage
Here is a simple example of how to import and use the framework in your own Python script.

### Running the Example

1. Navigate to the examples directory: cd examples

2. Install required packages: pip install python-dotenv (and any others needed for the example).

3. Copy the environment template: cp .env.example .env

4. Open the new .env file and add your OpenAI API key.

5. Run the example: python run_example.py

Python


# This is an example of how you would run the async function
```
import asyncio
import os
from dotenv import load_dotenv
from blog_agent_framework import Orchestrator

# This line loads the variables from the .env file into the environment
load_dotenv()

async def main():
    # Now, your library can find the OPENAI_API_KEY automatically
    # because it's loaded into the environment.
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found. Please create a .env file from .env.example and add your key.")
        return

    topic = "The Future of Renewable Energy"
    orchestrator = Orchestrator()

    print(f"Generating post for topic: {topic}...")
    final_post = await orchestrator.run_workflow(topic)

    print("\n--- Generated Blog Post ---")
    print(final_post)

if __name__ == "__main__":
    asyncio.run(main())

```


📜 License
This project is licensed under the terms of the MIT License.

✨ Author
Built with 💻 by Edilma Riano using Python and Autogen.

Helping businesses and creators use AI to work smarter and scale faster.