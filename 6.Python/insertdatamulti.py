import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="db_penjualan")
    
    mycursor = mydb.cursor()
    sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
    val = [("3", "Drinks"),("4", "Tepung")]
    mycursor.executemany(sql, val)
    
    mydb.commit()
    print(mycursor.rowcount, "Data Berhasil Ditambahkan.")


except mysql.connector.Error as err:
    print("Error: ", err)
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
