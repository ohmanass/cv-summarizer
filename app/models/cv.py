from app.db.session import Base
from sqlalchemy import Column, Integer, String

class Cv(Base):    
    __tablename__ = "cvs"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    location = Column(String, nullable=False)
    contenttype = Column(String,nullable=False)
    size = Column(Integer, nullable=False)
    desc = Column(String, nullable=True)