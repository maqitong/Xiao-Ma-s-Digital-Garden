from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    image_url = Column(String)
    link = Column(String)
    tags = Column(String)  # Stored as comma-separated string
    category = Column(String)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    visitor_name = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# New Models for Resume/Profile
class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="Xiao Ma")
    role = Column(String, default="Full Stack Developer")
    bio = Column(Text, default="A passionate developer...")
    email = Column(String, default="mqtfire@qq.com")
    phone = Column(String, nullable=True)
    github = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    resume_url = Column(String, nullable=True)

class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    duration = Column(String)
    description = Column(Text)

class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)
    degree = Column(String)
    school = Column(String)
    duration = Column(String)

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String, default="General") # Frontend, Backend, Tools

# New Models for Gallery, Videos, Blog
class GalleryItem(Base):
    __tablename__ = "gallery_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    image_url = Column(String)
    category = Column(String, default="Photography")

class VideoItem(Base):
    __tablename__ = "video_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    video_url = Column(String) # Link to video
    thumbnail_url = Column(String)
    platform = Column(String, default="YouTube") # YouTube, Bilibili, etc.

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    excerpt = Column(Text) # Short summary
    content = Column(Text) # Full content (HTML or Markdown)
    cover_image = Column(String, nullable=True)
    author = Column(String, default="Xiao Ma")
    date = Column(String) # Simple string date for now, or DateTime
    tags = Column(String, nullable=True)
