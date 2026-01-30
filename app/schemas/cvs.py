from pydantic import BaseModel

class CvBase(BaseModel):
    filename: str
    location: str
    contenttype: str
    size: int
    
class CvCreate(CvBase):
    pass

class Cv(CvBase):
    id: int

    class Config:
        from_attributes = True