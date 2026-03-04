import oracledb

# Konfigurasi Database
DB_USER = "trainingapi"
DB_PASSWORD = "bukapuasa"
# Jika menggunakan Oracle Database Free di Docker, DSN biasanya: localhost:1521/FREEPDB1
DB_DSN = "localhost:1521/FREEPDB1" 

def get_connection():
    """Membangun koneksi ke database Oracle."""
    try:
        connection = oracledb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            dsn=DB_DSN
        )
        return connection
    except oracledb.Error as e:
        # Menangani error koneksi
        error, = e.args
        print(f"Oracle-Error-Code: {error.code}")
        print(f"Oracle-Error-Message: {error.message}")
        raise

if __name__ == "__main__":
    try:
        # Memulai koneksi
        conn = get_connection()
        print("Connected to Oracle Database!")
        
        # Menggunakan Context Manager untuk cursor agar otomatis tertutup
        with conn.cursor() as cursor:
            cursor.execute("SELECT BANNER FROM v$version")
            row = cursor.fetchone()
            if row:
                print(f"Database version: {row[0]}")
        
        # Menutup koneksi utama
        conn.close()
        print("Connection closed.")
        
    except Exception as ex:
        print(f"Terjadi kesalahan saat menjalankan script: {ex}")