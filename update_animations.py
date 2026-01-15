import os
import glob

templates_dir = 'templates'
script_tag = '<script src="{{ url_for(\'static\', path=\'js/main.js\') }}"></script>'

# 1. Update all HTML files to include the script
for html_file in glob.glob(os.path.join(templates_dir, '*.html')):
    print(f"Processing {html_file}...")
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Inject script before </body>
    if 'js/main.js' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{script_tag}\n</body>')
            print("  Injected main.js script.")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print("  Warning: </body> not found.")
    else:
        print("  Script already present.")

# 2. Re-add animation classes to home.html (since we removed them previously)
# We look for specific sections we stripped.
home_path = os.path.join(templates_dir, 'home.html')
if os.path.exists(home_path):
    print("Restoring animation classes in home.html...")
    with open(home_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Restore stats section
    if 'stats-section" >' in content or 'stats-section">' in content: # Check if it lacks the animate classes
        # We search for the simplified tag we created
        content = content.replace(
            'class="grid grid-cols-2 md:grid-cols-4 gap-8 stats-section"',
            'class="grid grid-cols-2 md:grid-cols-4 gap-8 stats-section animate-on-scroll opacity-0 translate-y-8 transition-all duration-700"'
        )
        print("  Restored stats-section animation classes.")

    # Restore Explore More header
    content = content.replace(
        'class="text-center mb-16"',
        'class="text-center mb-16 animate-on-scroll opacity-0 translate-y-8 transition-all duration-700"'
    )

    # Restore Explore More cards (generic heuristic)
    # We look for the <a> tag with specific classes that match the card
    card_base_class = 'group relative bg-slate-900 rounded-2xl overflow-hidden border border-slate-800 hover:border-cyan-500/50 transition-all duration-300 cursor-pointer'
    
    # The previous replace removed 'animate-on-scroll ...'
    # We add it back.
    if card_base_class + ' hover:transform' in content:
        content = content.replace(
            card_base_class + ' hover:transform',
            card_base_class + ' animate-on-scroll opacity-0 translate-y-8 hover:transform'
        )
        print("  Restored card animation classes.")
        
    with open(home_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates complete.")
