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
├── subagents/
│   └── gitignore-guardian.md     # .gitignore review subagent
└── registry/
    ├── add-claude-to-context-menu.reg      # Add Claude CLI to right-click menu
    └── restore-classic-context-menu.reg    # Restore Windows 10 style context menu
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

### Windows Registry Tweaks
**Files**: `registry/*.reg`, `registry/Start-Codex-Proxy.ps1`, `registry/Start Codex Proxy.lnk`

**Pain point**: Windows 11's new context menu requires extra clicks to access useful tools, and adding Claude CLI to the context menu requires manual registry editing.

**Solution**: Registry scripts and a Codex proxy launcher to improve your Windows experience:

1. **Add Claude CLI to Context Menu** (`add-claude-to-context-menu.reg`)
   - Adds "Open Claude CLI" option when right-clicking on folder backgrounds
   - Opens PowerShell in the current directory and launches Claude CLI
   - Works with Windows 11 new context menu

2. **Restore Classic Context Menu** (`restore-classic-context-menu.reg`)
   - Disables Windows 11's new context menu
   - Restores the classic Windows 10 style context menu
   - Shows all options directly without "Show more options"

3. **Start Codex With Proxy** (`Start-Codex-Proxy.ps1`, `Start Codex Proxy.lnk`)
   - Starts Codex with `HTTP_PROXY`, `HTTPS_PROXY`, and `ALL_PROXY` set to `http://127.0.0.1:10808`
   - Keep the PowerShell script in `registry` and copy the shortcut to the desktop or another convenient location
   - The shortcut points back to the script in `registry`, so moving only the shortcut is enough

**Usage**: Double-click the `.reg` file and confirm to apply the changes. Restart Explorer or log out/in for changes to take effect.

**Note**: These scripts modify the Windows Registry. Always backup your registry before applying changes.
