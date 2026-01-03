from infrastructure.db_setup import create_database_and_table
from presentation.cli import menu

if __name__ == "__main__":
    create_database_and_table()  # otomatis create DB & table jika belum ada
    menu()
