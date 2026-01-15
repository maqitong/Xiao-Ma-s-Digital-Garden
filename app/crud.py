from sqlalchemy.orm import Session
from . import models

# Projects
def get_projects(db: Session):
    return db.query(models.Project).all()

def create_project(db: Session, project: models.Project):
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if project:
        db.delete(project)
        db.commit()

# Messages
def create_message(db: Session, message: models.Message):
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_messages(db: Session):
    return db.query(models.Message).order_by(models.Message.created_at.desc()).all()

# Profile
def get_profile(db: Session):
    return db.query(models.Profile).first()

def create_or_update_profile(db: Session, name, role, bio, email, resume_url=None):
    profile = db.query(models.Profile).first()
    if not profile:
        profile = models.Profile(name=name, role=role, bio=bio, email=email, resume_url=resume_url)
        db.add(profile)
    else:
        profile.name = name
        profile.role = role
        profile.bio = bio
        profile.email = email
        if resume_url:
            profile.resume_url = resume_url
    db.commit()
    db.refresh(profile)
    return profile

# Experience
def get_experiences(db: Session):
    return db.query(models.Experience).all()

def create_experience(db: Session, title, company, duration, description):
    exp = models.Experience(title=title, company=company, duration=duration, description=description)
    db.add(exp)
    db.commit()
    return exp

def delete_experience(db: Session, exp_id: int):
    exp = db.query(models.Experience).filter(models.Experience.id == exp_id).first()
    if exp:
        db.delete(exp)
        db.commit()

# Education
def get_educations(db: Session):
    return db.query(models.Education).all()

def create_education(db: Session, degree, school, duration):
    edu = models.Education(degree=degree, school=school, duration=duration)
    db.add(edu)
    db.commit()
    return edu

def delete_education(db: Session, edu_id: int):
    edu = db.query(models.Education).filter(models.Education.id == edu_id).first()
    if edu:
        db.delete(edu)
        db.commit()

# Skills
def get_skills(db: Session):
    return db.query(models.Skill).all()

def create_skill(db: Session, name, category):
    skill = models.Skill(name=name, category=category)
    db.add(skill)
    db.commit()
    return skill

def delete_skill(db: Session, skill_id: int):
    skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if skill:
        db.delete(skill)
        db.commit()

# --- New CRUD for Gallery, Videos, Blog ---

# Gallery
def get_gallery_items(db: Session):
    return db.query(models.GalleryItem).all()

def create_gallery_item(db: Session, title, description, image_url, category):
    item = models.GalleryItem(title=title, description=description, image_url=image_url, category=category)
    db.add(item)
    db.commit()
    return item

def delete_gallery_item(db: Session, item_id: int):
    item = db.query(models.GalleryItem).filter(models.GalleryItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()

# Videos
def get_video_items(db: Session):
    return db.query(models.VideoItem).all()

def create_video_item(db: Session, title, description, video_url, thumbnail_url, platform):
    item = models.VideoItem(title=title, description=description, video_url=video_url, thumbnail_url=thumbnail_url, platform=platform)
    db.add(item)
    db.commit()
    return item

def delete_video_item(db: Session, item_id: int):
    item = db.query(models.VideoItem).filter(models.VideoItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()

# Blog
def get_blog_posts(db: Session):
    return db.query(models.BlogPost).order_by(models.BlogPost.id.desc()).all()

def create_blog_post(db: Session, title, excerpt, content, cover_image, author, date, tags):
    post = models.BlogPost(title=title, excerpt=excerpt, content=content, cover_image=cover_image, author=author, date=date, tags=tags)
    db.add(post)
    db.commit()
    return post

def delete_blog_post(db: Session, post_id: int):
    post = db.query(models.BlogPost).filter(models.BlogPost.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
