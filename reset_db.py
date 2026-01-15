
from app.database import SessionLocal
from app.models import Project

def reset_projects():
    db = SessionLocal()
    db.query(Project).delete()
    db.commit()
    print("Deleted all projects.")
    db.close()

if __name__ == '__main__':
    reset_projects()
