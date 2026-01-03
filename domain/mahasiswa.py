from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Mahasiswa:
    id: Optional[int]
    nama: str
    nim: str
    jurusan: str
    angkatan: int
    created_at: Optional[datetime] = None
