import sys, json, time

THRESHOLD = 100  # 字符数，超过才写文件
OUT_FILE = r"C:\Users\Ua Pan\Desktop\claude_output.md"

data = json.loads(sys.stdin.read())
transcript_path = data.get("transcript_path", "")

if not transcript_path:
    print("{}")
    sys.exit(0)


def format_tool_use(block):
    name = block.get("name", "")
    inp = block.get("input", {})
    if name == "Write":
        fp = inp.get("file_path", "")
        content = inp.get("content", "")
        return f"\n**Write** `{fp}`\n```\n{content}\n```"
    elif name == "Edit":
        fp = inp.get("file_path", "")
        old = inp.get("old_string", "")
        new = inp.get("new_string", "")
        diff = "\n".join(
            [f"- {l}" for l in old.splitlines()] +
            [f"+ {l}" for l in new.splitlines()]
        )
        return f"\n**Edit** `{fp}`\n```diff\n{diff}\n```"
    return f"{name}..."


last_user = ""
assistant_chunks = []  # 当前 user 之后的所有 assistant 内容

time.sleep(0.5)  # 等待 JSONL 完全写入磁盘

try:
    with open(transcript_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue  # 跳过写入不完整的行
            if obj.get("isMeta"):
                continue
            role = obj.get("type", "")
            content = obj.get("message", {}).get("content", [])

            if role == "user":
                if isinstance(content, list):
                    text = "".join(
                        b.get("text", "") for b in content
                        if isinstance(b, dict) and b.get("type") == "text"
                    )
                elif isinstance(content, str):
                    text = content
                else:
                    text = ""
                if text:
                    last_user = text
                    assistant_chunks = []  # 新一轮对话，重置

            elif role == "assistant":
                if isinstance(content, list):
                    for block in content:
                        if not isinstance(block, dict):
                            continue
                        btype = block.get("type", "")
                        if btype == "text":
                            t = block.get("text", "")
                            if t:
                                assistant_chunks.append(t)
                        elif btype == "tool_use":
                            formatted = format_tool_use(block)
                            if formatted:
                                assistant_chunks.append(formatted)
except Exception:
    pass

last_assistant = "\n\n".join(assistant_chunks).strip()

if len(last_assistant) >= THRESHOLD:
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        if last_user:
            f.write(f"## 问题\n{last_user}\n\n")
        f.write(f"## 回答\n{last_assistant}\n")

print("{}")
