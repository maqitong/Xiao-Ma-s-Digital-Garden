
import os
from html.parser import HTMLParser
import re

def extract_content(file_path, tag_name, attrs=None):
    print(f"--- Analyzing {os.path.basename(file_path)} ---")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove Immersive Translate junk if possible (it's usually at the end)
        if '<div id="immersive-translate-popup"' in content:
            content = content.split('<div id="immersive-translate-popup"')[0]
            
        # Simple regex to find form
        if tag_name == 'form':
            forms = re.findall(r'(<form.*?>.*?</form>)', content, re.DOTALL | re.IGNORECASE)
            if forms:
                print(f"Found {len(forms)} forms.")
                for i, form in enumerate(forms):
                    print(f"Form {i+1}:")
                    # Print first 500 chars of form to identify
                    print(form[:500] + "...")
                    # Extract inputs
                    inputs = re.findall(r'<input[^>]*name=["\']([^"\']+)["\'][^>]*>', form)
                    textareas = re.findall(r'<textarea[^>]*name=["\']([^"\']+)["\'][^>]*>', form)
                    print("  Inputs:", inputs)
                    print("  Textareas:", textareas)
            else:
                print("No forms found.")

        # Regex to find Project cards (heuristic: look for "Projects" section and then repeated structures)
        # This is hard with regex. Let's just dump the body structure roughly.
        
        # Check for Project keywords
        if "Project" in content:
            print("Found 'Project' keyword.")
            
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def analyze_projects(file_path):
    print(f"--- Analyzing Projects in {os.path.basename(file_path)} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to find the container for projects. 
    # Usually readdy uses grid or flex.
    # Look for the card structure.
    # We'll look for multiple occurrences of similar blocks.
    # Let's try to find text inside project cards if we knew any.
    # The prompt says "Project: title, description, image_url, link, tags, category".
    # I'll look for common tags like "Travel", "Photography" which might be in the static data.
    
    # Just print the first few matches of class="...card..." or similar if possible.
    # Or just look for <a> tags with hrefs that might be projects.
    links = re.findall(r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>', content)
    project_links = [l for l in links if '/preview/' in l and 'travel' in l or 'project' in l.lower()]
    print(f"Potential Project Links: {project_links[:5]}")

extract_content('blog.html', 'form')
extract_content('home.html', 'form')
analyze_projects('projects.html')
