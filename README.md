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
✍️ Basic Usage
Here is a simple example of how to import and use the framework in your own Python script.

Prerequisite: You must have your OpenAI credentials set as environment variables. For modern project-based keys, this includes:

OPENAI_API_KEY (starting with sk-proj-...)

OPENAI_PROJECT_ID (starting with proj-...)

Python

import asyncio
import os
from blog_agent_framework import generate_blog_post_with_review

# This is an example of how you would run the async function
async def main():
    # Example of setting environment variables in a script
    # In a real app, you would use a .env file
    # os.environ["OPENAI_API_KEY"] = "sk-proj-YourSecretKey..."
    # os.environ["OPENAI_PROJECT_ID"] = "proj-YourProjectId..."

    # 1. Define a topic for the blog post
    topic = "The Benefits of a Mideterranean Diet"

    # 2. Call the main generation function using 'await'
    print(f"Generating blog post for topic: '{topic}'... this may take a few minutes.")
    final_post = await generate_blog_post_with_review(topic)

    # 3. Print the final, reviewed article
    print("\n--- Final Blog Post ---")
    print(final_post)

if __name__ == "__main__":
    asyncio.run(main())

📜 License
This project is licensed under the terms of the MIT License.

✨ Author
Built with 💻 by Edilma Riano using Python and Autogen.

Helping businesses and creators use AI to work smarter and scale faster.