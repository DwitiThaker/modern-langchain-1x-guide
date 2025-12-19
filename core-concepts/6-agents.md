6\. Agents (Why They Exist and When to Use Them)
------------------------------------------------

### What an Agent Is

An **agent** is a system where the **LLM decides what to do next**.

Instead of following fixed steps, the model:

-   analyzes the input

-   chooses an action (or tool)

-   observes the result

-   decides again

This happens in a loop.

* * * * *

### Agent Flow (Conceptual)

```
Input
  ↓
LLM reasons
  ↓
Should I use a tool?
  ↓
Tool runs (if needed)
  ↓
Observation
  ↓
LLM reasons again
  ↓
Final answer

```

The key idea:

> **The model is making decisions, not executing code.**

* * * * *

### Why Agents Exist

Agents exist to handle problems where:

-   steps are not known in advance

-   tool choice depends on the question

-   reasoning is non-linear

Examples:

-   research assistants

-   multi-source question answering

-   exploratory tasks

* * * * *

### When You Should NOT Use Agents

Do **not** use agents when:

-   the steps are fixed

-   logic is predictable

-   performance matters

-   failure must be controlled

In these cases, use **runnable pipelines** instead.

* * * * *

### Simple Analogy

-   **Runnable pipeline** = recipe (fixed steps)

-   **Agent** = chef deciding what to do next

Both are useful.\
Using the wrong one causes problems.

* * * * *

### Why Beginners Struggle With Agents

Most tutorials:

-   introduce agents too early

-   treat them as magic

This repo introduces agents **after** you understand:

-   runnables

-   messages

-   tools

So agents feel logical, not confusing.

* * * * *

### What You Should Remember

Agents are:

-   powerful

-   flexible

-   harder to control

Use them **deliberately**, not everywhere.

* * * * *

### Step 3 Summary (Mental Model Check)

By now, you should understand:

-   what LangChain is

-   what runnables are

-   why messages exist

-   what agents actually do

You are now ready to start coding **with understanding**, not guessing.
