
import os
import re

TEMPLATE_DIR = 'templates'
STATIC_DIR = 'static'

def rename_css():
    for root, dirs, files in os.walk(STATIC_DIR):
        for f in files:
            if f.startswith('css2') and not f.endswith('.css'):
                old_path = os.path.join(root, f)
                new_name = f + '.css'
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed {f} to {new_name}")

def update_references():
    # Targets: all html files in templates/ and seed.py
    targets = [os.path.join(TEMPLATE_DIR, f) for f in os.listdir(TEMPLATE_DIR) if f.endswith('.html')]
    targets.append('seed.py')
    
    for filepath in targets:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace image references
        # Pattern: search-image(\(\d+\))? -> \g<0>.jpg
        # But we need to be careful not to double extension if run multiple times.
        # So we look for search-image(\(\d+\))?(?!\.jpg)
        
        # Replace images
        content = re.sub(r'(search-image(?:\(\d+\))?)(?!\.jpg)', r'\1.jpg', content)
        
        # Replace css
        content = re.sub(r'(css2(?:\(\d+\))?)(?!\.css)', r'\1.css', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated references in {filepath}")

if __name__ == '__main__':
    rename_css()
    update_references()
