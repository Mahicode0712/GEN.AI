from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Item(Base):
    __tablename__= "items"

    id          =Column(Integer, primary_key =True, index=True)
    name        =Column(String, nullable=False)
    description =Column(String, nullable=True)
    price       =Column(Integer, nullable=False)
    is_ative    =Column(Boolean, default=True)