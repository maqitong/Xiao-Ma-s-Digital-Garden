from app import models, database
from sqlalchemy.orm import Session

db = database.SessionLocal()
items = db.query(models.GalleryItem).all()
print(f"Found {len(items)} gallery items:")
for item in items:
    print(f"- {item.title}: {item.image_url}")
