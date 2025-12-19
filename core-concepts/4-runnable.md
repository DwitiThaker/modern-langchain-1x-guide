### What Is a Runnable?

A **Runnable** is anything that:

-   takes input

-   does some work

-   returns output

That's it.

In LangChain 1.x, **almost everything is a Runnable**.

* * * * *

### Examples of Runnables

-   Prompt templates

-   LLMs

-   Tools

-   Chains

-   Agents

They all follow the same input → output idea.

* * * * *

### Why Runnables Exist

Runnables allow LangChain to:

-   connect steps together

-   reuse components

-   swap parts easily

-   debug each step separately

Without runnables, systems become tightly coupled and hard to change.

* * * * *

### Runnable Composition (Important)

Runnables can be connected using `|`:

```
prompt | llm

```

Think of it as:

```
output of prompt → input of llm

```

Each step does **one job**, then passes the result forward.

* * * * *

### Simple Analogy

Think of runnables like **assembly line stations**.

-   Each station performs one task

-   Output of one station feeds the next

-   You can replace a station without breaking the whole line

LangChain systems are built the same way.

* * * * *

### Why You Should Care

Understanding runnables means:

-   you understand modern LangChain

-   chains and agents stop feeling confusing

-   you build systems instead of scripts

This is the most important concept in LangChain 1.x.
