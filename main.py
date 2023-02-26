from fastapi import FastAPI
from database.database import Base, SessionLocal, engine

api = FastAPI()

# VERIFY IF DB EXIST & IF CONNEXION IS ENABLED
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# END VERIFY

# Route test
@api.get("/")
async def root():
    return {"message": "Super API"}