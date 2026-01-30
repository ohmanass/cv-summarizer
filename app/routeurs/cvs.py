from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import shutil
from pathlib import Path
import uuid
from app.schemas.cvs import CvCreate, CvBase, Cv
from app.models.cv import Cv as CvModel
from app.services.ai import generate_cv_resume
from app.db.database import get_db
from fastapi import Depends

LIMIT_FILE_SIZE = 500000
name_file = str(uuid.uuid4())
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

routeur = APIRouter(prefix="/cvs", tags=["cvs"])

@routeur.post("/upload")
async def upload_single_file(file: UploadFile = File(...)):
    ## Errors Handling
    if file.filename == "":
        raise HTTPException(status_code=412, detail="No file selected")

    if file.size > LIMIT_FILE_SIZE:
        raise HTTPException(status_code=413, detail="Payload Too Large")
    
    if file.contenttype != "application/pdf":
        raise HTTPException(status_code=415, detail="Unsupported Media Type")

    file_ext = Path(file.filename).suffix
    unique_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = UPLOAD_DIR / unique_filename
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {
        "filename": name_file,
        "contenttype": file.content_type,
        "size": file.size,
        "location": str(file_path)
    }

@routeur.get("/")
async def root():
    return {"message": "FastAPI File Upload Service is running"}

@routeur.post("/resume", response_model=CvBase)
async def generate_resume(
    cv: CvCreate,
    db: Session = Depends(get_db)
):  
    print(cv)
    db_cv = CvModel(**cv.model_dump())
    print(db_cv)
    db.add(db_cv)
    db.commit()
    db.refresh(db_cv)

    #prompt = f"Résume moi le cv {cv.filename} present dans {cv.location} qui a pour taille {cv.size}."
    description = "desccccccc" #await generate_cv_resume(cv.filename, cv.contenttype, cv.location)

    db_cv.desc = description
    db.commit()
    db.refresh(db_cv)
    return db_cv