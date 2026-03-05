# ClaudeHelper

A helper for improving Claude Code productivity, including hooks, skills, subagents, and more.

## Directory Structure

```
ClaudeHelper/
├── hooks/
│   ├── save_response.py          # Response saving hook
│   └── completion_notification.py # Completion notification hook
├── skills/
│   └── skill-generator/          # Skill generator
│       ├── SKILL.md
│       └── hooks-reference.md
└── subagents/
    └── gitignore-guardian.md     # .gitignore review subagent
```

## Features

### Claude Response Export
**File**: `hooks/save_response.py` (Hook)

**Pain point**: When Claude's response is too long, it's hard to find and scroll to the beginning of the response in the terminal.
https://github.com/anthropics/claude-code/issues/6206

**Solution**: This hook exports the last round of user question and Claude response to `claude_output.md` on the desktop after each conversation turn, making it easy to review.

Supported content:
- Plain text responses
- `Write` tool calls (displays file path and written content)
- `Edit` tool calls (displays file path and diff)
- Other tool calls (displays tool name)

Responses shorter than 100 characters are not written to file.

**Configuration**: Edit `config.json` to set your output file path and threshold:
```json
{
  "output_file": "~/Desktop/claude_output.md",
  "threshold": 100
}
```

**Usage**: Add a hook in Claude Code settings, set the trigger to `Stop`, and set the command to:

```
python hooks/save_response.py
```

### Claude Completion Notification
**File**: `hooks/completion_notification.py` (Hook)

**Pain point**: When Claude finishes a task, there's no notification, making it hard to know when to check back.

**Solution**: This hook plays a system sound when Claude completes a response, alerting you that the task is done.

**Usage**: Add a hook in Claude Code settings, set the trigger to `Stop`, and set the command to:

```
python hooks/completion_notification.py
```

### .gitignore Guardian
**File**: `subagents/gitignore-guardian.md` (Subagent)

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

### Skill Generator
**File**: `skills/skill-generator/SKILL.md` (Skill)

**Pain point**: Creating new Claude Code skills requires understanding the skill format, frontmatter fields, best practices, and file structure.

**Solution**: A skill that guides you through creating well-structured skills with proper YAML frontmatter, clear instructions, and progressive disclosure of detailed content.

Features:
- Interactive workflow to gather requirements
- Automatic frontmatter configuration (allowed-tools, context, agent, etc.)
- Progressive disclosure: moves verbose content to reference files
- Hooks configuration support
- Best practices enforcement

**Usage**: Invoke when you want to create a new skill:

```
/skill-generator
```

Or just ask Claude to create a skill, and it will auto-invoke this skill.
