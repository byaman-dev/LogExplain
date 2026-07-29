# Contributing to LogExplain

First of all, thank you for considering contributing to LogExplain!

LogExplain is an educational open-source project that helps beginners understand security logs through reasoning rather than memorization. Every contribution, whether it's improving an explanation, fixing a typo, or adding a new event, helps make cybersecurity more accessible.

## Our Philosophy

The knowledge base is the heart of LogExplain.

The goal of every contribution is to help answer one question:

> **"If I were a beginner looking at this security event, what would an experienced SOC analyst teach me?"**

When contributing, prioritize clarity, accuracy, and educational value over technical complexity.

## Ways to Contribute

You do **not** need to be a Python developer to contribute.

We welcome contributions such as:

* Improving event explanations
* Correcting grammar or spelling
* Adding references to official documentation
* Expanding investigation guidance
* Improving the README or documentation
* Reporting bugs or suggesting improvements
* Writing or improving tests
* Improving the CLI experience

## Before You Start

Before opening a Pull Request:

* Search existing Issues to avoid duplicate work.
* Read the project documentation.
* Keep changes focused on a single topic whenever possible.
* If you plan a large change, open an Issue first to discuss it.

## Adding a New Event

Adding a new security event is one of the best ways to contribute.

1. Create a new Markdown file inside the appropriate knowledge directory.
2. Follow the existing event template.
3. Complete every required section.
4. Verify that the YAML front matter is valid.
5. Submit a Pull Request.

Every event should follow the same educational structure.

## Writing Guidelines

When writing explanations:

* Assume the reader is new to cybersecurity.
* Explain unfamiliar terms.
* Avoid unnecessary jargon.
* Stay objective and factual.
* Do not exaggerate risk.
* Encourage investigation instead of making assumptions.
* Keep explanations practical and actionable.

Remember:

**Teach reasoning, not memorization.**

## Code Style

For Python contributions:

* Follow the existing project structure.
* Keep functions small and focused.
* Prefer readability over clever solutions.
* Add tests for new functionality whenever practical.

## Commit Messages

This project follows the Conventional Commits specification.

Examples:

* `feat: add Windows Event ID 4688`
* `fix: improve markdown parser error handling`
* `docs: update installation guide`
* `test: add loader validation tests`
* `chore: update development dependencies`

## Pull Requests

A good Pull Request should:

* Have a clear title.
* Explain the purpose of the change.
* Stay focused on one topic.
* Include tests when appropriate.
* Update documentation if needed.

Please be respectful during code review. Feedback is intended to improve the project, not criticize contributors.

## Questions

If you're unsure about anything, open an Issue before starting work.

We're happy to discuss ideas and help new contributors get started.

## Thank You

Thank you for helping improve LogExplain.

Every contribution—large or small—helps beginners become better security analysts.
