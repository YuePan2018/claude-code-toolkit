# CLAUDE.md

这是 ClaudeHelper 项目，用于提升 Claude Code 工作效率。

## 项目结构

- `hooks/` — Hook 脚本，在 Claude Code 特定事件时触发
  - `save_response.py` — 将每轮对话的最后一次问答保存到桌面 `claude_output.md`
- `skills/` — 自定义技能（预留）
- `subagents/` — 子 Agent 配置（预留）

## 关键实现细节

- `save_response.py` 从 stdin 接收 JSON，包含 `transcript_path` 字段指向 JSONL 会话记录
- JSONL 中每行的 `type` 字段区分 `user` / `assistant`，消息体在 `message.content` 中
- 支持格式化 `Write`、`Edit` 等工具调用的输出
- 输出阈值为 100 字符，低于此不写文件
- 输出路径硬编码为 `C:\Users\Ua Pan\Desktop\claude_output.md`
