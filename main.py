import codecs
import csv
import json
import os.path

from fastapi import FastAPI, UploadFile, File, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from schemas.schema import User_shema
import crud
from db import get_db, Base, engine
import glob


app = FastAPI()
Base.metadata.create_all(engine)

# @app.post('/upload')
# def upload(file: UploadFile = File(...)):
#     csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
#     data = {}
#     for rows in csvReader:
#         key = rows['Id']
#         data[key] = rows
#
#     file.file.close()
#     return data
#
# @app.post('/')
# def create(data:User_shema,db: Session = Depends(get_db)):
#     return crud.creat_user(data,db)
#
#
# @app.get('/{id}')
# def get(id:str,db: Session = Depends(get_db)):
#     return crud.get_user(id,db)


zap = 'zapic`'

class Item(BaseModel):
    id:int
    t1: str | None = None
    t2: str | None = None
    t3: str | None = None
    t4: str | None = None
    t5: str | None = None


def fail_est(id = 0):
    return glob.glob(os.path.join(zap,f'*{id if id else ""}.json'))

@app.get('/all')
def show():
    file = fail_est()

    v = {}
    if file:
        for f in file:
            with open(f,'r', encoding='UTF-8') as q:
                v[f] = json.load(q)

    return v

@app.post('/new_post')
def create_new(id:int,all:Item):
    file = fail_est(id)
    if file:
        return 'fail est`'
    else:
        with open(os.path.join(zap,f'№{id}.json'), 'w') as s:
            s.write(all.json())
        return True