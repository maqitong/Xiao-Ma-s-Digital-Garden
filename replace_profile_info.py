import re

with open('templates/resume.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Name
content = re.sub(r'>\s*小马\s*<', '>{{ profile.name }}<', content)
content = re.sub(r'>\s*Xiao Ma\s*<', '>{{ profile.name }}<', content)

# Replace Role
content = re.sub(r'>\s*全栈开发工程师\s*<', '>{{ profile.role }}<', content)

# Replace Email if found
content = re.sub(r'mailto:[\w\.-]+@[\w\.-]+', 'mailto:{{ profile.email }}', content)
content = re.sub(r'>[\w\.-]+@[\w\.-]+<', '>{{ profile.email }}<', content)

with open('templates/resume.html', 'w', encoding='utf-8') as f:
    f.write(content)
