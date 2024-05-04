import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done. DB Created!")
