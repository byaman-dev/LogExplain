# 🛠 Development Setup

> A step-by-step guide for setting up a local development environment for LogExplain.

![Project](https://img.shields.io/badge/Project-LogExplain-blue?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Development-success?style=for-the-badge)
![Document](https://img.shields.io/badge/Document-Setup%20Guide-purple?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-0.1-lightgrey?style=for-the-badge)

---

# 📖 Purpose

This guide explains how to set up LogExplain for local development.

By the end of this guide, you should be able to:

* Clone the repository.
* Create a Python virtual environment.
* Install project dependencies.
* Run the command-line application.
* Execute the test suite.

---

# ✅ Prerequisites

Before getting started, make sure you have the following installed:

* 🐍 Python 3.11 or later
* 🌱 Git
* 💻 A terminal (PowerShell, Command Prompt, Bash, or Zsh)
* 📝 A code editor (VS Code is recommended)

---

# 📥 Clone the Repository

Clone the repository and move into the project directory.

```bash
git clone https://github.com/byaman-dev/LogExplain.git
cd LogExplain
```

---

# 🐍 Create a Virtual Environment

Create an isolated Python environment for the project.

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, your terminal should display the virtual environment name.

---

# 📦 Install Dependencies

Install the project in editable mode.

```bash
pip install -e .
```

This allows changes to the source code to be reflected immediately without reinstalling the project.

---

# ▶️ Run LogExplain

Once the project is installed, start the command-line application.

```bash
logexplain --help
```

You should see the available commands and options.

---

# 🧪 Run the Test Suite

Run all automated tests.

```bash
pytest
```

Tests should pass before opening a pull request.

---

# 📁 Project Structure

The repository is organised into a small number of top-level directories.

```text
LogExplain/
├── docs/
├── knowledge/
├── logexplain/
├── tests/
└── pyproject.toml
```

Each directory has a specific responsibility. See **`architecture.md`** for a detailed overview.

---

# 🔄 Keeping Your Fork Updated

If you're contributing regularly, keep your local repository up to date before starting new work.

```bash
git pull
```

Resolve any merge conflicts before making additional changes.

---

# 🛠 Troubleshooting

### Python command not found

Ensure Python is installed and available in your system's PATH.

---

### Virtual environment not activated

Activate the virtual environment before installing dependencies or running commands.

---

### Command not recognised

If `logexplain` is unavailable after installation, confirm that the installation completed successfully.

Reinstall if necessary:

```bash
pip install -e .
```

---

### Tests are failing

Make sure:

* The virtual environment is active.
* Dependencies are installed.
* You're using a supported Python version.

If the issue persists, open a GitHub issue with the full error message.

---

# 🤝 Contributing

Before opening a pull request:

* Read `CONTRIBUTING.md`.
* Follow `event-writing-guide.md` when adding educational content.
* Keep documentation consistent with existing project standards.
* Ensure all tests pass.

Small, focused contributions are easier to review and merge.

---

# 🔗 Related Documentation

For additional information, see:

* `architecture.md` — Project architecture and component overview.
* `knowledge-base-specification.md` — Structure of the knowledge base.
* `event-writing-guide.md` — Standards for writing educational explanations.
* `CONTRIBUTING.md` — Contribution workflow and expectations.

---

> *"A consistent development environment makes contributing easier for everyone."*
