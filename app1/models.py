from sqlalchemy import Boolean, Column, ForeignKey, String, Integer

from database import Base

class Items(Base):
    __tablename__="items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)