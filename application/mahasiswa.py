from typing import List, Optional
from domain.mahasiswa import Mahasiswa
from infrastructure.mysql_repository import MySQLRepository

class MahasiswaService:
    def __init__(self, repo: MySQLRepository):
        self.repo = repo

    def create(self, mahasiswa: Mahasiswa) -> None:
        query = """
        INSERT INTO mahasiswa (nama, nim, jurusan, angkatan)
        VALUES (%s, %s, %s, %s)
        """
        params = (mahasiswa.nama, mahasiswa.nim, mahasiswa.jurusan, mahasiswa.angkatan)
        self.repo.execute(query, params)

    def get_all(self) -> List[Mahasiswa]:
        query = "SELECT * FROM mahasiswa ORDER BY created_at DESC"
        results = self.repo.fetch_all(query)
        return [Mahasiswa(**r) for r in results]

    def get_by_nim(self, nim: str) -> Optional[Mahasiswa]:
        query = "SELECT * FROM mahasiswa WHERE nim=%s"
        result = self.repo.fetch_one(query, (nim,))
        return Mahasiswa(**result) if result else None

    def update(self, nim: str, mahasiswa: Mahasiswa) -> None:
        query = """
        UPDATE mahasiswa
        SET nama=%s, jurusan=%s, angkatan=%s
        WHERE nim=%s
        """
        params = (mahasiswa.nama, mahasiswa.jurusan, mahasiswa.angkatan, nim)
        self.repo.execute(query, params)

    def delete(self, nim: str) -> None:
        query = "DELETE FROM mahasiswa WHERE nim=%s"
        self.repo.execute(query, (nim,))
