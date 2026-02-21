import sys, json

THRESHOLD = 400  # 字符数，超过才写文件
OUT_FILE = r"C:\Users\Ua Pan\Desktop\claude_output.md"

data = json.loads(sys.stdin.read())
transcript_path = data.get("transcript_path", "")

if not transcript_path:
    print("{}")
    sys.exit(0)

last_user = ""
last_assistant = ""

try:
    with open(transcript_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if obj.get("isMeta"):
                continue
            role = obj.get("type", "")
            content = obj.get("message", {}).get("content", [])
            if isinstance(content, list):
                text = "".join(
                    b.get("text", "") for b in content
                    if isinstance(b, dict) and b.get("type") == "text"
                )
            elif isinstance(content, str):
                text = content
            else:
                text = ""
            if role == "user" and text:
                last_user = text
            elif role == "assistant" and text:
                last_assistant = text
except Exception:
    pass

if len(last_assistant) >= THRESHOLD:
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        if last_user:
            f.write(f"## 问题\n{last_user}\n\n")
        f.write(f"## 回答\n{last_assistant}\n")

print("{}")
