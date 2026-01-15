import os
import glob
import re

# Configuration
STATIC_DIR = 'static'
TEMPLATES_DIR = 'templates'

def rename_download_files():
    print("--- 1. Renaming .下载 files ---")
    count = 0
    for root, dirs, files in os.walk(STATIC_DIR):
        for file in files:
            if file.endswith('.下载'):
                old_path = os.path.join(root, file)
                new_name = file.replace('.下载', '')
                new_path = os.path.join(root, new_name)
                
                # If target exists, remove it first (overwrite)
                if os.path.exists(new_path):
                    os.remove(new_path)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {file} -> {new_name}")
                count += 1
    print(f"Total renamed: {count}")

def sanitize_js_files():
    print("\n--- 2. Sanitizing JS files ---")
    # Targets to neutralize
    replacements = [
        ('https://public.readdy.ai/gen_page/readdy-logo.png', ''),
        ('https://public.readdy.ai/gen_page/watermark.png', ''),
        ('https://readdy.ai?ref=b', '#'),
        ('readdy.ai', 'localhost'), # Catch-all for other domains
        # Remove reference to .下载 files in imports if any
        ('.下载', '') 
    ]
    
    for root, dirs, files in os.walk(STATIC_DIR):
        for file in files:
            if file.endswith('.js'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_len = len(content)
                for old, new in replacements:
                    content = content.replace(old, new)
                
                # Try to break the watermark ID if found
                # Look for id:"watermark" or id="watermark"
                content = content.replace('id:"watermark"', 'id:"wm-removed",style:{display:"none"}')
                content = content.replace('id="watermark"', 'id="wm-removed" style="display:none"')
                
                if len(content) != original_len:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Sanitized: {file}")

def inject_css_killer():
    print("\n--- 3. Injecting CSS Killer ---")
    css_killer_rule = """
    /* FORCE REMOVE READDY WATERMARK */
    #watermark, #readdy-badge, [id*="readdy"], [class*="readdy"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
        width: 0 !important;
        height: 0 !important;
        position: fixed !important;
        top: -9999px !important;
        left: -9999px !important;
        z-index: -9999 !important;
    }
    """
    for root, dirs, files in os.walk(STATIC_DIR):
        for file in files:
            if file.endswith('.css'):
                path = os.path.join(root, file)
                with open(path, 'a', encoding='utf-8') as f:
                    f.write(css_killer_rule)
                print(f"Injected CSS killer into: {file}")

def inject_html_killer():
    print("\n--- 4. Injecting HTML/JS Killer ---")
    script_killer = """
    <script>
    (function() {
        // Immediate removal
        function kill() {
            var wm = document.getElementById('watermark');
            if (wm) wm.remove();
            
            // Also kill by text content if ID changes
            var divs = document.querySelectorAll('div');
            divs.forEach(function(div) {
                if (div.innerText && (div.innerText.includes('本网站来自') || div.innerText.includes('Made with Readdy'))) {
                    div.remove();
                }
            });
        }
        kill();
        
        // Persistent removal
        var observer = new MutationObserver(function(mutations) {
            kill();
        });
        observer.observe(document.body, { childList: true, subtree: true });
        
        // Periodic check just in case
        setInterval(kill, 1000);
    })();
    </script>
    """
    
    for file in glob.glob(os.path.join(TEMPLATES_DIR, '*.html')):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'function kill()' not in content:
            if '</body>' in content:
                content = content.replace('</body>', script_killer + '\n</body>')
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Injected JS killer into: {file}")

if __name__ == '__main__':
    rename_download_files()
    sanitize_js_files()
    inject_css_killer()
    inject_html_killer()
    print("\nDeep clean completed.")
