import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS db_penjualan")
print("Database Dibuat atau Sudah Ada")
