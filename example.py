import MySQLdb
import time

# MySQLの起動を待つため
time.sleep(5)

connection = MySQLdb.connect(
        host='db',
        user='docker',
        passwd='docker',
        db='test_database'
        )
cursor = connection.cursor()

cursor.execute("SHOW CREATE DATABASE test_database;")

myresult = cursor.fetchall()
for row in myresult:
    print(row)

connection.close()
