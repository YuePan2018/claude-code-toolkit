# ClaudeHelper

A helper for improving Claude Code productivity, including hooks, skills, subagents, and more.

## Directory Structure

```
ClaudeHelper/
├── hooks/
│   └── save_response.py   # Response saving hook
├── skills/                # Custom skills (reserved)
└── subagents/
    └── gitignore-guardian.md  # .gitignore review subagent
```

## Features

### save_response.py

**Pain point**: When Claude's response is too long, it's hard to find and scroll to the beginning of the response in the terminal.
https://github.com/anthropics/claude-code/issues/6206

**Solution**: This hook exports the last round of user question and Claude response to `claude_output.md` on the desktop after each conversation turn, making it easy to review.

Supported content:
- Plain text responses
- `Write` tool calls (displays file path and written content)
- `Edit` tool calls (displays file path and diff)
- Other tool calls (displays tool name)

Responses shorter than 100 characters are not written to file.

**Usage**: Add a hook in Claude Code settings, set the trigger to `Stop`, and set the command to:

```
python hooks/save_response.py
```

### completion_notification.py

**Pain point**: When Claude finishes a task, there's no notification, making it hard to know when to check back.

**Solution**: This hook plays a system sound when Claude completes a response, alerting you that the task is done.

**Usage**: Add a hook in Claude Code settings, set the trigger to `Stop`, and set the command to:

```
python hooks/completion_notification.py
```

### gitignore-guardian

**Pain point**: It's easy to accidentally commit IDE configs, log files, secrets, and other files that don't belong in the repo.

**Solution**: A dedicated .gitignore subagent that scans the actual project file structure and fills in missing .gitignore rules. It only adds patterns for files that actually exist — no speculative entries.

Coverage:
- Claude config (.claude/)
- IDE configs (.vscode/, .idea/)
- Sensitive files (.env, credentials)
- Build output (dist/, build/)
- Dependencies (node_modules/, .venv/)
- Logs, caches, temp files
- Compiled code (*.pyc, __pycache__/)
- OS files (.DS_Store, Thumbs.db)

**Usage**: Ask Claude Code to check gitignore in the conversation, e.g.:

```
check gitignore
```
