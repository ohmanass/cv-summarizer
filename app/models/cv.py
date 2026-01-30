from app.db.session import Base
from sqlalchemy import Column, Integer, String

class Car(Base):    
    __tablename__ = "cvs"
    
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)