# 🏗 Architecture

> An overview of how LogExplain is organised and how its components work together to transform security events into educational explanations.

![Project](https://img.shields.io/badge/Project-LogExplain-blue?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Architecture-success?style=for-the-badge)
![Document](https://img.shields.io/badge/Document-System%20Design-purple?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-0.1-lightgrey?style=for-the-badge)

---

# 📖 Purpose

This document explains the technical architecture of LogExplain.

Its goal is to help contributors understand how the project is organised, how information flows through the application, and where different responsibilities belong.

This document focuses on **how** the project is built.

For the project's philosophy and design decisions, see **`design-principles.md`**.

---

# 🎯 Architecture Overview

LogExplain follows a simple layered architecture.

Educational content, application logic, and user interfaces are intentionally separated so that each part of the project has a single responsibility.

```mermaid
flowchart LR

subgraph Interface
CLI["Typer CLI"]
end

subgraph Core
Registry["Registry"]
Loader["Markdown Loader"]
Validator["Pydantic Validator"]
Renderer["Rich Renderer"]
end

subgraph Knowledge
KB["Markdown Knowledge Base"]
end

CLI --> Registry
Registry --> Loader
Loader --> KB
Loader --> Validator
Validator --> Renderer
Renderer --> CLI
```

This design keeps the project modular while ensuring that educational content remains independent from the application itself.

---

# 🔄 Request Flow

Whenever a user requests an explanation, LogExplain follows the same predictable workflow.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant Registry
    participant Loader
    participant Validator
    participant Renderer

    User->>CLI: explain windows 4625
    CLI->>Registry: Find requested event
    Registry->>Loader: Load Markdown file
    Loader->>Validator: Validate content
    Validator->>Renderer: Format explanation
    Renderer-->>User: Display result
```

Following the same workflow for every request keeps the application's behaviour consistent and predictable.

---

# 📦 Core Components

## 💻 Typer CLI

The command-line interface is the primary entry point in Version 0.1.

It receives user commands and passes requests to the application's internal components.

---

## 📚 Registry

The Registry acts as the application's coordinator.

It identifies the requested event and connects the command-line interface with the knowledge loading process.

---

## 📄 Markdown Loader

The Markdown Loader reads security event files from the knowledge base.

It extracts structured content and prepares it for validation.

---

## ✅ Pydantic Validator

The validation layer ensures that every knowledge base entry follows the expected schema before it is presented to users.

---

## 🎨 Rich Renderer

The renderer transforms validated data into a clear, readable terminal experience.

Presentation is handled here rather than inside the knowledge base.

---

## 📚 Knowledge Base

The knowledge base contains all educational content.

Each security event exists as an individual Markdown document, making the knowledge base the project's single source of truth.

---

# 📂 Repository Organization

Each top-level directory has a clearly defined responsibility.

```mermaid
mindmap
  root((LogExplain))
    docs
    knowledge
      windows
    logexplain
    tests
    .github
```

| Directory     | Responsibility                                |
| ------------- | --------------------------------------------- |
| `docs/`       | Project documentation and contributor guides. |
| `knowledge/`  | Educational security event explanations.      |
| `logexplain/` | Python application source code.               |
| `tests/`      | Automated tests.                              |
| `.github/`    | GitHub workflows and community configuration. |

Keeping responsibilities separate makes the repository easier to understand, maintain, and contribute to.

---

# 🔮 Extensible Interfaces

Although Version **0.1** focuses on a command-line application, the architecture is designed so that additional interfaces can reuse the same knowledge base.

```mermaid
flowchart LR

KB["Knowledge Base"]

CLI["CLI"]
WEB["Website"]
API["REST API"]
DESKTOP["Desktop App"]
VSCODE["VS Code Extension"]
MOBILE["Mobile App"]

KB --> CLI
KB -. Future .-> WEB
KB -. Future .-> API
KB -. Future .-> DESKTOP
KB -. Future .-> VSCODE
KB -. Future .-> MOBILE
```

Because every interface reads from the same knowledge base, educational content only needs to be written once.

New interfaces can be introduced without duplicating explanations or changing the knowledge structure.

---

# 🔗 Related Documentation

Continue exploring the project through these documents:

* `design-principles.md` — Project philosophy and guiding principles.
* `knowledge-base-specification.md` — Structure of the Markdown knowledge base.
* `event-writing-guide.md` — Standards for writing educational content.
* `development-setup.md` — Setting up a local development environment.
* `roadmap.md` — Project milestones and future direction.

---

> *"A simple architecture is easier to understand, easier to maintain, and easier to grow."*
