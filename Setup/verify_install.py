"""
verify_install.py

Purpose:
- Verify Python version
- Verify LangChain installation
- Verify LLM connectivity
- Verify Tavily search tool

Run:
python 00-setup/verify_install.py
"""

import sys
import os

from dotenv import load_dotenv
load_dotenv()

# ---- Python version check ----
print("Python version:")
print(sys.version)
print("-" * 50)

# ---- LangChain version check ----
try:
    import langchain
    print("LangChain installed")
    print("LangChain version:", langchain.__version__)
except ImportError:
    raise RuntimeError("LangChain is not installed correctly")

print("-" * 50)

# ---- LLM check (Google Gemini) ----
try:
    from langchain_google_genai import GoogleGenerativeAI

    llm = GoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0
    )

    response = llm.invoke("Say hello in one sentence.")
    print("LLM call successful")
    print("LLM response:", response)

except Exception as e:
    raise RuntimeError(f"LLM check failed: {e}")

print("-" * 50)

# ---- Tavily search tool check ----
try:
    from langchain_community.tools.tavily_search import TavilySearchResults

    search = TavilySearchResults(max_results=2)
    results = search.invoke({"query": "What is LangChain?"})

    print("Tavily search successful")
    print("Sample result:", results[0])

except Exception as e:
    raise RuntimeError(f"Tavily check failed: {e}")

print("-" * 50)
print("Environment verification complete. You are ready to build.")
