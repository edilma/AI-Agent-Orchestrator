> ### ⚠️ Superseded by [`ai-blog-app`](https://github.com/edilma/ai-blog-app)
>
> This project is the first version of the framework and is no longer maintained.
> It works only with OpenAI, with the provider hardcoded.
>
> The successor, [**`ai-blog-app`**](https://pypi.org/project/ai-blog-app/), has the
> same multi-agent architecture with configurable providers — OpenAI, Gemini, Claude,
> and local models via Ollama — selectable per call.
>
> ```bash
> pip install ai-blog-app
> ```
>
> This repository stays available for anyone using the original package.



# Blog Agent Framework
📖 También disponible en [Español](README.es.md)

An advanced framework for building AI-powered content generation pipelines. This project uses a multi-agent system, powered by Microsoft Autogen, to autonomously write, critique, and review articles for quality, compliance, and SEO.
**Create smarter, better blogs—autonomously.**

The **Blog Agent Framework** is a plug-and-play Python library that helps you generate high-quality blog posts using a team of AI agents. Built on top of Microsoft’s powerful [Autogen](https://microsoft.github.io/autogen) system, this framework mimics a professional content team: a writer, a critic, and multiple expert reviewers work together to craft concise, SEO-optimized, story-driven articles, designed to engage readers and rank well in search engines.  Applies best practices in digital marketing to improve the reach, structure, and impact of each post. 

Whether you're a solo blogger, content marketer, or developer, you can use this library to automate content creation or integrate it into your own API.

---

## 🔧 Features
**🧩 Modular Agent Architecture**  
    Includes specialized agents for:
    - **Writer** – Crafts story-driven blog posts using simple, clear language  
    - **Content Marketing Reviewer** – Improves structure, flow, and engagement  
    - **Clarity & Ethics Reviewer** – Ensures content is easy to understand and free from misleading claims  
    - **SEO Reviewer** – Optimizes for discoverability on search engines like Google and AI tools

**💬 Intelligent Agent Collaboration**  
    Each agent plays a focused role in a structured review loop, and a meta-agent brings everything together into one polished result.

**📦 Use As a Library or API**  
    - Use the library directly in your Python projects  
    - Or build an API on top to serve real-time blog generation for your website or content service

**✅ SEO-Friendly & Reader-Focused**  
    Designed to help your content perform well on search engines *and* connect with real people—especially readers with a basic or general reading level.

## 📁 Project Structure
The project is structured as a standard Python package, making it easy to install and use.

    ```
    .
    ├── blog_agent_framework/    # The main library source code
    │   ├── agents/              # Contains the logic for individual AI agents
    │   ├── utils/               # Utility functions and helpers
    │   ├── __init__.py          # Exposes the main generation function
    │   └── config.py            # Handles model client configuration
    │
    ├── examples/                # Self-contained examples for users
    │   ├── .env.example         # Template for environment variables
    │   └── run_example.py       # Main script to demonstrate library usage
    │
    ├── .gitignore               # Specifies which files Git should ignore
    ├── LICENSE                  # The open-source license for the project
    ├── pyproject.toml           # The modern configuration file for the package
    └── README.md                # This file!

    ```

## 🚀 Installation

[![PyPI version](https://badge.fury.io/py/blog-agent-framework.svg)](https://badge.fury.io/py/blog-agent-framework)


Install from PyPI:

```bash
pip install blog-agent-framework
```
<sub>Requires Python 3.11+</sub>

Install the Blog Agent Framework directly from GitHub using pip:

```bash
pip install git+https://github.com/edilma/AI-Agent-Orchestrator.git
```

## ✍️ Basic Usage
Here's how to quickly get started with the built-in example.

### Running the Example

1.  Navigate into the examples directory:
    ```bash
    cd examples
    ```

2.  Create your own .env file by copying the template. 
    ```bash
    # On Windows
    copy .env.example .env

    # On macOS or Linux
    cp .env.example .env
    ```

3.  Add your OpenAi credentials to the new .env file
    ```bash
    OPENAI_API_KEY=your_openai_key_here
    OPENAI_PROJECT_ID=your_project_id_here
    ```

4.  Run the example script:
    ```bash
    python run_example.py
    ```
## 🧠 How It Works

The Blog Agent Framework simulates a collaborative writing and editing process using a team of specialized AI agents. Each agent plays a unique role in refining the blog post.

1. **Writer Agent**  
   Creates an initial blog post based on a topic prompt. The post is designed to be simple, engaging, and story-driven.

2. **Critic Agent**  
   Reviews the writer's draft and offers direct, actionable feedback. This agent evaluates story structure, clarity, tone, and flow—and helps polish the final version by incorporating all key reviewer suggestions.

3. **SEO Reviewer**  
   Ensures the blog includes relevant keywords, strong headings, and other on-page SEO elements to improve visibility on AI and search engines like Google and attracts organic traffic.

4. **Content Marketing Reviewer**  
   Analyzes structure, engagement, and presentation. Helps make sure the blog is clear, logically organized, and engaging for readers.

5. **Clarity and Ethics Reviewer**  
   Checks that the writing is easy to understand for a general audience, free of confusing or problematic language, and appropriate for public consumption.

The agents communicate intelligently to revise and refine the blog post until it meets quality standards for readability, SEO, and flow.

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software for personal or commercial use, with attribution.

## ✨ Author

Created with 💻 by **Edilma Riano**  
Helping businesses and creators use AI to work smarter and scale faster.

🐙 [Follow me on GitHub](https://github.com/edilma)  
