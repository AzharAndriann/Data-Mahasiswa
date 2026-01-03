import mysql.connector
from mysql.connector import Error
from typing import List, Dict, Optional
from dotenv import load_dotenv
import os

load_dotenv()

class MySQLRepository:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
<<<<<<< HEAD
        self.password = os.getenv("DB_PASSWORD")
        self.port = 3308
=======
        self.password = os.getenv("DB_PASSWORD", "")
>>>>>>> 64982597e617bfafad7c3aa6af70826ddbd0afe7
        self.database = os.getenv("DB_NAME", "mahasiswa_app")
        self.conn: Optional[mysql.connector.connection_cext.CMySQLConnection] = None
        self.connect()

    def connect(self) -> None:
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                port=self.port,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                print("Connected to MySQL")
        except Error as e:
            raise ConnectionError(f"Error connecting to MySQL: {e}")

    def execute(self, query: str, params: tuple = ()) -> None:
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        cursor.close()

    def fetch_one(self, query: str, params: tuple = ()) -> Optional[Dict]:
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def fetch_all(self, query: str, params: tuple = ()) -> List[Dict]:
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        return results

    def close(self) -> None:
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Connection closed")
