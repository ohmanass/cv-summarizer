# from fastapi import APIRouter, HTTPException
# from sqlalchemy.orm import Session
# #from app.models.cv import 

# MAX_FILE_SIZE = 5

# router = APIRouter(prefix="/cvs", tags=["cvs"])

# @router.get("/ping")
# def health_check():
#     return {"response": "pong"}

# @router.post("/upload")
# def upload_file(file: str):
#     if file.content_type != "app/pdf":
#         raise HTTPException(status_code=415, detail="Unsupported Media Type")
#     if file.size > MAX_FILE_SIZE:
#         raise HTTPException(status_code=413, detail="Payload Too Large")
    
#     cv_id = generate_uuid()
#     file_path = f'uploads/cvs/{cv_id}.pdf'
#     save_file_bytes(file_path, file.content)

#     return{
#         "id": cv_id,
#     }

# from fastapi import FastAPI, File, UploadFile, HTTPException
# from fastapi.responses import JSONResponse
# from typing import List
# import os
# import shutil
# from pathlib import Path

# # # Create upload directory
# # UPLOAD_DIR = Path("uploads")
# # UPLOAD_DIR.mkdir(exist_ok=True)

# # app = FastAPI(title="FastAPI File Upload Service")

# @app.post("/upload/single")
# async def upload_single_file(file: UploadFile = File(...)):
#     """Upload a single file with basic validation"""
#     if file.filename == "":
#         raise HTTPException(status_code=400, detail="No file selected")

#     file_path = UPLOAD_DIR / file.filename

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         "size": file.size,
#         "location": str(file_path)
#     }



