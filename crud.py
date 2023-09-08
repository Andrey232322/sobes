from models.model import User
from schemas.schema import User_shema
from sqlalchemy.orm import Session
from fastapi import UploadFile,File
import codecs
import csv



def creat_user(data:User,db):
    user = User(id = data.id ,t1= data.t1,t2= data.t2,t3 = data.t3,t4=data.t4)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user



def get_user(id:int,db):
    return db.query(User).filter(User.id==id).first()

def remove(db:Session,id:int):
    user = db.query(User).filter(User.id==id).delete()
    db.commit()
    return user