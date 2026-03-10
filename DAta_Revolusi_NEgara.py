    
    #========================================#
#SISTEM List Data Langkah langkah Revolusi Negara#
    #========================================#

import time

Username = "Pemoeda NoeSantara"
PASSWORD = "revolusi123 ganti rezim mboto ini!"

# ===== DATABASE DATA =====
data_revolusi = []


#================================#
# Function Login RE-Login
#================================#
def RE_login():
    attemps = 0
    max_attempts = 5
    
    while attemps < max_attempts:
        print("===== LOGIN SISTEM =====")
        username = input("Username: ")
        password = input("Password: ")

        if username == Username and password == PASSWORD:
            print("Login berhasil!\n")
            return True
        else:
            attemps += 1
            print(f"Login gagal! Sisa percobaan: {max_attempts - attemps}\n")
            time.sleep(1)  # Tambahkan delay untuk keamanan
            
        if attemps >= max_attempts:
            print("Anda telah mencapai batas percobaan login. Program berhenti.")  
            return False
    #Execute RE-Login
    RE_login()
    
if not RE_login():
    exit()  # Keluar dari program jika login gagal setelah 5 percobaan login
          

# =====================================
# TAMBAH DATA REVOLUSI
# =====================================
def tambah_data():
    print("\n=== Tambah Data Revolusi ===")
    negara = input("Nama Negara: ")
    tahun = input("Tahun Revolusi: ")
    fase = input("Fase/Langkah Revolusi: ")
    deskripsi = input("Deskripsi Singkat: ")

    data = {
        "negara": negara,
        "tahun": tahun,
        "fase": fase,
        "deskripsi": deskripsi
    }

    data_revolusi.append(data)
    print("Data berhasil ditambahkan!\n")


# =====================================
# LIHAT SEMUA DATA
# =====================================
def lihat_data():
    print("\n=== Daftar Data Revolusi ===")
    if len(data_revolusi) == 0:
        print("Belum ada data.\n")
    else:
        for i, data in enumerate(data_revolusi):
            print(f"{i+1}. {data['negara']} ({data['tahun']})")
            print(f"   Fase: {data['fase']}")
            print(f"   Deskripsi: {data['deskripsi']}\n")


# =====================================
# UPDATE DATA
# =====================================
def update_data():
    lihat_data()
    if len(data_revolusi) == 0:
        return

    index = int(input("Pilih nomor data yang ingin diupdate: ")) - 1

    if 0 <= index < len(data_revolusi):
        data_revolusi[index]['negara'] = input("Nama Negara baru: ")
        data_revolusi[index]['tahun'] = input("Tahun baru: ")
        data_revolusi[index]['fase'] = input("Fase baru: ")
        data_revolusi[index]['deskripsi'] = input("Deskripsi baru: ")
        print("Data berhasil diupdate!\n")
    else:
        print("Nomor tidak valid!\n")


# =====================================
# HAPUS DATA
# =====================================
def hapus_data():
    lihat_data()
    if len(data_revolusi) == 0:
        return

    index = int(input("Pilih nomor data yang ingin dihapus: ")) - 1

    if 0 <= index < len(data_revolusi):
        data_revolusi.pop(index)
        print("Data berhasil dihapus!\n")
    else:
        print("Nomor tidak valid!\n")


# =====================================
# CARI DATA BERDASARKAN NEGARA
# =====================================
def cari_data():
    print("\n=== Cari Data Berdasarkan Negara ===")
    cari = input("Masukkan nama negara: ")

    ditemukan = False
    for data in data_revolusi:
        if data['negara'].lower() == cari.lower():
            print(f"{data['negara']} ({data['tahun']})")
            print(f"Fase: {data['fase']}")
            print(f"Deskripsi: {data['deskripsi']}\n")
            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.\n")


# =====================================
# MENU UTAMA
# =====================================
def menu():
    while True:
        print("===== MENU UTAMA =====")
        print("Input harus angka!")
        print("0. Login Ulang")
        print("1. Tambah Data Revolusi")
        print("2. Lihat Semua Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        print("6. Logout/keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            cari_data()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid!\n")


# =====================================
# PROGRAM UTAMA
# =====================================
if RE_login():
    menu()
else:
    print("Program berhenti.")

