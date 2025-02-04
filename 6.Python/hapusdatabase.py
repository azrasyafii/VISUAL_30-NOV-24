import mysql.connector

# Koneksi ke MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Membuat cursor
mycursor = mydb.cursor()

# Nama database yang ingin dicek dan dihapus
nama_database = "db_penjualan"

# Mengecek daftar database yang ada
mycursor.execute("SHOW DATABASES")

# Menyimpan hasil pengecekan ke dalam list
databases = [db[0] for db in mycursor]

# Mengecek apakah database ada
if nama_database in databases:
    print(f"Database '{nama_database}' ditemukan. Menghapus database...")
    mycursor.execute(f"DROP DATABASE {nama_database}")
    print(f"Database '{nama_database}' berhasil dihapus.")
else:
    print(f"Database '{nama_database}' tidak ditemukan.")
