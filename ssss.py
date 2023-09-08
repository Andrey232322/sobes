# import sqlite3
# import csv
# import os
#
#
# def create_db_table():
#     connection = sqlite3.connect('my_database.db')
#     cursor = connection.cursor()
#
#     # Создаем таблицу Users
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Users (
#     id TEXT,
#     name TEXT,
#     age real,
#     height real,
#     weight real
#     )
#     ''')
#
#     # Сохраняем изменения и закрываем соединение
#     connection.commit()
#     connection.close()
#
#
# def import_one_file_csv_to_sqlite(file:str):
#     con = sqlite3.connect('my_database.db')
#     cur = con.cursor()
#
#     with open(file, 'r', encoding='utf-8') as f_open_csv:
#         rows = csv.reader(f_open_csv,delimiter=",")
#
#         for row in rows:
#             a = tuple(row)
#             cur.execute('INSERT INTO Users (id,name, age, height, weight) VALUES (?,?, ?, ?, ?)', a)
#
#     con.commit()
#     con.close()
#
#
#
# create_db_table()
# import_one_file_csv_to_sqlite('12.csv')
#######################################################
# a = [
#     {
#       "id": 0,
#       "t1": "string",
#       "t2": "string",
#       "t3": "string",
#       "t4": "string",
#       "t5": "string"
#     },
#     {
#       "id": 2,
#       "t1": "string",
#       "t2": "string",
#       "t3": "string",
#       "t4": "string",
#       "t5": "string"
#     }
#   ]
# b = [
#     "zapic`\\№1.json",
#     "zapic`\\№2.json"
#   ]
# print(list(zip(a,b)))
