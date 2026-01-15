from bs4 import BeautifulSoup
import re

with open('templates/resume.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Helper to replace list
def replace_list(header_text, jinja_template):
    # Find header by text (searching recursively)
    header = soup.find(lambda tag: tag.name in ['h2', 'h3', 'h4', 'h5'] and header_text in tag.get_text())
    
    if header:
        print(f"Found header for {header_text}: {header}")
        # The list container is likely the next sibling, or we need to traverse up/down
        # In many templates, it's:
        # <div>
        #   <h4>Header</h4>
        #   <div class="list">...</div>
        # </div>
        
        container = header.find_next_sibling('div')
        if not container:
            # Try parent's next sibling?
            # <div><h4>Header</h4></div>
            # <div class="list">...</div>
            # But let's check if the container has content.
            pass
            
        if container:
            print(f"  Replacing content in container: {container.name} with {len(container.contents)} items")
            container.clear()
            # We must NOT use BeautifulSoup(jinja, 'html.parser') directly if it contains {{ }} blocks that might be malformed HTML
            # But Jinja is text.
            # We can't insert Jinja logic as a BS4 tag easily because it's not valid HTML.
            # However, we can insert it as a NavigableString or comment, but that won't render.
            # Actually, standard way is to treat it as text.
            # But BS4 escapes text.
            
            # WORKAROUND: We will replace the whole container with a placeholder, 
            # and then do a string replace on the final output.
            placeholder = f"__REPLACE_{header_text}__"
            container.string = placeholder
            return placeholder, jinja_template
    else:
        print(f"Header {header_text} not found")
        return None, None

replacements = {}

# Experience
exp_html = """
{% for exp in experiences %}
<div class="mb-6 border-l-2 border-slate-200 pl-4 ml-2">
    <h5 class="text-lg font-bold text-slate-800">{{ exp.title }}</h5>
    <div class="text-sm text-cyan-600 mb-1">{{ exp.company }} | {{ exp.duration }}</div>
    <p class="text-slate-600 leading-relaxed">{{ exp.description }}</p>
</div>
{% endfor %}
"""
p, t = replace_list("工作经验", exp_html)
if p: replacements[p] = t

# Education
edu_html = """
{% for edu in educations %}
<div class="mb-6 border-l-2 border-slate-200 pl-4 ml-2">
    <h5 class="text-lg font-bold text-slate-800">{{ edu.school }}</h5>
    <div class="text-sm text-cyan-600 mb-1">{{ edu.degree }} | {{ edu.duration }}</div>
</div>
{% endfor %}
"""
p, t = replace_list("教育背景", edu_html)
if p: replacements[p] = t

# Skills
# Found "专业技能" in h2
skill_html = """
<div class="flex flex-wrap gap-2">
{% for skill in skills %}
<span class="px-4 py-2 bg-slate-100 text-slate-700 rounded-lg text-sm font-medium hover:bg-cyan-50 hover:text-cyan-600 transition-colors">{{ skill.name }}</span>
{% endfor %}
</div>
"""
p, t = replace_list("专业技能", skill_html)
if p: replacements[p] = t

# Save structure first
output_html = str(soup)

# Apply string replacements
for placeholder, content in replacements.items():
    output_html = output_html.replace(placeholder, content)

# Write back
with open('templates/resume.html', 'w', encoding='utf-8') as f:
    f.write(output_html)
