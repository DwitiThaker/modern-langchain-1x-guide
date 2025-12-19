4\. Messages & Prompts (Why Strings Are Not Enough)
---------------------------------------------------

### The Old Way of Thinking

Most beginners think:

> "I send a string to the model and get a string back."

That works only for **simple use cases**.

* * * * *

### The Modern Way (Correct Mental Model)

LLMs actually work with **messages**, not just text.

Each message has a **role**:

-   system (rules)

-   human (user input)

-   AI (model response)

-   tool (tool output)

LangChain makes this structure explicit.

* * * * *

### Why Messages Matter

Messages allow:

-   multi-turn conversations

-   tool usage

-   agent reasoning

-   clear separation of instructions vs input

Agents and tools **cannot work reliably with plain strings**.

* * * * *

### Prompts vs Messages

| Prompt | Message |
| --- | --- |
| Template | Conversation unit |
| Defines structure | Carries role + content |
| Used to create messages | Used by models and agents |

A prompt **creates messages**.\
Messages **drive the system**.

* * * * *

### Simple Analogy

Think of:

-   **Prompt** as a form template

-   **Messages** as filled forms sent to the model

LangChain handles this conversion so systems stay consistent.

* * * * *

### Why This Matters Before Coding

If you understand messages:

-   agent behavior makes sense

-   tool calls are clearer

-   debugging is easier

If you don't:

-   errors feel random

-   agent outputs feel unpredictable

This is why we learn this **before writing code**.
