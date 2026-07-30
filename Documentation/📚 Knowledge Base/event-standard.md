# 📝 LogExplain Event Standard

> The official specification that defines the required structure, sections, and educational flow for every LogExplain knowledge base entry.

![Project](https://img.shields.io/badge/Project-LogExplain-blue?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Event%20Standard-success?style=for-the-badge)
![Document](https://img.shields.io/badge/Document-Specification-purple?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)

---

# 📖 Purpose

The LogExplain Event Standard defines the official structure used by every knowledge base entry.

Its purpose is to ensure that all security events provide a consistent learning experience regardless of platform, event type, or contributor.

This document defines **what every event contains**.

For guidance on **how each section should be written**, see **`event-writing-guide.md`**.

---

# 🎯 Objectives

The Event Standard is designed to:

* 📚 Create a consistent educational experience.
* 🧠 Encourage analytical thinking.
* 🔍 Promote investigation over memorisation.
* 🤝 Make contributions predictable and maintainable.
* 🌍 Support future interfaces using the same knowledge base.

Every event should feel like part of the same educational resource.

---

# 🏛 Guiding Principles

Every LogExplain event follows these principles:

* One event, one consistent structure.
* Context determines significance.
* Security events are evidence—not conclusions.
* Teach reasoning before technical details.
* Encourage investigation before judgement.
* Every section should provide unique educational value.

---

# 🧩 Required Structure

Every knowledge base entry **must** include the following sections in the same order.

| Order | Section                    | Required |
| ----: | -------------------------- | :------: |
|     1 | 📌 Event Information       |     ✅    |
|     2 | 📖 Event Summary           |     ✅    |
|     3 | 🧠 Understanding the Event |     ✅    |
|     4 | ⚖️ Context Matters         |     ✅    |
|     5 | 🔍 Investigation Guide     |     ✅    |
|     6 | 📋 Investigation Checklist |     ✅    |
|     7 | 🧠 Think Like an Analyst   |     ✅    |
|     8 | 🌍 Real-World Relevance    |     ✅    |
|     9 | 🔗 Related Events          |     ✅    |
|    10 | 📚 Continue Learning       |     ✅    |
|    11 | 📌 Key Takeaways           |     ✅    |
|    12 | 🌱 Learning Reflection     |     ✅    |
|    13 | ➡️ Continue Your Journey   | Optional |

Contributors should not change the order of these sections.

---

# 📌 Event Information

Every event begins with a concise metadata table.

Recommended fields include:

| Property     | Example                             |
| ------------ | ----------------------------------- |
| Event ID     | 4625                                |
| Platform     | Windows                             |
| Category     | Authentication                      |
| Event Source | Microsoft-Windows-Security-Auditing |
| Common Tags  | Authentication, Failed Logon        |

This section provides quick reference information without explaining the event itself.

---

# 📖 Educational Flow

Every event should guide readers through a logical learning journey.

```text
Learn the Event
        │
        ▼
Understand What Happened
        │
        ▼
Understand the Context
        │
        ▼
Investigate the Evidence
        │
        ▼
Think Like an Analyst
        │
        ▼
Connect Related Knowledge
        │
        ▼
Reflect and Continue Learning
```

The structure should naturally progress from understanding to investigation and finally to reflection.

---

# 🔄 Standard Workflow

Every LogExplain event should answer these questions as the reader progresses through the document.

```text
What happened?
        │
        ▼
Why did it happen?
        │
        ▼
When does context matter?
        │
        ▼
How should I investigate?
        │
        ▼
How would an analyst think?
        │
        ▼
What should I learn next?
```

The reader should never be expected to memorise isolated facts.

---

# 🎨 Formatting Standards

To maintain consistency across the knowledge base:

* Use emoji headings consistently.
* Begin every event with project badges.
* Present metadata using tables.
* Use diagrams only when they improve understanding.
* Prefer short paragraphs over large blocks of text.
* Use checklists where appropriate.
* Keep terminology consistent across all events.

Formatting should improve readability rather than decorate the document.

---

# 🚫 Prohibited Changes

Contributors should not:

* Remove required sections.
* Rename standard section headings.
* Change the educational order.
* Replace investigation guidance with procedural instructions.
* Draw conclusions without context.
* Duplicate information across sections.

Consistency is essential to the quality of the knowledge base.

---

# 🔄 Versioning

The Event Standard evolves independently of the software.

Changes follow semantic versioning principles.

* **v1.x** — Minor improvements and clarifications.
* **v2.x** — Breaking structural changes.

Knowledge base entries may include the standard version they follow when appropriate.

---

# 🌍 Future Compatibility

The Event Standard is intentionally interface-independent.

The same knowledge base should be reusable by:

* 💻 Command-Line Interface
* 🌐 Website
* 📱 Mobile Application
* 🧩 VS Code Extension
* 🔌 REST API

Educational content should be written once and reused everywhere.

---

# 📚 Related Documentation

* `event-writing-guide.md`
* `knowledge-base-specification.md`
* `design-principles.md`
* `architecture.md`

---

> *"A consistent structure allows readers to spend less time learning where information is located—and more time learning how to investigate security events."*
