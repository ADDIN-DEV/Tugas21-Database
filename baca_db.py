import sqlite3

# koneksi ke file DB SQLite nya
conn = sqlite3.connect('E:\Python Courses\API Test/test.db')
cursor = conn.cursor()


cursor.execute("SELECT * FROM sintesa")
rows = cursor.fetchall()

# tampilkan hasil
for row in rows:
    print(row)

# tutup koneksi
conn.close()
