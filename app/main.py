from app.routeurs.cvs import routeur
from fastapi import FastAPI
from app.db.session import Base
from app.db.database import engine

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the CV-Summarizer API"}

Base.metadata.create_all(bind=engine)
app.include_router(routeur)