
-----

# Blog Agent Framework

An advanced framework for building AI-powered content generation pipelines. This project uses a multi-agent system, powered by **Microsoft Autogen**, to autonomously write, critique, and review articles for quality, compliance, and SEO.

## 🔧 Features

  * **Modular Agent Architecture:** Easily configurable agents for writing, legal review, marketing, and SEO.
  * **Flexible Orchestration:** A nested chat structure allows for complex review and revision loops.
  * **Installable as a Library:** Designed to be used as a package in other Python applications.
  * **Extensible by Design:** Add new agent roles and capabilities by extending the core classes.

## 📁 Project Structure

The project is structured as a standard Python package, making it easy to install and use.

```
.
├── blog_agent_framework/
│   ├── __init__.py          # Exposes the main generation function
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── critic.py
│   │   ├── reviewers.py
│   │   └── writer.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## 🚀 Installation

Install the framework directly from GitHub using pip:

```bash
pip install git+https://github.com/edilma/AI-Agent-Orchestrator.git
```

## ✍️ Basic Usage

Here is a simple example of how to import and use the framework in your own Python script.

**Prerequisite:** You must have your LLM API key (e.g., `OPENAI_API_KEY`) set as an environment variable for the agents to function.

```python
import os
from blog_agent_framework import generate_blog_post_with_review

# Example of setting the environment variable in your script
# os.environ["OPENAI_API_KEY"] = "sk-YourSecretKey"

# 1. Define a topic for the blog post
topic = "The Future of Renewable Energy and its Impact on the Global Economy"

# 2. Call the main generation function
print("Generating blog post... this may take a few minutes.")
final_post = generate_blog_post_with_review(topic)

# 3. Print the final, reviewed article
print("\n--- Final Blog Post ---")
print(final_post)

```

## 📜 License

This project is licensed under the terms of the [MIT License](https://www.google.com/search?q=LICENSE).

## ✨ Author

Built with 💻 by Edilma Riano using Python and [Autogen](https://microsoft.github.io/autogen/stable//index.html).

Helping businesses and creators use AI to work smarter and scale faster.