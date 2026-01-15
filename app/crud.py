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

def create_or_update_profile(db: Session, name, role, bio, email):
    profile = db.query(models.Profile).first()
    if not profile:
        profile = models.Profile(name=name, role=role, bio=bio, email=email)
        db.add(profile)
    else:
        profile.name = name
        profile.role = role
        profile.bio = bio
        profile.email = email
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
