# CLAUDE.md

This is the ClaudeHelper project, designed to improve Claude Code productivity.

## Project Structure

- `hooks/` — Hook scripts triggered on specific Claude Code events
  - `save_response.py` — Saves the last Q&A of each conversation turn to `claude_output.md` on the desktop
  - `completion_notification.py` — Plays a system sound when Claude completes a task
- `skills/` — Custom skills (reserved)
- `subagents/` — Subagent configs (reserved)

## Key Implementation Details

- `save_response.py` receives JSON from stdin containing a `transcript_path` field pointing to a JSONL session log
- Each line in the JSONL has a `type` field (`user` / `assistant`), with the message body in `message.content`
- Supports formatted output for `Write`, `Edit`, and other tool calls
- Output threshold is 100 characters; files are not written below this limit
- Output path is hardcoded to `C:\Users\Ua Pan\Desktop\claude_output.md`
