# 📜 Design Principles

> The guiding principles that shape every design, development, and maintenance decision within LogExplain.

![Project](https://img.shields.io/badge/Project-LogExplain-blue?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Project%20Documentation-success?style=for-the-badge)
![Document](https://img.shields.io/badge/Document-Design%20Principles-purple?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-0.1-lightgrey?style=for-the-badge)

---

## 📖 Purpose

LogExplain is intended to grow into a long-term educational open-source project.

As the project evolves, contributors will naturally introduce new ideas, features, and improvements. Without a shared philosophy, those changes can gradually pull the project away from its original mission.

This document defines the principles that guide decision-making throughout the project.

Whenever a design choice, feature proposal, or contribution is considered, it should be evaluated against these principles before implementation.

---

## 🎯 Mission

The mission of LogExplain is straightforward:

> **Help beginners understand security events through reasoning, investigation, and practical guidance.**

Every meaningful contribution should move the project closer to this goal.

If a proposed change does not improve the educational experience or help users develop analytical thinking, it should be reconsidered.

---

## 🌱 Guiding Principles

### 📚 Education Before Technology

LogExplain is an educational platform first and a software project second.

Technology exists to support learning, not to become the focus of the project.

When there is a choice between adding a technical feature and improving educational content, educational value takes priority.

---

### 🧠 Teach Reasoning, Not Memorisation

Security professionals do more than recognise Event IDs—they understand the context surrounding them.

LogExplain should encourage users to ask questions, investigate evidence, and understand why an event matters rather than simply remembering what it is.

The project should develop transferable analytical skills rather than isolated technical knowledge.

---

### 🔍 Encourage Investigation

A single log entry rarely provides the complete picture.

Instead of presenting definitive conclusions, LogExplain should encourage readers to continue investigating by considering surrounding events, related evidence, and possible explanations.

Curiosity and critical thinking are essential parts of the learning process.

---

### 📖 Knowledge Is the Core Product

The educational knowledge base is the foundation of LogExplain.

All interfaces—whether command-line, web, desktop, or mobile—exist to present that knowledge in different ways.

When improving the project, strengthening the knowledge base should generally take precedence over expanding interfaces.

---

### 🤝 Welcome Different Types of Contributions

Open-source projects succeed because people contribute in different ways.

Improving explanations, correcting documentation, refining investigation guidance, fixing grammar, writing tests, or reviewing changes all strengthen the project.

Meaningful contributions are not limited to writing Python code.

---

### ⚖️ Simplicity Enables Sustainability

Version 0.1 intentionally focuses on a small, well-designed foundation.

Every new feature increases maintenance requirements.

Features should only be introduced when they clearly support the project's mission and can be maintained over time.

Choosing not to implement a feature is sometimes the best design decision.

---

### 📏 Consistency Builds Trust

Users should know what to expect regardless of which security event they are reading.

Consistent structure, terminology, tone, and educational quality help create a reliable learning experience for both users and contributors.

---

## 🚫 Principles for Saying "No"

Not every good idea belongs in Version 0.1.

When evaluating a proposal, maintainers should ask:

* Does this improve the educational experience?
* Does it support the project's mission?
* Does it keep the project simple?
* Can contributors maintain it without unnecessary complexity?
* Is this the right time to introduce it?

If the answer to these questions is uncertain, it is usually better to postpone the idea until a future release.

---

## 🌍 Looking Ahead

LogExplain is designed with long-term growth in mind.

As the knowledge base expands, future versions may support additional log sources, interfaces, and educational content. However, growth should never come at the expense of clarity, consistency, or maintainability.

The project's philosophy should remain stable even as its capabilities evolve.

---

## 🔗 Related Documentation

This document explains **why** LogExplain is designed the way it is.

For other aspects of the project, see:

* `architecture.md` — How the project is structured.
* `knowledge-base-specification.md` — How security events are organised.
* `event-writing-guide.md` — How educational content should be written.
* `development-setup.md` — How to set up a development environment.
* `roadmap.md` — Planned milestones and future direction.

---

> *"Every design decision should make LogExplain a better teacher, not simply a larger project."*
