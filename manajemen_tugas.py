import json
import os   

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def simpan(tugas):
    with open('data_tugas.json', 'w') as file:
        json.dump(tugas, file)  

def baca():
    try:
        with open('data_tugas.json', 'r') as file:
            tugas = json.load(file)
    except FileNotFoundError:
        tugas = []
    return tugas

def tampil():
    tugas = baca()
    if tugas:
        print("Daftar Tugas:")
        print("+----+------------------------------------------+------------------+")
        print("| No | Tugas                                    | Deadline         |")
        print("+----+------------------------------------------+------------------+")
        for idx, t in enumerate(tugas, start=1):
            print("| {:<2} | {:<40} | {:<16} |".format(idx, t["tugas"], t["deadline"]))
        print("+----+------------------------------------------+------------------+")
    else:
        clear()
        print("Belum ada tugas yang tersimpan.")

def tambah():
    tugas = baca()
    tugas_baru = input("Masukkan tugas baru: ")
    deadline = input("Masukkan tanggal deadline: ")
    tugas.append({"tugas": tugas_baru, "deadline": deadline})
    simpan(tugas)
    print("Tugas berhasil ditambahkan.")

def edit():
    tugas = baca()
    if tugas:
        tampil()
        indeks_tugas = int(input("\nPilih nomor tugas yang akan diperbarui: ")) - 1
        if 0 <= indeks_tugas < len(tugas):
            tugas_baru = input("Masukkan tugas yang diperbarui: ")
            deadline_baru = input("Masukkan tanggal deadline baru: ")
            tugas[indeks_tugas] = {"tugas": tugas_baru, "deadline": deadline_baru}
            simpan(tugas)
            print("Tugas berhasil diperbarui.")
        else:
            print("Nomor tugas tidak valid.")
    else:
        clear()
        print("Belum ada tugas yang tersimpan.")

def hapus():
    tugas = baca()
    if tugas:
        clear()
        tampil()
        indeks_tugas = int(input("\nPilih nomor tugas yang akan dihapus: ")) - 1
        if 0 <= indeks_tugas < len(tugas):
            tugas.pop(indeks_tugas)
            simpan(tugas)
            print("Tugas berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    else:
        clear()
        print("Belum ada tugas yang tersimpan.")

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
            tampil()
        elif pilihan == '2':
            clear()
            tambah()
        elif pilihan == '3':
            clear()
            edit()
        elif pilihan == '4':
            hapus()
        elif pilihan == '0':
            break
        else:
            clear()
            print("Pilihan tidak valid.")

menu()
