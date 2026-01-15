from bs4 import BeautifulSoup

with open('templates/resume.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- Headers ---")
for i in range(1, 7):
    for tag in soup.find_all(f'h{i}'):
        print(f"<{tag.name}>{tag.get_text()}</{tag.name}>")
