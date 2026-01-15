from bs4 import BeautifulSoup

# --- Gallery ---
print("Refactoring Gallery...")
with open('templates/gallery.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the main grid
grid = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6')
if grid:
    # Clear existing content
    grid.clear()
    # Insert Jinja loop placeholder
    grid.string = "__GALLERY_LOOP__"
    
    html_content = str(soup)
    
    jinja_loop = """
    {% for item in gallery_items %}
    <div class="group relative overflow-hidden rounded-xl cursor-pointer animate-on-scroll opacity-0 translate-y-8 transition-all duration-700">
        <div class="aspect-[4/3] bg-slate-900 overflow-hidden">
            <img alt="{{ item.title }}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" src="{{ item.image_url }}"/>
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900/90 via-slate-900/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                    <span class="text-cyan-400 text-sm font-medium mb-2 block">{{ item.category }}</span>
                    <h3 class="text-xl font-bold text-white mb-2">{{ item.title }}</h3>
                    {% if item.description %}
                    <p class="text-slate-300 text-sm">{{ item.description }}</p>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
    {% endfor %}
    """
    
    html_content = html_content.replace("__GALLERY_LOOP__", jinja_loop)
    
    with open('templates/gallery.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Gallery updated.")

# --- Videos ---
print("Refactoring Videos...")
with open('templates/videos.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the main grid. 
# Note: inspect_pages.py said: ['grid', 'md:grid-cols-2', 'lg:grid-cols-3', 'gap-6']
# But usually classes might be in different order.
grid = soup.find('div', class_=lambda x: x and 'grid' in x and 'md:grid-cols-2' in x and 'lg:grid-cols-3' in x)

if grid:
    grid.clear()
    grid.string = "__VIDEO_LOOP__"
    
    html_content = str(soup)
    
    jinja_loop = """
    {% for item in video_items %}
    <div class="group bg-slate-900 rounded-xl overflow-hidden border border-slate-800 hover:border-cyan-500/50 transition-all duration-300 animate-on-scroll opacity-0 translate-y-8">
        <a href="{{ item.video_url }}" target="_blank" class="block relative aspect-video overflow-hidden">
            <img alt="{{ item.title }}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" src="{{ item.thumbnail_url }}"/>
            <div class="absolute inset-0 bg-black/50 group-hover:bg-black/40 transition-colors flex items-center justify-center">
                <div class="w-12 h-12 bg-cyan-500/90 rounded-full flex items-center justify-center group-hover:scale-110 transition-transform duration-300 shadow-lg shadow-cyan-500/50">
                    <i class="ri-play-fill text-white text-2xl ml-1"></i>
                </div>
            </div>
            <div class="absolute top-4 right-4 px-2 py-1 bg-black/80 rounded text-xs text-white font-medium">{{ item.platform }}</div>
        </a>
        <div class="p-6">
            <h3 class="text-lg font-bold text-white mb-2 line-clamp-2 group-hover:text-cyan-400 transition-colors">{{ item.title }}</h3>
            <p class="text-slate-400 text-sm line-clamp-2">{{ item.description }}</p>
        </div>
    </div>
    {% endfor %}
    """
    
    html_content = html_content.replace("__VIDEO_LOOP__", jinja_loop)
    
    with open('templates/videos.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Videos updated.")

# --- Blog ---
print("Refactoring Blog...")
with open('templates/blog.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the main grid
grid = soup.find('div', class_=lambda x: x and 'grid' in x and 'md:grid-cols-2' in x and 'lg:grid-cols-3' in x)

if grid:
    grid.clear()
    grid.string = "__BLOG_LOOP__"
    
    html_content = str(soup)
    
    jinja_loop = """
    {% for post in blog_posts %}
    <article class="group bg-slate-900 rounded-2xl overflow-hidden border border-slate-800 hover:border-cyan-500/50 transition-all duration-300 animate-on-scroll opacity-0 translate-y-8 hover:-translate-y-1">
        <div class="relative h-48 overflow-hidden">
            {% if post.cover_image %}
            <img alt="{{ post.title }}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" src="{{ post.cover_image }}"/>
            {% else %}
            <div class="w-full h-full bg-slate-800 flex items-center justify-center">
                <i class="ri-article-line text-4xl text-slate-700"></i>
            </div>
            {% endif %}
            <div class="absolute top-4 left-4">
                <span class="px-3 py-1 bg-cyan-500/90 backdrop-blur-sm text-white text-xs font-medium rounded-full">{{ post.tags.split(',')[0] if post.tags else 'Article' }}</span>
            </div>
        </div>
        <div class="p-6">
            <div class="flex items-center gap-2 text-slate-500 text-xs mb-3">
                <i class="ri-calendar-line"></i>
                <span>{{ post.date }}</span>
                <span class="w-1 h-1 bg-slate-500 rounded-full"></span>
                <span>{{ post.author }}</span>
            </div>
            <h3 class="text-xl font-bold text-white mb-3 line-clamp-2 group-hover:text-cyan-400 transition-colors">{{ post.title }}</h3>
            <p class="text-slate-400 text-sm mb-4 line-clamp-3 leading-relaxed">{{ post.excerpt }}</p>
            <a class="inline-flex items-center gap-1 text-cyan-400 font-medium text-sm group-hover:gap-2 transition-all" href="#">
                Read More <i class="ri-arrow-right-line"></i>
            </a>
        </div>
    </article>
    {% endfor %}
    """
    
    html_content = html_content.replace("__BLOG_LOOP__", jinja_loop)
    
    with open('templates/blog.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Blog updated.")
