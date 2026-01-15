
from app.database import SessionLocal, engine
from app import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Check if projects exist
if db.query(models.Project).count() == 0:
    print("Seeding projects...")
    p1 = models.Project(
        title="Digital Garden V1",
        description="The first version of my personal website using static HTML.",
        image_url="/static/projects_files/search-image.jpg",  # Use existing images as placeholder
        link="#",
        tags="HTML,CSS",
        category="Web"
    )
    p2 = models.Project(
        title="Python Automation Script",
        description="A script to automate file organization and processing.",
        image_url="/static/projects_files/search-image(1).jpg",
        link="#",
        tags="Python,Automation",
        category="Script"
    )
    db.add(p1)
    db.add(p2)
    db.commit()
    print("Projects seeded!")
else:
    print("Projects already exist.")

db.close()
