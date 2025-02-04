import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjualan"
)

mycursor = mydb.cursor()
sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
val = ("5", "Roti")
mycursor.execute(sql, val)

mydb.commit()
print("1 Record Inserted, ID:", mycursor.lastrowid)
