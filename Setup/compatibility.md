LangChain Compatibility Guide (Old → Modern 1.x)
================================================

Purpose
-------

LangChain has evolved rapidly. Many tutorials, blog posts, and GitHub examples still reference **pre-1.0 or early-1.x APIs** that no longer reflect how LangChain is designed today.

This document exists to:

-   Prevent confusion when following older resources

-   Explain *why* certain APIs were replaced

-   Show the **correct modern equivalents** used in this repository

-   Make version intent explicit (LangChain **1.1.x**)

If you copy code from the internet and it fails, this file is usually the reason.

* * * * *

Target Version
--------------

This repository targets:

-   `langchain==1.1.3`

-   `langchain-core==0.1.x`

-   `langchain-community==0.0.x`

All examples assume **modern LangChain 1.x APIs** only.

* * * * *

High-Level Design Shift (Important)
-----------------------------------

Before listing API changes, understand the core shift:

| Old LangChain | Modern LangChain 1.x |
| --- | --- |
| Chain-centric | Runnable-centric |
| Implicit behavior | Explicit composition |
| Hidden agent internals | Visible agent construction |
| String inputs | Structured inputs |
| Demo-oriented | System-oriented |

Most "breaking changes" are a result of this shift.

* * * * *

Major API Changes (Old → New)
-----------------------------

### 1\. `initialize_agent` → Explicit Agent Creation

#### Old (pre-1.0)

`from langchain.agents import initialize_agent

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description"
)`

#### Modern (1.x)

`from langchain.agents import create_agent, AgentExecutor

agent = create_agent(
    llm=llm,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools
)`

**Why this changed**

-   `initialize_agent` hid agent internals

-   Debugging and customization were difficult

-   Modern APIs separate **agent definition** from **execution**

This mirrors real system design.

* * * * *

### 2\. `create_react_agent` → `create_agent`

#### Older 1.x examples

`from langchain.agents import create_react_agent

agent = create_react_agent(llm, tools, prompt)`

#### Modern (1.1+)

`from langchain.agents import create_agent

agent = create_agent(
    llm=llm,
    tools=tools
)`

**Why this changed**

-   LangChain is moving away from hard-coding reasoning strategies

-   `create_agent` selects the appropriate internal strategy

-   ReAct is still supported, but not forced

This repository uses `create_agent` unless a reasoning pattern is being explicitly taught.

* * * * *

### 3\. `.run()` → `.invoke()`

#### Old

`agent.run("What is LangChain?")`

#### Modern

`agent_executor.invoke({
    "input": "What is LangChain?"
})`

**Why this changed**

-   `.run()` accepted unstructured input

-   `.invoke()` enforces explicit input schemas

-   Required for tools, memory, and observability

In modern LangChain, **everything is invoked**.

* * * * *

### 4\. `LLMChain` → Runnable Pipelines

#### Old

`from langchain import LLMChain

chain = LLMChain(
    llm=llm,
    prompt=prompt
)`

#### Modern

`chain = prompt | llm`

**Why this changed**

-   Runnables unify prompts, models, tools, and memory

-   Enables streaming, retries, tracing, and composition

-   Reduces boilerplate while increasing control

This is one of the most important conceptual changes in LangChain 1.x.

* * * * *

### 5\. Direct String Calls → Message-Based Invocation

#### Old

`llm("Hello")`

#### Modern

`from langchain_core.messages import HumanMessage

llm.invoke([
    HumanMessage(content="Hello")
])`

**Why this changed**

-   Conversations are multi-role (human, system, tool)

-   Agents require structured messages

-   Tool calls are represented as messages

Messages are now **first-class primitives**.

* * * * *

### 6\. Tools: Plain Functions → Schema-Aware Tools

#### Old

`def search(query: str) -> str:
    ...`

#### Modern

`from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search the web for information."""
    ...`

**Why this changed**

-   Tools now expose machine-readable schemas

-   Agents can reason about tool inputs safely

-   Required for multi-tool and production agents

All tools in this repo use `@tool`.

* * * * *

### 7\. Implicit Tool Usage → Explicit Tool Invocation

#### Old mental model

> "The agent just magically calls tools."

#### Modern mental model

-   The agent **decides**

-   The executor **invokes**

-   Tools are **validated and logged**

This separation improves:

-   Debugging

-   Observability

-   Control

* * * * *

### 8\. Deprecated Imports and Paths

Avoid these entirely:

| Deprecated | Modern |
| --- | --- |
| `langchain.llms` | `langchain_* integrations` |
| `langchain.agents.initialize_agent` | `create_agent` |
| `agent.run()` | `agent.invoke()` |
| `LLMChain` | Runnable pipelines |
| Experimental agent APIs | Stable agent APIs |

If you see these in a tutorial, it is likely outdated.

* * * * *

Common Failure Patterns (Why Code Breaks)
-----------------------------------------

### "This tutorial worked last month"

LangChain is version-sensitive. Always check:

`pip show langchain`

### Mixing old and new APIs

Example:

-   Using `LLMChain`

-   Then calling `.invoke()`

These belong to **different eras**.

### Tools without schemas

Agents will fail or behave unpredictably.

* * * * *

Repository Policy
-----------------

This repository:

-   Uses **LangChain 1.1.x only**

-   Avoids deprecated APIs entirely

-   Explains *why* something exists before using it

-   Treats agents as **system components**, not demos

If an API is missing here, it is intentional.

* * * * *

Final Note
----------

LangChain 1.x is not just a version bump.\
It is a **design correction**.

Once you understand the modern mental model, the APIs become:

-   More predictable

-   More composable

-   More production-ready

This repository is built to teach that model from the ground up