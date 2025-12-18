### Purpose of this section

This section ensures that:

-   Your Python environment is correctly configured

-   LangChain **1.x (modern APIs only)** is installed

-   Required integrations (LLM + Tavily) are available

-   You can detect and fix setup issues **before** moving to chains or agents

This avoids the most common beginner frustration:

> "My code is correct, but nothing works."

* * * * *

Prerequisites
-------------

### 1\. Python Version

LangChain 1.x requires **Python 3.9+**.\
Python **3.10 or 3.11** is recommended.

Check your version:

`python --version`

If you see anything below 3.9, upgrade before proceeding.

* * * * *

2\. Create a Virtual Environment (Strongly Recommended)
-------------------------------------------------------

This repository assumes **isolated environments** to avoid dependency conflicts.

### Windows

`python -m venv .venv
.venv\Scripts\activate`

### macOS / Linux

`python3 -m venv .venv
source .venv/bin/activate`

You should now see `(.venv)` in your terminal.

* * * * *

3\. Install Core Dependencies
-----------------------------

Install **LangChain 1.x core**, an LLM provider, and Tavily search.

`pip install --upgrade pip
pip install langchain langchain-community langchain-core
pip install langchain-google-genai
pip install tavily-python
pip install python-dotenv`

### Why these packages?

| Package | Purpose |
| --- | --- |
| langchain | Core abstractions (chains, agents) |
| langchain-core | Messages, prompts, runnables |
| langchain-community | Community tools (Tavily, loaders) |
| langchain-google-genai | Google Gemini LLM integration |
| tavily-python | Real-time web search |
| python-dotenv | Secure API key loading |

* * * * *

4\. API Keys Setup
------------------

Create a `.env` file **in the root of the repository** (not inside `00-setup`).

`GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here`

### Important

-   Never commit `.env`

-   Add it to `.gitignore`

-   LangChain reads environment variables automatically

* * * * *

5\. Common Setup Errors (Read This)
-----------------------------------

### ❌ Error: `ModuleNotFoundError: langchain.agents`

**Cause:** Using old LangChain docs or partial installs\
**Fix:** Ensure `langchain` >= 1.x and use imports from `langchain.agents` (not experimental)

* * * * *

### ❌ Error: `Invalid API key`

**Cause:** `.env` not loaded or key is incorrect\
**Fix:**

-   Ensure `.env` is at repo root

-   Ensure `python-dotenv` is installed

-   Restart terminal after editing `.env`

* * * * *

### ❌ Error: `TypeError: object is not callable`

**Cause:** Mixing deprecated APIs with modern runnable APIs\
**Fix:** This repo **never uses deprecated patterns** --- follow examples strictly

* * * * *

6\. Verify Your Installation
----------------------------

Before writing any LangChain code, **run the verification script**:

`python 00-setup/verify_install.py`

You should see:

-   Python version

-   LangChain version

-   Successful LLM response

-   Successful Tavily search

If anything fails, fix it **before moving forward**.