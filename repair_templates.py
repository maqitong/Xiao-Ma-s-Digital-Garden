import os
import glob

templates_dir = 'templates'
files_map = {
    'blog.html': 'blog_files',
    'gallery.html': 'gallery_files',
    'home.html': 'home_files',
    'projects.html': 'projects_files',
    'resume.html': 'resume_files',
    'videos.html': 'videos_files'
}

for html_file in glob.glob(os.path.join(templates_dir, '*.html')):
    basename = os.path.basename(html_file)
    folder = files_map.get(basename)
    
    if not folder:
        continue
        
    print(f"Repairing {basename}...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Construct the missing tags + </head>
    missing_tags = (
        f'<link href="{{{{ url_for(\'static\', path=\'{folder}/css2(1).css\') }}}}" rel="stylesheet"/>'
        f'<script async="" src="{{{{ url_for(\'static\', path=\'{folder}/array.full.min.js\') }}}}"></script>'
        '</head>'
    )
    
    if '</head>' not in content:
        if '<body>' in content:
            content = content.replace('<body>', f'{missing_tags}\n<body>')
            print("  Restored tags and </head> before <body>.")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print("  Error: <body> not found either!")
    else:
        print("  </head> exists. Checking for missing scripts...")
        # (Optional: logic to check if scripts are missing even if head exists)
