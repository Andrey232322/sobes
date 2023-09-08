from db import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer,primary_key=True)
    t1 = Column(String)
    t2 = Column(String)
    t3 = Column(String)
    t4 = Column(String)