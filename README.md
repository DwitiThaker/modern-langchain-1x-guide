
```
## modern-langchain-1x-guide

A hands-on, beginner-to-intermediate guide to **LangChain 1.x** --- covering prompts, chains, agents, tools, Tavily search, and real-world AI workflows with clean, well-explained examples.

---

## 🚀 What is this repository?

This repository is a **practical, from-scratch guide to LangChain 1.x**, built while learning and experimenting with modern LangChain APIs.

Unlike many outdated tutorials, this guide:
- Uses **LangChain ≥ 1.1.x**
- Avoids deprecated APIs
- Focuses heavily on **agents, tools, and real-world patterns**
- Explains **why things break**, not just how to make them work

The goal is to help students and developers **actually understand LangChain**, not just copy code.

---

## 🎯 Who is this for?

This repo is designed for:
- Students learning AI / LLM frameworks
- Beginners starting with LangChain
- Developers transitioning from simple LLM calls to **agents**
- Anyone confused by LangChain 1.x changes

You should be comfortable with:
- Basic Python
- Virtual environments
- Reading error messages (we do this a lot here)

---

## 🧠 What you will learn

By the end of this guide, you will understand:

- How to use LLMs correctly in LangChain
- Prompt engineering with `PromptTemplate`
- Chains and why **order matters**
- Output parsers (string & JSON)
- What agents actually are (and are not)
- How tools work and how agents choose them
- Tavily web search (manual + agent-based)
- When to search vs when not to search
- Real-world AI workflow patterns

---

## 🧭 Learning Path

The repository follows this learning progression:

```

LLMs\
↓\
Prompt Engineering\
↓\
Chains\
↓\
Output Parsers\
↓\
Agents (Core)\
↓\
Custom Tools\
↓\
Tavily Search\
↓\
Real-World AI Patterns

```

Each folder builds on the previous one.

---

## 📁 Repository Structure

```

modern-langchain-1x-guide/\
│\
├── 00-setup/ # Environment setup & verification\
├── 01-llm-basics/ # Basic LLM usage\
├── 02-prompt-engineering/ # Prompt templates & best practices\
├── 03-chains/ # Chains & LCEL basics\
├── 04-output-parsers/ # Structured outputs\
├── 05-agents-core/ # What agents really are\
├── 06-custom-tools/ # Writing and using tools\
├── 07-tavily-search/ # Web search with Tavily\
├── 08-real-world-patterns/# Production-style workflows\
│\
├── requirements.txt\
├── .env.example\
└── README.md

```

---

## ⚙️ Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/modern-langchain-1x-guide.git
cd modern-langchain-1x-guide

```

### 2️⃣ Create and activate a virtual environment

```
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows

```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt

```

### 4️⃣ Set up environment variables

Copy `.env.example` to `.env` and add your API keys:

```
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

```

### 5️⃣ Verify setup

Run the setup verification script:

```
python 00-setup/verify_install.py

```

If this runs successfully, you're ready to start learning.

* * * * *

⚠️ Important Notes
------------------

-   This repo targets **LangChain 1.x** (not 0.x)

-   Many online tutorials use **deprecated APIs**

-   Agents in LangChain 1.x behave differently than older versions

-   Chat models are required for agents (not text models)

These differences are explained throughout the repo.

* * * * *

👩‍💻 Author
------------

This repository is created and maintained by **Dwiti Thaker**.

-   Focus areas: AI agents, applied ML, LangChain, real-world AI systems

-   Built as a **learning project** 

-   Designed to help other students avoid the confusion I faced while learning LangChain

If this repo helps you, feel free to ⭐ star it or share it with others.

* * * * *

📌 Disclaimer
-------------

This is an educational repository.\
APIs and libraries evolve quickly --- always refer to official documentation for production use.

* * * * *

Happy building 🚀

