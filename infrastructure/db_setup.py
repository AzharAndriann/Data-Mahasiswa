import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "mahasiswa_app")

def create_database_and_table():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database `{DB_NAME}` ready")

        cursor.execute(f"USE {DB_NAME}")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100) NOT NULL,
            nim VARCHAR(20) NOT NULL UNIQUE,
            jurusan VARCHAR(50) NOT NULL,
            angkatan INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        print("Table `mahasiswa` ready")

        cursor.close()
        conn.close()
    except Error as e:
        print(f"❌ Error creating DB or table: {e}")

if __name__ == "__main__":
    create_database_and_table()
