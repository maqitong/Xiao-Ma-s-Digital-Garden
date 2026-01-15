from bs4 import BeautifulSoup

files = ['templates/gallery.html', 'templates/videos.html', 'templates/blog.html']

for file in files:
    print(f"\n--- Analyzing {file} ---")
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Look for grid containers
    grids = soup.find_all('div', class_=lambda x: x and ('grid' in x))
    print(f"Found {len(grids)} grid containers.")
    
    for i, grid in enumerate(grids):
        # Print first few chars of content to identify
        print(f"Grid {i} classes: {grid.get('class')}")
        # print(f"Sample content: {str(grid)[:200]}...")

    # Look for specific headers
    headers = soup.find_all(['h1', 'h2', 'h3'])
    for h in headers:
        print(f"Header: {h.get_text().strip()}")
