
from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from . import models, database, crud, admin # Import admin router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Include Admin Router
app.include_router(admin.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse, name="home")
async def read_root(request: Request, db: Session = Depends(get_db)):
    profile = crud.get_profile(db)
    skills = crud.get_skills(db)
    experiences = crud.get_experiences(db)
    projects = crud.get_projects(db)
    return templates.TemplateResponse("home.html", {
        "request": request, 
        "profile": profile, 
        "skills": skills,
        "experiences": experiences,
        "projects": projects
    })

@app.get("/resume", response_class=HTMLResponse, name="resume")
async def read_resume(request: Request, db: Session = Depends(get_db)):
    profile = crud.get_profile(db)
    experiences = crud.get_experiences(db)
    educations = crud.get_educations(db)
    skills = crud.get_skills(db)
    return templates.TemplateResponse("resume.html", {
        "request": request, 
        "profile": profile, 
        "experiences": experiences, 
        "educations": educations, 
        "skills": skills
    })

@app.get("/projects", response_class=HTMLResponse, name="projects")
async def read_projects(request: Request, db: Session = Depends(get_db)):
    projects = crud.get_projects(db)
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects})

@app.get("/gallery", response_class=HTMLResponse, name="gallery")
async def read_gallery(request: Request, db: Session = Depends(get_db)):
    gallery_items = crud.get_gallery_items(db)
    return templates.TemplateResponse("gallery.html", {"request": request, "gallery_items": gallery_items})

@app.get("/videos", response_class=HTMLResponse, name="videos")
async def read_videos(request: Request, db: Session = Depends(get_db)):
    video_items = crud.get_video_items(db)
    return templates.TemplateResponse("videos.html", {"request": request, "video_items": video_items})

@app.get("/blog", response_class=HTMLResponse, name="blog")
async def read_blog(request: Request, db: Session = Depends(get_db)):
    blog_posts = crud.get_blog_posts(db)
    return templates.TemplateResponse("blog.html", {"request": request, "blog_posts": blog_posts})

@app.post("/api/message")
async def create_message(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
    db: Session = Depends(get_db)
):
    db_message = models.Message(visitor_name=name, content=f"Email: {email}\nSubject: {subject}\nMessage: {message}")
    crud.create_message(db, db_message)
    return {"status": "success", "message": "Message sent successfully"}
