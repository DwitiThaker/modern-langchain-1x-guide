2\. Mental Models (How to Think About LangChain)
------------------------------------------------

Before writing code, you need the **right way to think** about LangChain.

### Core Mental Model

LangChain is **not the brain**.\
The LLM is the brain.

LangChain is the **system that controls how the brain is used**.

* * * * *

### Simple Flow

```
Input
  ↓
Prompt / Messages
  ↓
LLM
  ↓
Output

```

This is the base of everything.

LangChain adds **structure and control** around this flow.

* * * * *

### LangChain's Role

LangChain helps you decide:

-   how input is formatted

-   what steps happen next

-   when tools are used

-   how outputs are handled

It does **not** make the model smarter.\
It makes the system **more reliable and organized**.

* * * * *

### Correct Way to Think About Components

| Component | Think of it as |
| --- | --- |
| Prompt | Instructions |
| Messages | Conversation state |
| Runnable | A step in a pipeline |
| Tool | An external action |
| Agent | A decision-maker |

Each part has **one clear job**.

* * * * *

### Why This Mental Model Matters

If you understand this:

-   LangChain code feels logical

-   Errors make sense

-   You know *why* an abstraction exists

If you don't:

-   You copy code blindly

-   Agents feel "magical"

-   Debugging becomes painful

This section exists to prevent that.

* * * * *
