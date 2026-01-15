from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import database, crud, models

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
    return templates.TemplateResponse("admin/dashboard.html", {
        "request": request,
        "profile": profile,
        "msg_count": msg_count,
        "proj_count": proj_count
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
    db: Session = Depends(get_db)
):
    crud.create_or_update_profile(db, name, role, bio, email)
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
