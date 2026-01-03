from tabulate import tabulate
from application.mahasiswa import MahasiswaService
from domain.mahasiswa import Mahasiswa
from infrastructure.mysql_repository import MySQLRepository
import tkinter as tk



def menu():
    window = tk.Tk()
    window.mainloop()
    repo = MySQLRepository()
    service = MahasiswaService(repo)

    while True:
        print("\n" + "="*30)
        print("MENU MANAJEMEN MAHASISWA")
        print("="*30)
        print("1. Tambah Mahasiswa")
        print("2. Lihat Semua Mahasiswa")
        print("3. Update Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        print("-"*30)

        choice = input("Pilih menu (1-5): ").strip()

        if choice == "1":
            print("\n--- TAMBAH MAHASISWA ---")
            nama = input("Nama: ").strip()
            nim = input("NIM: ").strip()
            jurusan = input("Jurusan: ").strip()
            angkatan = int(input("Angkatan: ").strip())
            service.create(Mahasiswa(0, nama, nim, jurusan, angkatan))
            print("✅ Mahasiswa berhasil ditambahkan")

        elif choice == "2":
            print("\n--- DAFTAR MAHASISWA ---")
            mahasiswa_list = service.get_all()
            if mahasiswa_list:
                # Mengonversi data mahasiswa ke format tabel
                table_data = []
                for m in mahasiswa_list:
                    # Asumsi: Mahasiswa memiliki atribut id, nama, nim, jurusan, angkatan
                    table_data.append([
                        m.id, 
                        m.nama, 
                        m.nim, 
                        m.jurusan, 
                        m.angkatan
                    ])
                
                # Header tabel
                headers = ["ID", "Nama", "NIM", "Jurusan", "Angkatan"]
                
                # Menampilkan tabel
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
                
                # Menampilkan jumlah data
                print(f"\n📊 Total: {len(mahasiswa_list)} mahasiswa")
            else:
                print("📭 Tidak ada data mahasiswa")

        elif choice == "3":
            print("\n--- UPDATE DATA MAHASISWA ---")
            nim = input("NIM mahasiswa yang ingin diupdate: ").strip()
            mahasiswa = service.get_by_nim(nim)
            
            if not mahasiswa:
                print("❌ Mahasiswa tidak ditemukan")
                continue
            
            # Tampilkan data lama
            print(f"\nData saat ini:")
            print(f"Nama    : {mahasiswa.nama}")
            print(f"NIM     : {mahasiswa.nim}")
            print(f"Jurusan : {mahasiswa.jurusan}")
            print(f"Angkatan: {mahasiswa.angkatan}")
            print("-"*30)
            
            # Input data baru
            print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
            nama_baru = input(f"Nama baru [{mahasiswa.nama}]: ").strip()
            jurusan_baru = input(f"Jurusan baru [{mahasiswa.jurusan}]: ").strip()
            angkatan_baru = input(f"Angkatan baru [{mahasiswa.angkatan}]: ").strip()
            
            # Gunakan nilai lama jika input kosong
            nama = nama_baru if nama_baru else mahasiswa.nama
            jurusan = jurusan_baru if jurusan_baru else mahasiswa.jurusan
            angkatan = int(angkatan_baru) if angkatan_baru else mahasiswa.angkatan
            
            service.update(nim, Mahasiswa(mahasiswa.id, nama, nim, jurusan, angkatan))
            print("✅ Data mahasiswa berhasil diupdate")

        elif choice == "4":
            print("\n--- HAPUS DATA MAHASISWA ---")
            nim = input("NIM mahasiswa yang ingin dihapus: ").strip()
            
            # Konfirmasi sebelum menghapus
            mahasiswa = service.get_by_nim(nim)
            if mahasiswa:
                print(f"\n⚠️  Akan menghapus data:")
                print(f"Nama    : {mahasiswa.nama}")
                print(f"NIM     : {mahasiswa.nim}")
                print(f"Jurusan : {mahasiswa.jurusan}")
                
                konfirmasi = input("\nApakah Anda yakin? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    service.delete(nim)
                    print("✅ Mahasiswa berhasil dihapus")
                else:
                    print("❌ Penghapusan dibatalkan")
            else:
                print("❌ Mahasiswa tidak ditemukan")

        elif choice == "5":
            print("\n👋 Terima kasih telah menggunakan sistem!")
            repo.close()
            break

        else:
            print("❌ Pilihan tidak valid. Silakan pilih 1-5")

if __name__ == "__main__":
    menu()