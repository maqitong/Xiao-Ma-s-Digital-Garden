
import re
from bs4 import BeautifulSoup

def implement_projects():
    filepath = 'templates/projects.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Find the grid container
    # Based on inspection: found 2 grids. The first one (Grid 0) had project cards.
    grids = soup.find_all(class_=lambda x: x and 'grid' in x)
    if not grids:
        print("No grids found in projects.html")
        return

    # Grid 0 is likely the projects grid.
    project_grid = grids[0]
    
    # Get the first card to use as template
    cards = [c for c in project_grid.children if c.name]
    if not cards:
        print("No cards found in grid")
        return
    
    template_card = cards[0]
    
    # Convert template card to string and inject Jinja2 variables
    # We need to handle the structure. 
    # If it's a div, we might want to change it to 'a' if we have a link, 
    # or keep it as div and put the link inside?
    # But usually wrapping the whole card is better.
    
    # Let's see the structure of template_card
    # It has an image, a title, a description, tags.
    
    # We will construct the Jinja2 loop string manually to ensure correct placement.
    # We'll use the classes from the template_card.
    
    card_classes = template_card.get('class', [])
    card_class_str = " ".join(card_classes)
    
    # Check if there is an img
    img = template_card.find('img')
    img_classes = " ".join(img.get('class', [])) if img else ""
    
    # Check title (h3)
    h3 = template_card.find('h3')
    h3_classes = " ".join(h3.get('class', [])) if h3 else ""
    
    # Check description (p)
    p = template_card.find('p')
    p_classes = " ".join(p.get('class', [])) if p else ""
    
    # Check category/tag (span)
    # The inspection showed a span with bg-cyan-500/10
    span = template_card.find('span', class_=lambda x: x and 'bg-cyan-500/10' in x)
    span_classes = " ".join(span.get('class', [])) if span else ""
    
    # Construct the loop
    jinja_loop = f"""
    {{% for project in projects %}}
    <a href="{{{{ project.link }}}}" class="{card_class_str} block" target="_blank">
        <div class="relative h-64 overflow-hidden">
            <img alt="{{{{ project.title }}}}" class="{img_classes}" src="{{{{ project.image_url }}}}"/>
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-transparent to-transparent opacity-60"></div>
        </div>
        <div class="p-6">
            <div class="flex items-center justify-between mb-4">
                <span class="{span_classes}">{{{{ project.category }}}}</span>
            </div>
            <h3 class="{h3_classes}">{{{{ project.title }}}}</h3>
            <p class="{p_classes}">{{{{ project.description }}}}</p>
        </div>
    </a>
    {{% endfor %}}
    """
    
    # Replace the content of project_grid with the loop
    # We need to parse the jinja_loop string back to soup elements is hard because it's a template.
    # We can just replace the inner HTML of the grid.
    
    project_grid.clear()
    project_grid.append(BeautifulSoup(jinja_loop, 'html.parser'))
    
    # Write back
    # Note: BeautifulSoup will escape the Jinja tags if we are not careful? 
    # Actually, if we append it as a NavigableString or parsed soup, it might be fine.
    # But since it contains {{ }}, BS4 treats it as text.
    # We might need to unescape it or just write string replacement.
    
    html_str = str(soup)
    # The append might have escaped < > chars in the jinja_loop if processed as text.
    # Let's check.
    # Actually, appending BeautifulSoup(jinja_loop) parses the HTML tags in jinja_loop, 
    # but the {{ }} are text content. That should be fine.
    # The only issue is {% for %} which is not valid HTML tag. BS4 might treat it as text.
    
    # Let's verify if the output html has &lt;% for ...
    # If so, we need to fix it.
    html_str = html_str.replace('&lt;', '<').replace('&gt;', '>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_str)
    print("Implemented projects loop in projects.html")

def implement_blog_form():
    filepath = 'templates/blog.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    form = soup.find('form')
    if not form:
        print("No form found in blog.html")
        return
    
    form['id'] = 'contact-form'
    # Remove any existing action/method just in case
    if 'action' in form.attrs: del form['action']
    if 'method' in form.attrs: del form['method']
    
    # Add script
    script_content = """
    <script>
    document.getElementById('contact-form').addEventListener('submit', async function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        
        try {
            const response = await fetch('/api/message', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (response.ok) {
                alert('Message sent successfully!');
                this.reset();
            } else {
                alert('Failed to send message.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred.');
        }
    });
    </script>
    """
    
    # Append script to body
    if soup.body:
        soup.body.append(BeautifulSoup(script_content, 'html.parser'))
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Implemented form script in blog.html")

if __name__ == '__main__':
    implement_projects()
    implement_blog_form()
