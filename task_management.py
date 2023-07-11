import json
import os   

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menyimpan tugas ke dalam file
def simpan_ke_file(tugas):
    with open('data_tugas.json', 'w') as file:
        json.dump(tugas, file)  

# Fungsi untuk membaca tugas dari file
def baca_dari_file():
    try:
        with open('data_tugas.json', 'r') as file:
            tugas = json.load(file)
    except FileNotFoundError:
        tugas = []
    return tugas

# Fungsi untuk menampilkan semua tugas
def tampilkan_tugas():
    tugas = baca_dari_file()
    if tugas:
        print("Daftar Tugas:")
        for idx, t in enumerate(tugas, start=1):
            print(f"{idx}. {t}")
    else:
        print("Belum ada tugas yang tersimpan.")

# Fungsi untuk menambahkan tugas baru
def tambahkan_tugas():
    tugas = baca_dari_file()
    tugas_baru = input("Masukkan tugas baru: ")
    tugas.append(tugas_baru)
    simpan_ke_file(tugas)
    print("Tugas berhasil ditambahkan.")

# Fungsi untuk memperbarui tugas yang ada
def perbarui_tugas():
    tugas = baca_dari_file()
    if tugas:
        tampilkan_tugas()
        indeks_tugas = int(input("\nPilih nomor tugas yang akan diperbarui: ")) - 1
        if 0 <= indeks_tugas < len(tugas):
            tugas_baru = input("Masukkan tugas yang diperbarui: ")
            tugas[indeks_tugas] = tugas_baru
            simpan_ke_file(tugas)
            print("Tugas berhasil diperbarui.")
        else:
            print("Nomor tugas tidak valid.")
    else:
        print("Belum ada tugas yang tersimpan.")

# Fungsi untuk menghapus tugas yang ada
def hapus_tugas():
    tugas = baca_dari_file()
    if tugas:
        clear()
        tampilkan_tugas()
        indeks_tugas = int(input("\nPilih nomor tugas yang akan dihapus: ")) - 1
        if 0 <= indeks_tugas < len(tugas):
            tugas.pop(indeks_tugas)
            simpan_ke_file(tugas)
            print("Tugas berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    else:
        print("Belum ada tugas yang tersimpan.")

# Menu utama
def menu():
    while True:
        print("\n===== Aplikasi Manajemen Tugas berbasis Python =====")
        print("============= Developed by Agrey Tosira ============\n")
        print("1. Tampilkan Daftar Tugas")
        print("2. Tambahkan Tugas")
        print("3. Perbarui Tugas")
        print("4. Hapus Tugas")
        print("0. Keluar\n")

        pilihan = input("Masukkan pilihan (0-4): ")
        
        if pilihan == '1':
            clear()
            tampilkan_tugas()
        elif pilihan == '2':
            clear()
            tambahkan_tugas()
        elif pilihan == '3':
            clear()
            perbarui_tugas()
        elif pilihan == '4':
            hapus_tugas()
        elif pilihan == '0':
            break
        else:
            clear()
            print("Pilihan tidak valid.")

# Menjalankan aplikasi
menu()
