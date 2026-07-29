# 📚 Knowledge Base Specification

> The official specification for LogExplain's educational knowledge base, including its structure, organization, and formatting requirements.

![Project](https://img.shields.io/badge/Project-LogExplain-blue?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Knowledge%20Base-success?style=for-the-badge)
![Document](https://img.shields.io/badge/Document-Specification-purple?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-0.1-lightgrey?style=for-the-badge)

---

# 📖 Purpose

The knowledge base is the foundation of LogExplain.

Every educational explanation is stored as an individual Markdown document, making the knowledge base the project's single source of truth.

This document defines how the knowledge base is organised, how event files are structured, and the rules that every knowledge entry must follow.

---

# 🎯 Design Goals

The knowledge base is designed to be:

* 📚 Human-readable
* 🤝 Easy to contribute to
* 🔄 Consistent across every event
* ✅ Machine-validated
* 🌱 Easy to extend over time

These goals ensure that contributors can improve educational content without modifying the application's source code.

---

# 📂 Directory Structure

Version **0.1** supports Windows Security Events only.

```text
knowledge/
└── windows/
    ├── 4624.md
    ├── 4625.md
    ├── 4634.md
    └── ...
```

Future versions may introduce additional directories for other log sources while preserving the same overall structure.

---

# 📄 Event File Structure

Each security event is stored as an individual Markdown document.

The filename should match the event identifier whenever possible.

Example:

```text
knowledge/windows/4625.md
```

Every event file consists of two sections:

1. YAML Front Matter
2. Markdown Content

```text
---
YAML Front Matter
---

Markdown Content
```

---

# 🏷 YAML Front Matter

The front matter contains structured metadata used by the application.

Example:

```yaml
---
id: 4625
title: An account failed to log on
platform: windows
category: authentication
severity: medium
source: Security
---
```

The front matter should describe the event rather than explain it.

Educational content belongs in the Markdown body.

---

# 📝 Markdown Content

The Markdown body contains the educational explanation presented to users.

Content should remain readable both in GitHub and through the command-line interface.

Version **0.1** follows a consistent educational structure for every event.

The exact writing standards are documented in **`event-writing-guide.md`**.

---

# 📏 Knowledge Base Rules

Every knowledge entry should follow these principles:

* One file represents one security event.
* Metadata belongs in YAML front matter.
* Educational explanations belong in Markdown.
* Event files should remain self-contained.
* Avoid duplicating information across multiple entries.
* Use consistent terminology throughout the knowledge base.

These rules help maintain consistency as the project grows.

---

# ✅ Validation

Before an event is presented to users, LogExplain validates the knowledge entry.

Validation checks include:

* Required metadata fields
* Expected data types
* Valid file structure
* Supported schema version

Validation ensures that every event follows the same specification and helps prevent inconsistent or incomplete entries.

---

# 🌱 Future Growth

The specification has been designed to support additional log sources without changing the overall structure.

Possible future directories include:

```text
knowledge/
├── windows/
├── linux/
├── apache/
├── nginx/
├── firewall/
└── cloud/
```

Regardless of the platform, every knowledge entry should follow the same specification defined in this document.

---

# 🔗 Related Documentation

For additional information, see:

* `architecture.md` — How the application loads and uses the knowledge base.
* `design-principles.md` — Educational philosophy and project principles.
* `event-writing-guide.md` — Standards for writing educational explanations.
* `development-setup.md` — Setting up a local development environment.

---

> *"A consistent knowledge base makes educational content easier to write, easier to review, and easier to trust."*
