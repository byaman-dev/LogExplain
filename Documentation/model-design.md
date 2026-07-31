# 🏗️ LogExplain Model Design

> **Purpose**
>
> This document defines the design philosophy behind the LogExplain data models.
> It explains **what the models should represent, what they should not represent,
> and why they are designed this way.**
>
> Every future change to `models.py` should follow the principles described here.

---

# Philosophy

LogExplain is an **educational knowledge base**, not a database.

The primary product is the **Markdown knowledge base**.

Python exists only to:

- validate content
- load content
- render content
- power the CLI

The application should never dictate how educational content is written.

Instead, the educational content should define the application.

---

# Source of Truth

The canonical source of truth is:

```
Markdown
        ↓
Models
        ↓
Loader
        ↓
Renderer
        ↓
CLI
```

The Markdown knowledge base always comes first.

The models describe the Markdown.

They do **not** define it.

---

# Design Principles

## 1. Markdown First

Every knowledge base article is written in Markdown.

The Markdown is the product.

Python simply understands it.

---

## 2. Structure Only What Needs Structure

Ask one question for every section:

> **Will the application need to query this information?**

If the answer is **yes**, create a structured model.

Examples:

- Event Information
- Related Events
- Continue Learning
- Key Takeaways

If the answer is **no**, keep it as educational Markdown.

Examples:

- Event Summary
- Understanding the Event
- Context Matters
- Think Like an Analyst

Educational writing should remain flexible.

---

## 3. One Model per Canonical Section

Every top-level Markdown section corresponds to one model.

This creates a predictable relationship between the document and the code.

```
Markdown Section
        ↓
Python Model
```

This consistency makes the project easier to understand, maintain, and extend.

---

## 4. Don't Over-Engineer Educational Content

Educational writing should not be broken into dozens of artificial fields.

Bad:

```python
what_happened
why_it_happened
legitimate_causes
malicious_causes
```

Good:

```python
content
```

The Markdown already provides structure.

The model should preserve that freedom.

---

## 5. Separate Metadata from Knowledge

LogExplain contains two different kinds of information.

### Metadata

Information primarily used by the application.

Examples:

- Event ID
- Platform
- Provider
- Category
- Related Events

---

### Educational Knowledge

Information written for humans.

Examples:

- Event Summary
- Investigation Guide
- Context Matters
- Learning Reflection

These should remain expressive, readable, and easy to improve over time.

---

## 6. Future-Proof the Knowledge Base

Educational content will evolve.

Future versions may include:

- diagrams
- callout blocks
- examples
- timelines
- exercises
- notes
- warnings

The model should allow these improvements without requiring structural changes.

---

# Canonical Event Structure

Every event follows the same section order.

```
📌 Event Information

📖 Event Summary

🧠 Understanding the Event

⚖️ Context Matters

🔍 Investigation Guide

📋 Investigation Checklist

🧠 Think Like an Analyst

🌍 Real-World Relevance

🔗 Related Events

📚 Continue Learning

📌 Key Takeaways

🌱 Learning Reflection
```

This is the official LogExplain Event Standard.

---

# Structured Sections

These sections contain machine-readable information.

- Event Information
- Investigation Checklist
- Related Events
- Continue Learning
- Key Takeaways

These should have dedicated models.

---

# Educational Sections

These sections primarily contain educational prose.

- Event Summary
- Understanding the Event
- Context Matters
- Investigation Guide
- Think Like an Analyst
- Real-World Relevance
- Learning Reflection

These should remain flexible and primarily be stored as Markdown content.

---

# Design Goal

The purpose of the models is **not** to describe Windows.

The purpose of the models is to describe a **LogExplain knowledge article**.

That distinction is important.

Windows may change.

Cybersecurity may evolve.

The educational standard may improve.

The document structure should remain stable.

---

# Long-Term Vision

The architecture should allow future interfaces without changing the knowledge base.

For example:

```
Markdown
      │
      ├── CLI
      ├── Website
      ├── Desktop App
      ├── Mobile App
      ├── REST API
      └── VS Code Extension
```

Every interface should consume the same validated knowledge.

The knowledge base should only need to be written once.

---

# Final Principle

> **The models should describe the document—not dictate it.**

The Markdown knowledge base is the product.

Everything else exists to serve it.
