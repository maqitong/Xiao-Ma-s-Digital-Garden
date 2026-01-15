
import os
import re
from bs4 import BeautifulSoup

TEMPLATE_DIR = 'templates'
STATIC_DIR = 'static'

# Mapping of Readdy URL suffixes to local routes
ROUTE_MAP = {
    '5503083': '/',
    'about': '/resume',
    'travel': '/projects',
    'gallery': '/gallery',
    'videos': '/videos',
    'crafts': '/videos',
    'journal': '/blog'
}

def fix_html_file(filename):
    filepath = os.path.join(TEMPLATE_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # 1. Remove Immersive Translate Junk
    # Remove style tag
    style_imt = soup.find('style', attrs={'data-id': 'immersive-translate-input-injected-css'})
    if style_imt:
        style_imt.decompose()
        
    # Remove popup div
    popup = soup.find('div', id='immersive-translate-popup')
    if popup:
        popup.decompose()
        
    # Remove popup overlay
    popup_overlay = soup.find('div', id='immersive-translate-popup-overlay')
    if popup_overlay:
        popup_overlay.decompose()
        
    # Remove manga button
    manga = soup.find('div', id='manga-button')
    if manga:
        manga.decompose()
        
    # Remove float ball container
    fb = soup.find('div', class_='imt-fb-container')
    if fb:
        fb.decompose()
        
    # Remove any other elements with class starting with imt-
    for tag in soup.find_all(True, class_=lambda x: x and 'imt-' in x):
        tag.decompose()
        
    # Remove the stubborn junk div
    # <div class="" style="position: relative; pointer-events: all; display: inline-block;">
    for div in soup.find_all('div', style=lambda s: s and 'pointer-events: all' in s and 'position: relative' in s):
        div.decompose()
        
    # Also remove any div that is a direct child of html (if any) or after body
    if soup.body:
        for sibling in soup.body.next_siblings:
            if sibling.name == 'div':
                sibling.decompose()

    # 2. Remove Readdy Scripts and Meta
    script_copy = soup.find('script', id='allow-copy_script')
    if script_copy:
        script_copy.decompose()
    
    meta_readdy = soup.find('meta', attrs={'name': 'readdy-project-version'})
    if meta_readdy:
        meta_readdy.decompose()

    for script in soup.find_all('script'):
        if script.get('src') and 'readdy.ai' in script.get('src'):
            script.decompose()
            
    # 3. Fix Static Paths
    def replace_static(tag, attr):
        val = tag.get(attr)
        if val and val.startswith('./') and '_files/' in val:
            path = val[2:] # remove ./
            # Check if already replaced
            if 'url_for' not in val:
                new_val = f"{{{{ url_for('static', path='{path}') }}}}"
                tag[attr] = new_val

    for tag in soup.find_all(['link', 'script', 'img', 'source']):
        if tag.name == 'link': replace_static(tag, 'href')
        if tag.name == 'script': replace_static(tag, 'src')
        if tag.name == 'img': replace_static(tag, 'src')
        if tag.name == 'source': replace_static(tag, 'src')

    # 4. Fix Navigation Links
    for a in soup.find_all('a'):
        href = a.get('href')
        
        # 4a. Fix based on Text Content (Primary Method for Nav Bar)
        text = a.get_text().strip().lower()
        target = None
        if text == 'home': target = 'home'
        elif text == 'resume': target = 'resume'
        elif text == 'projects': target = 'projects'
        elif text == 'gallery': target = 'gallery'
        elif text == 'videos': target = 'videos'
        elif text == 'blog': target = 'blog'
        
        if target:
            a['href'] = f"{{{{ url_for('{target}') }}}}"
            continue

        # 4b. Fix based on URL matching (Fallback for logos, buttons, etc.)
        if href and ('readdy.link' in href or '5503083' in href):
            # Check which route it matches
            found = False
            for suffix, route in ROUTE_MAP.items():
                if href.endswith('/' + suffix) or href.endswith('/' + suffix + '/') or (suffix == '5503083' and href.endswith('5503083')):
                    a['href'] = f"{{{{ url_for('{route.strip('/') or 'home'}') }}}}"
                    found = True
                    break
            
            if not found and '5503083' in href:
                 # Default to home if it contains the ID but no specific suffix
                 a['href'] = "{{ url_for('home') }}"

    # 5. Remove "Made with Readdy" Badge
    for element in soup.find_all(string=re.compile("Readdy", re.IGNORECASE)):
        parent = element.parent
        if parent and parent.name == 'a':
             # If external link to readdy
             if parent.get('href') and 'readdy' in parent.get('href'):
                 if not parent['href'].startswith('{{'):
                     parent.decompose()
    
    # 6. Output
    final_html = str(soup)
    
    # Fix potential Jinja escaping by BS4
    final_html = final_html.replace('%7B%7B', '{{').replace('%7D%7D', '}}')
    final_html = final_html.replace('&lt;', '<').replace('&gt;', '>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Fixed {filename}")

if __name__ == '__main__':
    files = os.listdir(TEMPLATE_DIR)
    for f in files:
        if f.endswith('.html'):
            try:
                fix_html_file(f)
            except Exception as e:
                print(f"Error processing {f}: {e}")
