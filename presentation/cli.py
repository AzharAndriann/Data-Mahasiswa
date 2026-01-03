from application.mahasiswa_service import MahasiswaService
from domain.mahasiswa import Mahasiswa
from infrastructure.mysql_repository import MySQLRepository

def menu():
    repo = MySQLRepository()
    service = MahasiswaService(repo)

    while True:
        print("\n=== Menu Mahasiswa ===")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Semua Mahasiswa")
        print("3. Update Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")

        choice = input("Pilih menu: ").strip()

        if choice == "1":
            nama = input("Nama: ").strip()
            nim = input("NIM: ").strip()
            jurusan = input("Jurusan: ").strip()
            angkatan = int(input("Angkatan: ").strip())
            service.create(Mahasiswa(nama, nim, jurusan, angkatan))
            print("✅ Mahasiswa berhasil ditambahkan")

        elif choice == "2":
            for m in service.get_all():
                print(m)

        elif choice == "3":
            nim = input("NIM mahasiswa yang ingin diupdate: ").strip()
            if not service.get_by_nim(nim):
                print("❌ Mahasiswa tidak ditemukan")
                continue
            nama = input("Nama baru: ").strip()
            jurusan = input("Jurusan baru: ").strip()
            angkatan = int(input("Angkatan baru: ").strip())
            service.update(nim, Mahasiswa(nama, nim, jurusan, angkatan))
            print("✅ Mahasiswa berhasil diupdate")

        elif choice == "4":
            nim = input("NIM mahasiswa yang ingin dihapus: ").strip()
            service.delete(nim)
            print("✅ Mahasiswa berhasil dihapus")

        elif choice == "5":
            repo.close()
            break

        else:
            print("❌ Pilihan tidak valid")

if __name__ == "__main__":
    menu()
