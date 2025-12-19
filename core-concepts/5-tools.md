5\. Tools (How LLMs Interact With the Real World)
-------------------------------------------------

### What a Tool Is

A **tool** is a function the LLM is allowed to use.

LLMs can reason and write, but they **cannot**:

-   search the internet

-   access databases

-   call APIs

-   run calculations reliably

Tools give the model **capabilities beyond text**.

* * * * *

### What Tools Are Used For

Tools are used when the model needs:

-   external information (search)

-   fresh data

-   system actions

-   deterministic results

LangChain treats tools as **controlled entry points** to the real world.

* * * * *

### How Tools Fit in the System

```
LLM
 ↓ decides
Tool
 ↓ returns result
LLM

```

Important:

> The model **chooses** whether to use a tool.\
> The code **executes** the tool.

This separation is intentional.

* * * * *

### Why Tools Are Structured (Not Random Functions)

In LangChain 1.x, tools:

-   have input schemas

-   are validated

-   are observable

This prevents:

-   unsafe calls

-   malformed inputs

-   unpredictable behavior

Tools are designed like APIs, not shortcuts.

* * * * *

### Simple Analogy

Think of tools as:

-   approved actions in a company system

The employee (LLM) can:

-   request an action\
    But the system:

-   validates

-   executes

-   logs it

* * * * *

### Why This Matters Before Coding

If you understand tools:

-   agent behavior makes sense

-   failures are easier to debug

-   systems feel controlled, not magical

Tools are the **bridge between reasoning and action**.

* * * * *

### Important Rule

**Never assume the model can "just do" something.**\
If it needs external data or action, it needs a tool.