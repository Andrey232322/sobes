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

    with open(os.path.join(zap, f'№{a}'), 'w') as s:
        s.write(str(list(csvReader)))

        return True

    colum = pandas.read_csv(a).columns.tolist()
    file.file.close()
    print('dwa')
    return data

