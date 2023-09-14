import codecs
import csv
import json
import os.path
from fastapi import FastAPI, UploadFile, File
import pandas

import sqlite3

app = FastAPI()
zap = 'zapic`'
#################################
### headre scv который d csv.dictreadre есть
### pandas read_csv chunksize

@app.post('/upload')
def upload(file: UploadFile = File(...)):
    a = file.filename
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))

    """запись и хранение файлов и данных на локалке, позже реализовать 
    нэйм какой на входе прилетает и проверять есть он или нет"""
    b = []
    with open(os.path.join(zap, f'{a}'), 'r') as s:
        csvReader = csv.DictReader(s)
        with open(os.path.join(zap, '12.csv'), 'r') as w:
            wr = csv.DictWriter(w, fieldnames=a)
            for i in csvReader:
                b.append(i)
        for i in b:
            wr.writerow(i)
        return True

    colum = pandas.read_csv(a).columns.tolist()
    file.file.close()
    print('dwa')
    return data

@app.get('/show')
def show():
    file = os.listdir(zap)
    b = []
    for i in file:
        with open(i, 'r', encoding='utf-8') as r:
            b.append(r.read())
    return b