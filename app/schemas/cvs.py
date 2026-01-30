from pydantic import BaseModel

class CvBase(BaseModel):
    file_name: str
    file_size: int
    file_path: str

class Cv(BaseModel):
    id: int

    class Config:
        from_attributes = True