# ✍️ Event Writing Guide

> Guidelines for writing clear, consistent, and educational security event explanations that teach readers **how to think like a security analyst**, not simply what an event means.

![Project](https://img.shields.io/badge/Project-LogExplain-blue?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Writing%20Guide-success?style=for-the-badge)
![Document](https://img.shields.io/badge/Document-Contributor%20Guide-purple?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)

---

# 📖 Purpose

LogExplain is an educational cybersecurity project.

Its goal is not to create another Event ID reference or reproduce vendor documentation. Instead, it helps readers understand security events through reasoning, investigation, and practical thinking.

This guide defines the writing standards that keep every knowledge base entry accurate, approachable, and consistent.

It is intended for anyone contributing new security events or improving existing explanations.

---

# 🎯 Writing Philosophy

Every LogExplain event should help readers answer three questions:

* **What happened?**
* **Why does it matter?**
* **How should I investigate it?**

More importantly, every explanation should encourage readers to think critically rather than memorise facts.

> **Core Principle**
>
> **LogExplain does not tell readers what to think. It teaches them how to think.**

---

# 📝 Follow the Event Standard

Every knowledge base entry **must** follow the **LogExplain Event Standard v1.0**.

The Event Standard defines:

* Required sections
* Document structure
* Educational flow
* Consistent formatting

This guide explains **how to write each section**, while the Event Standard defines **what every event contains**.

---

# ✍️ General Writing Principles

When writing for LogExplain, always aim to be:

* 📚 Educational
* 🧠 Analytical
* 🤝 Beginner-friendly
* 🎯 Practical
* 🔍 Objective
* 📖 Technically accurate

Explain concepts before introducing technical terminology whenever possible.

Assume the reader is motivated to learn but may have little or no prior experience with security logs.

---

# 🧩 Writing Each Section

## 📖 Event Summary

The Event Summary introduces the event in plain English.

A good summary should:

* Explain the event in two or three concise paragraphs.
* Avoid unnecessary technical language.
* Give readers enough context before exploring the details.

Avoid copying vendor documentation.

Rewrite information using your own words.

---

## 🧠 Understanding the Event

This section explains what the event represents and why it occurs.

Describe:

* What generated the event.
* Why the operating system or application created it.
* Common legitimate situations.
* Possible security-related situations.

Remember that identical events may occur during both normal operation and malicious activity.

---

## ⚖️ Context Matters

One of the most important sections in LogExplain.

Never encourage readers to make conclusions based on a single event.

Instead, explain:

* Situations where the event is expected.
* Situations where additional investigation is appropriate.
* Why surrounding context changes the interpretation.

Avoid statements such as:

* "This event is malicious."
* "This always indicates an attack."

Instead, write:

> This event may warrant further investigation depending on the surrounding activity and available evidence.

---

## 🔍 Investigation Guide

Teach readers how experienced analysts investigate the event.

Present investigation as a logical process rather than a checklist of isolated actions.

Guide readers towards useful sources of evidence.

Examples include:

* Related security events
* User accounts
* Host information
* Network activity
* Process activity
* Authentication history

The goal is to demonstrate investigation methodology rather than provide incident response procedures.

---

## 📋 Investigation Checklist

Provide practical questions that encourage systematic investigation.

Checklist items should help readers gather evidence before reaching conclusions.

Examples:

* Identify the affected account.
* Review the originating host.
* Examine nearby events.
* Look for repeated activity.
* Verify whether the behaviour is expected.

Avoid writing checklists that assume malicious activity.

---

## 🧠 Think Like an Analyst

This is the educational heart of every LogExplain event.

Rather than giving answers, encourage curiosity.

Ask questions that help readers build analytical habits.

Examples include:

* What evidence supports this conclusion?
* What evidence contradicts it?
* Is this behaviour normal for this environment?
* Have related events been reviewed?
* Am I making assumptions?

A good analyst investigates evidence before reaching conclusions.

LogExplain should encourage the same mindset.

---

## 🌍 Real-World Relevance

Help readers understand why the event matters outside of a lab environment.

Discuss where they may encounter the event.

Examples include:

* Security Operations Centres (SOC)
* Incident Response
* Threat Hunting
* Enterprise Administration
* Digital Forensics
* Security Monitoring

Keep this section practical rather than theoretical.

---

## 🔗 Related Events

Security events rarely exist in isolation.

Explain how related events provide additional context.

Whenever possible, describe the relationship instead of simply listing Event IDs.

Encourage readers to correlate multiple sources of evidence.

---

## 📚 Continue Learning

Recommend trustworthy resources that expand the reader's understanding.

Prefer:

* Official vendor documentation
* MITRE ATT&CK
* Sigma Rules
* Industry best practices
* Academic or technical references

Do not duplicate external documentation.

Instead, explain why each resource is valuable.

---

## 📌 Key Takeaways

Summarise the event using concise, memorable points.

Good takeaways reinforce understanding rather than repeat earlier sections.

Readers should be able to review this section quickly before moving to the next event.

---

## 🌱 Learning Reflection

Every LogExplain event should conclude with reflection.

Rather than summarising technical details, explain what investigative mindset or security concept the reader has developed.

Focus on learning rather than memorisation.

---

# 🎨 Writing Style

Write as if mentoring someone who is new to cybersecurity.

Your writing should be:

* Friendly without being informal.
* Professional without being overly academic.
* Clear without oversimplifying technical concepts.
* Encouraging without making assumptions about the reader's knowledge.

Prefer short paragraphs.

Use headings, tables, lists, and diagrams where they improve readability.

---

# 🚫 Common Mistakes

Avoid the following:

* ❌ Copying vendor documentation.
* ❌ Large blocks of text.
* ❌ Fear-based language.
* ❌ Definitive conclusions without evidence.
* ❌ Unexplained jargon.
* ❌ Vendor-specific bias.
* ❌ Repeating information across sections.

Every section should contribute something new.

---

# ✅ Quality Checklist

Before submitting an event, confirm that:

* [ ] The event follows the LogExplain Event Standard v1.0.
* [ ] Every section provides unique educational value.
* [ ] Technical information has been verified.
* [ ] The language is beginner-friendly.
* [ ] Conclusions are evidence-based.
* [ ] Investigation guidance encourages analytical thinking.
* [ ] The document has been reviewed for grammar, spelling, and consistency.

---

# 🤝 Final Principle

Every LogExplain contribution should leave readers with better questions—not just more answers.

If an explanation encourages curiosity, investigation, and evidence-based reasoning, it supports the mission of the project.

---

# 🔗 Related Documentation

* `event-standard.md`
* `knowledge-base-specification.md`
* `design-principles.md`
* `architecture.md`
* `CONTRIBUTING.md`

---

> *"The goal of LogExplain is not to create people who recognise Event IDs. It is to help create analysts who recognise patterns, ask better questions, and investigate with evidence."*
