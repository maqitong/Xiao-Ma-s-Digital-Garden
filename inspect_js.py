import os

file_path = r"static/home_files/index-DzpddGlb.js"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

index = content.find("watermark")
if index != -1:
    start = max(0, index - 100)
    end = min(len(content), index + 100)
    print(f"Match 1 context:\n{content[start:end]}")

index2 = content.find("readdy.ai")
if index2 != -1:
    start = max(0, index2 - 100)
    end = min(len(content), index2 + 100)
    print(f"Match 2 context:\n{content[start:end]}")
