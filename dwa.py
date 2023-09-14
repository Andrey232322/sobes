import csv
import glob
import json
import os
import sqlite3
import pandas
zap = 'zapic`'
file = os.listdir(zap)
a = pandas.read_csv('12.csv').columns.tolist()
with open('12.csv', 'r') as s:
    csvReader = csv.DictReader(s)
    with open(os.path.join(zap, '12.csv'), 'w') as w:
        write = csv.DictWriter(w, fieldnames=a)
        #write.writerow(a)
        for i in csvReader:
            write.writerow(i)









# b = []
# a = pandas.read_csv('zapic`\\12.csv').columns.tolist()
# for i in a:
#     b.append(i)
# for i in file:
#     with open(i, 'r', encoding='utf-8') as r:
#         for i in r:
#             b.append(i)






# db =sqlite3.connect('test_db')
# sql = db.cursor()
#
# sql.execute(""""CREATE TABLE IF NOT EXISTS Users()""")
