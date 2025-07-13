
# AI-Agent-Orchestrator

An advanced AI article (or blog) generator powered by multi-agent collaboration using [Autogen](https://microsoft.github.io/autogen/stable//index.html). This project uses autonomous agents to handle different tasks like writing, reviewing, and optimizing blog content for quality, compliance, and relevance.

## 🔧 Features

- Multi-agent architecture (writer, critic, reviewers)
- Built using the [Autogen framework](https://microsoft.github.io/autogen/stable//index.html)
- Topic selection via JSON or Python script
- Blog post generation to Markdown files
- Review and optimization loop using agents
- Easy-to-configure prompts and logic

## 📁 Project Structure

```
.
├── agents/                  # AI agents for writing and reviewing
│   ├── critic.py
│   ├── reviewers.py
│   ├── reviewers_old.py
│   └── writer.py
│
├── utils/                   # Helper functions
│   └── helpers.py
│
├── blog_post_1.md           # Generated blog examples
├── blog_post_2.md
├── blog_post_3.md
│
├── generate_blog.py         # Main script to generate blog posts
├── topics_python.py         # Optional Python topic generator
├── topics.json              # Topics list in JSON
├── requirements.txt         # Python dependencies
├── LICENSE
└── README.md


````

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/blog_generator_project.git
cd blog_generator_project
````

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Blog Generator

```bash
python generate_blog.py
```

This will create new blog posts using the agents and save them as Markdown files.

## ✍️ Customization

* Add topics to `topics.json` or edit `topics_python.py` if generating topics programmatically.
* You can modify agent behavior in `agents/`.

## 📜 License

This project is licensed under the terms of the [MIT License](LICENSE).

## ✨ Author

Built with 💻 by Edilma Riano using Python and [Autogen](https://microsoft.github.io/autogen/stable//index.html).

Helping businesses and creators use AI to work smarter and scale faster.
