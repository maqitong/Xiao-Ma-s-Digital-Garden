import markdown
from fastapi import APIRouter, Request, Depends, Form, status, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import database, crud, models
import shutil
import os

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="templates")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Dashboard ---
@router.get("/", response_class=HTMLResponse)
async def admin_dashboard(request: Request, db: Session = Depends(get_db)):
    profile = crud.get_profile(db)
    msg_count = db.query(models.Message).count()
    proj_count = db.query(models.Project).count()
    blog_count = db.query(models.BlogPost).count()
    gallery_count = db.query(models.GalleryItem).count()
    video_count = db.query(models.VideoItem).count()
    
    return templates.TemplateResponse("admin/dashboard.html", {
        "request": request,
        "profile": profile,
        "msg_count": msg_count,
        "proj_count": proj_count,
        "blog_count": blog_count,
        "gallery_count": gallery_count,
        "video_count": video_count
    })

# --- Profile ---
@router.get("/profile", response_class=HTMLResponse)
async def admin_profile(request: Request, db: Session = Depends(get_db)):
    profile = crud.get_profile(db)
    experiences = crud.get_experiences(db)
    educations = crud.get_educations(db)
    skills = crud.get_skills(db)
    return templates.TemplateResponse("admin/profile.html", {
        "request": request,
        "profile": profile,
        "experiences": experiences,
        "educations": educations,
        "skills": skills
    })

@router.post("/profile")
async def update_profile(
    request: Request,
    name: str = Form(...),
    role: str = Form(...),
    bio: str = Form(...),
    email: str = Form(...),
    resume_file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    resume_url = None
    if resume_file and resume_file.filename:
        # Create static/resumes directory if not exists
        os.makedirs("static/resumes", exist_ok=True)
        file_location = f"static/resumes/{resume_file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(resume_file.file, file_object)
        resume_url = f"/{file_location}"
    
    crud.create_or_update_profile(db, name, role, bio, email, resume_url)
    return RedirectResponse(url="/admin/profile", status_code=status.HTTP_303_SEE_OTHER)

# --- Experience ---
@router.post("/experience/add")
async def add_experience(
    request: Request,
    title: str = Form(...),
    company: str = Form(...),
    duration: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    crud.create_experience(db, title, company, duration, description)
    return RedirectResponse(url="/admin/profile", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/experience/delete/{id}")
async def delete_experience(id: int, db: Session = Depends(get_db)):
    crud.delete_experience(db, id)
    return RedirectResponse(url="/admin/profile", status_code=status.HTTP_303_SEE_OTHER)

# --- Education ---
@router.post("/education/add")
async def add_education(
    request: Request,
    degree: str = Form(...),
    school: str = Form(...),
    duration: str = Form(...),
    db: Session = Depends(get_db)
):
    crud.create_education(db, degree, school, duration)
    return RedirectResponse(url="/admin/profile", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/education/delete/{id}")
async def delete_education(id: int, db: Session = Depends(get_db)):
    crud.delete_education(db, id)
    return RedirectResponse(url="/admin/profile", status_code=status.HTTP_303_SEE_OTHER)

# --- Skills ---
@router.post("/skill/add")
async def add_skill(
    request: Request,
    name: str = Form(...),
    category: str = Form("General"),
    db: Session = Depends(get_db)
):
    crud.create_skill(db, name, category)
    return RedirectResponse(url="/admin/profile", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/skill/delete/{id}")
async def delete_skill(id: int, db: Session = Depends(get_db)):
    crud.delete_skill(db, id)
    return RedirectResponse(url="/admin/profile", status_code=status.HTTP_303_SEE_OTHER)

# --- Projects ---
@router.get("/projects", response_class=HTMLResponse)
async def admin_projects(request: Request, db: Session = Depends(get_db)):
    projects = crud.get_projects(db)
    return templates.TemplateResponse("admin/projects.html", {"request": request, "projects": projects})

@router.post("/projects/add")
async def add_project(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    image_url: str = Form(...),
    link: str = Form(...),
    category: str = Form(...),
    tags: str = Form(""),
    db: Session = Depends(get_db)
):
    new_project = models.Project(
        title=title,
        description=description,
        image_url=image_url,
        link=link,
        category=category,
        tags=tags
    )
    crud.create_project(db, new_project)
    return RedirectResponse(url="/admin/projects", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/projects/delete/{id}")
async def delete_project(id: int, db: Session = Depends(get_db)):
    crud.delete_project(db, id)
    return RedirectResponse(url="/admin/projects", status_code=status.HTTP_303_SEE_OTHER)

# --- Messages ---
@router.get("/messages", response_class=HTMLResponse)
async def admin_messages(request: Request, db: Session = Depends(get_db)):
    messages = crud.get_messages(db)
    return templates.TemplateResponse("admin/messages.html", {"request": request, "messages": messages})

# --- Gallery ---
@router.get("/gallery", response_class=HTMLResponse)
async def admin_gallery(request: Request, db: Session = Depends(get_db)):
    gallery_items = crud.get_gallery_items(db)
    return templates.TemplateResponse("admin/gallery.html", {"request": request, "gallery_items": gallery_items})

@router.post("/gallery/add")
async def add_gallery_item(
    request: Request,
    title: str = Form(...),
    description: str = Form(""),
    image_url: str = Form(...),
    category: str = Form("Photography"),
    db: Session = Depends(get_db)
):
    crud.create_gallery_item(db, title, description, image_url, category)
    return RedirectResponse(url="/admin/gallery", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/gallery/delete/{id}")
async def delete_gallery_item(id: int, db: Session = Depends(get_db)):
    crud.delete_gallery_item(db, id)
    return RedirectResponse(url="/admin/gallery", status_code=status.HTTP_303_SEE_OTHER)

# --- Videos ---
@router.get("/videos", response_class=HTMLResponse)
async def admin_videos(request: Request, db: Session = Depends(get_db)):
    video_items = crud.get_video_items(db)
    return templates.TemplateResponse("admin/videos.html", {"request": request, "video_items": video_items})

@router.post("/videos/add")
async def add_video_item(
    request: Request,
    title: str = Form(...),
    description: str = Form(""),
    video_url: str = Form(...),
    thumbnail_url: str = Form(...),
    platform: str = Form("YouTube"),
    db: Session = Depends(get_db)
):
    crud.create_video_item(db, title, description, video_url, thumbnail_url, platform)
    return RedirectResponse(url="/admin/videos", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/videos/delete/{id}")
async def delete_video_item(id: int, db: Session = Depends(get_db)):
    crud.delete_video_item(db, id)
    return RedirectResponse(url="/admin/videos", status_code=status.HTTP_303_SEE_OTHER)

# --- Blog ---
@router.get("/blog", response_class=HTMLResponse)
async def admin_blog(request: Request, db: Session = Depends(get_db)):
    blog_posts = crud.get_blog_posts(db)
    return templates.TemplateResponse("admin/blog.html", {"request": request, "blog_posts": blog_posts})

@router.post("/blog/add")
async def add_blog_post(
    request: Request,
    title: str = Form(...),
    excerpt: str = Form(...),
    content: str = Form(...),
    cover_image: str = Form(""),
    author: str = Form("Xiao Ma"),
    date: str = Form(...),
    tags: str = Form(""),
    db: Session = Depends(get_db)
):
    # Store Raw Content (Markdown or HTML) directly
    # Rendering will happen at display time in main.py
    crud.create_blog_post(db, title, excerpt, content, cover_image, author, date, tags)
    return RedirectResponse(url="/admin/blog", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/blog/delete/{id}")
async def delete_blog_post(id: int, db: Session = Depends(get_db)):
    crud.delete_blog_post(db, id)
    return RedirectResponse(url="/admin/blog", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/blog/edit/{id}", response_class=HTMLResponse)
async def edit_blog_post(id: int, request: Request, db: Session = Depends(get_db)):
    post = crud.get_blog_post(db, id)
    if not post:
        return RedirectResponse(url="/admin/blog", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("admin/edit_blog.html", {"request": request, "post": post})

@router.post("/blog/edit/{id}")
async def update_blog_post(
    id: int,
    request: Request,
    title: str = Form(...),
    excerpt: str = Form(...),
    content: str = Form(...),
    cover_image: str = Form(""),
    author: str = Form("Xiao Ma"),
    date: str = Form(...),
    tags: str = Form(""),
    db: Session = Depends(get_db)
):
    # Same here, convert MD to HTML
    # Note: This implies the user must input Markdown in the edit box.
    # If the database stores HTML, converting HTML to Markdown for editing is hard.
    # Strategy: For this task, we will assume the user inputs Markdown.
    # But if we load HTML into the textarea, it will be messy.
    # Ideally, we should add a 'content_md' column. 
    # However, to avoid DB migration complexity for this task, 
    # we will just support writing HTML/Markdown mixed or just Markdown.
    # If we overwrite 'content' with HTML, next time we edit we see HTML.
    # This is not ideal for "Markdown Support".
    # Correct approach:
    # 1. Add `content_source` column to BlogPost to store raw Markdown.
    # 2. Render HTML on the fly or store compiled HTML in `content`.
    # Given the constraint of "simple changes", let's try to just render on the fly in the frontend?
    # No, Jinja2 doesn't render MD by default.
    # Let's update the model to store raw markdown if possible?
    # Or just assume the 'content' field stores Markdown, and we render it at runtime.
    # Let's check `app/models.py` again.
    
    # If we change `content` to store Markdown, existing HTML posts might break if we treat them as MD?
    # Markdown parser usually handles HTML fine.
    # So, let's change the strategy:
    # 1. `content` stores Raw Markdown (or HTML).
    # 2. `admin` saves raw content.
    # 3. `main.py` renders Markdown to HTML when serving the post.
    
    # So in `admin.py`, we should NOT convert to HTML. We just save as is.
    crud.update_blog_post(db, id, title, excerpt, content, cover_image, author, date, tags)
    return RedirectResponse(url="/admin/blog", status_code=status.HTTP_303_SEE_OTHER)
