import codecs
import csv
import glob
import json
import os
import sqlite3
import pandas
zap = 'zapic`'
file = os.listdir(zap)
a = pandas.read_csv('12.csv').columns.tolist()
b = []
with open('12.csv', 'r') as s:
    csvReader = csv.DictReader(s)
    with open(os.path.join(zap, '12.csv'), 'w') as w:
        wr = csv.DictWriter(w,fieldnames=a)
        for i in csvReader:
            b.append(i)
            #print(wr.writerow(i))

print(b)
for i in b:
    print(type(i))
# file = os.listdir(zap)
# b = []
# for i in file:
#     with open(i, 'r') as r:
#         b.append(r.read())
# print(b)



# db =sqlite3.connect('test_db')
# sql = db.cursor()
#
# sql.execute(""""CREATE TABLE IF NOT EXISTS Users()""")
