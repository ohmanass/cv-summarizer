# from app.routeurs.cvs import router
# from fastapi import FastAPI
# from app.db.session import Base
# from app.db.database import engine

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Welcome to the CV-Summarizer API"}

# # Base.metadata.create_all(bind=engine)
# # app.include_router(router)


from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import os
import shutil
from pathlib import Path
import uuid

LIMIT_FILE_SIZE = 500000

name_file = str(uuid.uuid4())
# Create upload directory
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI(title="FastAPI File Upload Service")

@app.post("/upload/single")
async def upload_single_file(file: UploadFile = File(...)):
    ## Errors Handling
    if file.filename == "":
        raise HTTPException(status_code=412, detail="No file selected")

    if file.size > LIMIT_FILE_SIZE:
        raise HTTPException(status_code=413, detail="Payload Too Large")
    
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=415, detail="Unsupported Media Type")

    file_ext = Path(file.filename).suffix
    unique_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = UPLOAD_DIR / unique_filename
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {
        "filename": name_file,
        "content_type": file.content_type,
        "size": file.size,
        "location": str(file_path)
    }

@app.get("/")
async def root():
    return {"message": "FastAPI File Upload Service is running"}
