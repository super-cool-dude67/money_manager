
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("postgresql+psycopg2://da:1111@localhost/cofee")

Base = declarative_base()


class Products(Base):
    __tablename__ = "products"
    id= Column(Integer,primary_key=True,nullable=False)
    name= Column(String(250), nullable=False)
    cost= Column(Integer,nullable=False)
    quantity= Column(Integer,nullable=False)

class Drinks(Base):
    __tablename__ = "drinks"
    id= Column(Integer,primary_key=True,nullable=False)
    name= Column(String(250), nullable=False)
    cost= Column(Integer,nullable=False)