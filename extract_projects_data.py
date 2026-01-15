from bs4 import BeautifulSoup
import re

# Try reading with 'utf-16' if 'utf-8' fails
try:
    with open('original_projects.html', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open('original_projects.html', 'r', encoding='utf-16') as f:
        content = f.read()

soup = BeautifulSoup(content, 'html.parser')

projects = []

# Find the main grid
# Based on inspection, it usually has classes like 'grid md:grid-cols-2 lg:grid-cols-3 gap-8'
grid = soup.find('div', class_=lambda x: x and 'grid' in x and 'gap-8' in x)

if grid:
    # Items are usually articles or divs
    items = grid.find_all(['div', 'article'], class_=lambda x: x and 'group' in x, recursive=False)
    print(f"Found {len(items)} projects.")
    
    for item in items:
        # Image
        img = item.find('img')
        image_url = img['src'] if img else ""
        if "url_for" in image_url:
            match = re.search(r"path='([^']+)'", image_url)
            if match:
                image_url = "/static/" + match.group(1)
        
        # Category/Tags
        # Usually in a span or div at top
        category_tag = item.find('span', class_=lambda x: x and 'bg-cyan-500' in x)
        category = category_tag.get_text().strip() if category_tag else "Web Development"
        
        # Title
        h3 = item.find('h3')
        title = h3.get_text().strip() if h3 else "Untitled"
        
        # Description
        p = item.find('p', class_='text-slate-400')
        description = p.get_text().strip() if p else ""
        
        # Link
        # Usually wrapping the image or a "View Project" button
        a = item.find('a', href=True)
        link = a['href'] if a else "#"
        
        # Tags (Technology stack icons/text)
        # Look for a container with icons like ri-reactjs-line
        tags = []
        tech_container = item.find('div', class_='flex gap-3')
        if tech_container:
            icons = tech_container.find_all('i')
            for icon in icons:
                # Map classes to names if possible, or just skip
                pass
            # Or text tags
            text_tags = tech_container.find_all('span')
            for tag in text_tags:
                tags.append(tag.get_text().strip())
        
        tags_str = ", ".join(tags) if tags else "React, Tailwind"

        projects.append({
            "title": title,
            "description": description,
            "image_url": image_url,
            "link": link,
            "category": category,
            "tags": tags_str
        })

print("Extracted Projects:")
print("\n--- Python Code ---")
print("        projects = [")
for p in projects:
    print(f"            models.Project(title=\"{p['title']}\", description=\"{p['description']}\", image_url=\"{p['image_url']}\", link=\"{p['link']}\", category=\"{p['category']}\", tags=\"{p['tags']}\"),")
print("        ]")
