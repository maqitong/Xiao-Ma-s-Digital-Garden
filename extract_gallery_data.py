from bs4 import BeautifulSoup
import re

# Try reading with 'utf-16' if 'utf-8' fails (PowerShell redirection might use UTF-16)
try:
    with open('original_gallery.html', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open('original_gallery.html', 'r', encoding='utf-16') as f:
        content = f.read()

soup = BeautifulSoup(content, 'html.parser')

items = []

grid = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6')
if grid:
    divs = grid.find_all('div', class_=lambda x: x and 'group relative' in x, recursive=False)
    print(f"Found {len(divs)} items.")
    
    for div in divs:
        # Image
        img = div.find('img')
        image_url = img['src'] if img else ""
        if "url_for" in image_url:
            match = re.search(r"path='([^']+)'", image_url)
            if match:
                image_url = "/static/" + match.group(1)
        
        # Title
        h3 = div.find('h3')
        title = h3.get_text().strip() if h3 else "Untitled"
        
        # Description / Location
        p = div.find('p', class_='text-cyan-400')
        desc = p.get_text().strip() if p else ""
        
        items.append({
            "title": title,
            "description": desc,
            "image_url": image_url,
            "category": "Photography"
        })

print("Extracted Items:")
# Generate Python code for seed_db.py
print("\n--- Python Code ---")
print("        items = [")
for item in items:
    print(f"            models.GalleryItem(title=\"{item['title']}\", description=\"{item['description']}\", image_url=\"{item['image_url']}\", category=\"{item['category']}\"),")
print("        ]")
