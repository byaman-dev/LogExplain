# ✍️ Event Writing Guide

> Guidelines and standards for writing clear, consistent, and educational security event explanations for LogExplain.

![Project](https://img.shields.io/badge/Project-LogExplain-blue?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Writing%20Guide-success?style=for-the-badge)
![Document](https://img.shields.io/badge/Document-Contributor%20Guide-purple?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-0.1-lightgrey?style=for-the-badge)

---

# 📖 Purpose

LogExplain is an educational project.

Its goal is not simply to describe security events, but to teach beginners how an experienced security analyst would understand and investigate them.

This guide defines the writing standards that keep every event explanation accurate, approachable, and consistent.

---

# 🎯 Writing Goals

Every event explanation should:

* 📚 Teach rather than define.
* 🧠 Develop analytical thinking.
* 🔍 Encourage investigation.
* 🤝 Be accessible to beginners.
* 📖 Remain technically accurate.
* 🔄 Follow a consistent structure.

The objective is to help readers understand both **what happened** and **how to think about it**.

---

# 🧭 The Eight-Question Framework

Every event explanation in LogExplain follows the same educational structure.

## 1. What Happened?

Describe the event in plain English.

Assume the reader has never seen the event before.

---

## 2. Why Did It Happen?

Explain why the operating system, application, or service generated the event.

Provide context rather than simply repeating the event description.

---

## 3. Should I Worry?

Help readers judge whether the event is usually:

* Informational
* Expected
* Suspicious
* Potentially malicious

Avoid absolute answers whenever possible.

Context matters.

---

## 4. Why Should I Care?

Explain why the event is important during security monitoring or investigations.

Focus on practical significance rather than technical details alone.

---

## 5. What Can I Do?

Suggest reasonable next steps.

Examples include:

* Reviewing related logs
* Verifying user activity
* Confirming expected behaviour
* Escalating unusual findings

Recommendations should remain educational rather than procedural.

---

## 6. Where Should I Investigate?

Guide readers toward useful evidence.

Examples include:

* Related Event IDs
* Authentication logs
* Process activity
* Network activity
* System configuration

Teach where additional context can be found.

---

## 7. Think Like an Analyst

This is the educational heart of LogExplain.

Encourage readers to ask questions such as:

* Does this event fit the surrounding activity?
* Is this behaviour expected?
* What evidence supports my conclusion?
* What additional information would increase confidence?

The goal is to develop reasoning rather than memorisation.

---

## 8. Learn More

Provide trustworthy references for readers who want to continue learning.

Prefer official documentation whenever possible.

---

# ✍️ Writing Style

Use language that is:

* Professional
* Educational
* Friendly
* Objective
* Clear
* Concise

Write for understanding rather than impressing the reader.

---

# 🚫 Avoid

When writing event explanations, avoid:

* Fear-based language
* Marketing language
* Unexplained jargon
* Unsupported assumptions
* Vendor-specific bias
* Large blocks of text

Whenever technical terminology is necessary, explain it clearly.

---

# 💡 Writing Tips

Keep these practices in mind while writing:

* Explain ideas before introducing technical terms.
* Prefer short paragraphs over long ones.
* Use examples when they improve understanding.
* Focus on reasoning rather than memorisation.
* Keep explanations practical and actionable.
* Write as if mentoring someone new to cybersecurity.

---

# 📋 Quality Checklist

Before submitting a new event, confirm that:

* The explanation follows the eight-question framework.
* Technical information is accurate.
* The language is beginner-friendly.
* Investigation guidance is practical.
* Terminology is consistent.
* Grammar and spelling have been reviewed.

Every contribution should leave the knowledge base clearer than before.

---

# 🔗 Related Documentation

For additional information, see:

* `knowledge-base-specification.md` — Knowledge base structure and file format.
* `architecture.md` — How the application loads and presents event explanations.
* `design-principles.md` — Educational philosophy and project principles.
* `CONTRIBUTING.md` — General contribution guidelines.

---

> *"Great security analysts don't memorise every event—they learn how to ask better questions."*
