# ClaudeHelper

用于提升 Claude Code 工作效率的 helper，包含 hook、skill、subagent 等。

## 目录结构

```
ClaudeHelper/
├── hooks/
│   └── save_response.py   # 回答保存 Hook
├── skills/                # 自定义技能（预留）
└── subagents/             # 子 Agent 配置（预留）
```

## 功能

### save_response.py

**痛点**：当 Claude 的回答太长时，在命令行里不容易找到回答的开头并跳转。

**方案**：这个 hook 会在每轮对话结束后，把最后一轮的用户问题和 Claude 回答输出到桌面的 `claude_output.md`，方便查看。

支持的内容：
- 普通文本回答
- `Write` 工具调用（显示文件路径和写入内容）
- `Edit` 工具调用（显示文件路径和 diff）
- 其他工具调用（显示工具名称）

回答长度低于 100 字符时不写文件。

**使用方式**：在 Claude Code 设置中添加 hook，触发时机选择 `Stop`，命令设置为：

```
python.exe hooks/save_response.py
```
