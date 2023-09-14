import glob
import json
import os
import sqlite3
import pandas

a = pandas.read_csv('12.csv').columns.tolist()
db =sqlite3.connect('test_db')
sql = db.cursor()

sql.execute(""""CREATE TABLE IF NOT EXISTS Users()""")
