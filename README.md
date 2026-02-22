# ClaudeHelper

A helper for improving Claude Code productivity, including hooks, skills, subagents, and more.

## Directory Structure

```
ClaudeHelper/
├── hooks/
│   └── save_response.py   # Response saving hook
├── skills/                # Custom skills (reserved)
└── subagents/             # Subagent configs (reserved)
```

## Features

### save_response.py

**Pain point**: When Claude's response is too long, it's hard to find and scroll to the beginning of the response in the terminal.

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
