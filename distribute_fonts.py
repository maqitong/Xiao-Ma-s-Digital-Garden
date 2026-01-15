import os
import shutil

source_dir = os.path.join('static', 'home_files')
target_dirs = [
    'static/blog_files',
    'static/gallery_files',
    'static/projects_files',
    'static/resume_files',
    'static/videos_files'
]

font_files = [
    'remixicon.css', 
    'remixicon.min.css', 
    'remixicon.woff2', 
    'remixicon.woff', 
    'remixicon.ttf'
]

print("Distributing fonts...")
for target in target_dirs:
    if not os.path.exists(target):
        print(f"Target dir not found: {target}")
        continue
        
    for font in font_files:
        src = os.path.join(source_dir, font)
        dst = os.path.join(target, font)
        
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {font} to {target}")
        else:
            print(f"Warning: Source font {font} not found in {source_dir}")

print("Font distribution done.")
