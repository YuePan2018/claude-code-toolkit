import sys, json, winsound

# 读取 hook 输入
try:
    data = json.loads(sys.stdin.read())
except:
    pass

# 播放 Windows 完成音（较长的提示音）
winsound.PlaySound(r"C:\Windows\Media\tada.wav", winsound.SND_FILENAME)

# 返回空 JSON（hook 要求）
print("{}")
