from app.database import SessionLocal, engine
from app import models

def reset_db():
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    print("Database reset complete (dropped and recreated all tables).")

if __name__ == '__main__':
    reset_db()
