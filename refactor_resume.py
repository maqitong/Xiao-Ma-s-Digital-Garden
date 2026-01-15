from bs4 import BeautifulSoup
import re

with open('templates/resume.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# 1. Inject Profile Data
# Find "小马" in h3
name_tag = soup.find('h3', string=re.compile("小马"))
if name_tag:
    name_tag.string = "{{ profile.name }}"
    print("Replaced Name")

# Find Role
role_tag = soup.find('p', string=re.compile("全栈开发工程师"))
if role_tag:
    role_tag.string = "{{ profile.role }}"
    print("Replaced Role")

# Find Bio (Paragraph after role? Or separate?)
# In the Home page snippet, bio was "探索创意...".
# Let's look for a generic paragraph container if possible, or just skip bio for now if not distinct.

# 2. Experience
# Find h4 with "工作经验"
exp_header = soup.find('h4', string=re.compile("工作经验"))
if exp_header:
    # The container should be the parent's sibling or inside the same container
    # Based on home.html structure: h4 -> div.space-y-3 -> div.flex
    
    # Let's find the container of the list items
    # It's likely the next sibling div or the parent's next sibling
    exp_list_container = exp_header.find_next_sibling('div')
    if exp_list_container:
        # Create Jinja loop structure
        # We need to replace the content of this container with the loop
        
        # Sample item structure from home.html OCR:
        # <div class="flex justify-between"><span class="font-semibold">Role</span><span class="text-slate-500">Date</span></div>
        # We might need to check the actual HTML structure in resume.html
        
        # Let's just assume standard list structure and replace inner HTML
        new_html = """
        {% for exp in experiences %}
        <div class="mb-4">
            <div class="flex justify-between items-baseline mb-1">
                <h5 class="font-bold text-slate-800">{{ exp.title }}</h5>
                <span class="text-sm text-slate-500">{{ exp.duration }}</span>
            </div>
            <div class="text-sm text-cyan-600 mb-2">{{ exp.company }}</div>
            <p class="text-slate-600 text-sm leading-relaxed">{{ exp.description }}</p>
        </div>
        {% endfor %}
        """
        # We replace the content of the container
        # Use BeautifulSoup to parse the new HTML so it's inserted correctly?
        # Or just string replacement if we can identify the unique block.
        # BS4 modification is safer.
        exp_list_container.clear()
        exp_list_container.append(BeautifulSoup(new_html, 'html.parser'))
        print("Replaced Experience List")

# 3. Education
edu_header = soup.find('h4', string=re.compile("教育背景"))
if edu_header:
    edu_list_container = edu_header.find_next_sibling('div')
    if edu_list_container:
        new_html = """
        {% for edu in educations %}
        <div class="mb-4">
            <div class="flex justify-between items-baseline mb-1">
                <h5 class="font-bold text-slate-800">{{ edu.school }}</h5>
                <span class="text-sm text-slate-500">{{ edu.duration }}</span>
            </div>
            <div class="text-sm text-cyan-600">{{ edu.degree }}</div>
        </div>
        {% endfor %}
        """
        edu_list_container.clear()
        edu_list_container.append(BeautifulSoup(new_html, 'html.parser'))
        print("Replaced Education List")

# 4. Skills
skill_header = soup.find('h4', string=re.compile("技能")) # Or "专业技能"
if not skill_header:
    skill_header = soup.find('h4', string=re.compile("专业技能"))

if skill_header:
    skill_container = skill_header.find_next_sibling('div')
    if skill_container:
        # Assuming it's a flex wrap container
        new_html = """
        {% for skill in skills %}
        <span class="px-3 py-1 bg-slate-100 text-slate-700 rounded-full text-sm font-medium">{{ skill.name }}</span>
        {% endfor %}
        """
        skill_container.clear()
        skill_container.append(BeautifulSoup(new_html, 'html.parser'))
        print("Replaced Skills List")

# Save
with open('templates/resume.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
