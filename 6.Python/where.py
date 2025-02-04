import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    database="db_penjualan"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM kategori where id = '3'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)