import os
import glob

static_dir = os.path.join('static', 'home_files')
templates_dir = 'templates'

# 1. Replace remixicon.min.css
remix_css = os.path.join(static_dir, 'remixicon.css')
remix_min = os.path.join(static_dir, 'remixicon.min.css')
if os.path.exists(remix_css):
    print(f"Replacing {remix_min} with {remix_css}")
    if os.path.exists(remix_min):
        os.remove(remix_min)
    os.rename(remix_css, remix_min)

# 2. Fix .下载 files
for filename in os.listdir(static_dir):
    if filename.endswith('.下载'):
        new_name = filename.replace('.下载', '')
        old_path = os.path.join(static_dir, filename)
        new_path = os.path.join(static_dir, new_name)
        print(f"Renaming {filename} -> {new_name}")
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)

# 3. Update templates
for html_file in glob.glob(os.path.join(templates_dir, '*.html')):
    print(f"Processing {html_file}...")
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    new_content = []
    for line in content:
        # Remove Readdy links
        if 'readdy.ai' in line:
            print(f"  Removing readdy line: {line.strip()}")
            continue
        
        # Fix .下载 references
        if '.下载' in line:
            print(f"  Fixing .下载 ref in: {line.strip()}")
            line = line.replace('.下载', '')
            
        new_content.append(line)
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.writelines(new_content)

print("Cleanup done.")
