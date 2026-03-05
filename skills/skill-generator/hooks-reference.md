# Hooks Reference

Hooks allow skills to run scripts at specific lifecycle events. They are scoped to the skill's lifetime and automatically cleaned up when the skill finishes.

## Supported Hook Events

All hook events are supported:
- `PreToolUse` — Before a tool is used
- `PostToolUse` — After a tool completes
- `Stop` — When the skill finishes (auto-converted to `SubagentStop` for subagents)
- Other events as defined in Claude Code hooks system

## Hook Configuration Format

```yaml
hooks:
  EventName:
    - matcher: "ToolName"        # Optional: filter by tool name (e.g., "Bash", "Read")
      hooks:
        - type: command           # Hook type: "command" or "prompt"
          command: "./script.sh"  # Script to execute
          args: ["arg1", "arg2"]  # Optional: script arguments
```

## Example: Security Validation

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/security-check.sh"
---
```

This runs `security-check.sh` before each Bash command execution.

## Example: Logging Tool Usage

```yaml
hooks:
  PostToolUse:
    - hooks:
        - type: command
          command: "./scripts/log-usage.sh"
```

This logs all tool usage without filtering by tool name.
