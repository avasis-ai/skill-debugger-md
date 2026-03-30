# Skill-Debugger.md (#67)

## Tagline
Step-through debugging for AI agent thought processes.

## What It Does
Bringing traditional software debugging to agents, developers can set breakpoints inside a SKILL.md. When the agent hits that step, execution pauses, allowing the human to inspect the agent's memory, prompt context, and planned actions.

## Inspired By
VS Code Debugger, Continue.dev, Cursor + IDE integrations

## Viral Potential
Debugging agents is currently a massive, frustrating black box. Provides a familiar, highly ergonomic developer experience. Instant adoption by anyone building complex, multi-step agents.

## Unique Defensible Moat
Deep IDE integration (VS Code / JetBrains) requires complex Debug Adapter Protocol (DAP) manipulation specifically mapped to non-deterministic LLM generation states, a highly complex engineering task.

## Repo Starter Structure
/dap-server, /extension, MIT License, VS Code extension

## Metadata
- **License**: MIT
- **Org**: avasis-ai
- **PyPI**: skill-debugger-md
- **Dependencies**: pyyaml>=6.0, click>=8.0
