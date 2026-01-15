
from bs4 import BeautifulSoup

def inspect_projects():
    with open('templates/projects.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Look for a grid container. 
    # Usually class contains "grid".
    grids = soup.find_all(class_=lambda x: x and 'grid' in x)
    print(f"Found {len(grids)} grids in projects.html")
    
    for i, grid in enumerate(grids):
        print(f"--- Grid {i} ---")
        # Print first child
        children = [c for c in grid.children if c.name]
        if children:
            print(children[0].prettify()[:500])
        else:
            print("No children")

def inspect_blog_form():
    with open('templates/blog.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    form = soup.find('form')
    if form:
        print("\n--- Blog Form ---")
        print(form.prettify()[:1000])
    else:
        print("\nNo form found in blog.html")

if __name__ == '__main__':
    inspect_projects()
    inspect_blog_form()
