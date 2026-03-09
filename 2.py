"""
Student Manager App
Login + CRUD system (simple console app)
"""

username_benar = "admin"
password_benar = "123"
data_siswa = []


def login():
  """Prompt until correct username/password."""
  print("=== LOGIN SISTEM ===")
  while True:
    user = input("Username: ").strip()
    pw = input("Password: ").strip()
    if user == username_benar and pw == password_benar:
      print("Login berhasil!\n")
      return
    else:
      print("Username atau password salah!\n")


def tambah_data():
  nama = input("Nama siswa: ").strip()
  kelas = input("Kelas: ").strip()
  siswa = {"nama": nama, "kelas": kelas}
  data_siswa.append(siswa)
  print("Data berhasil ditambahkan!")


def lihat_data():
  if len(data_siswa) == 0:
    print("Belum ada data.")
    return
  print("\n=== DATA SISWA ===")
  for i, s in enumerate(data_siswa, start=1):
    print(f"{i}. {s['nama']} - {s['kelas']}")


def edit_data():
  lihat_data()
  if len(data_siswa) == 0:
    return
  try:
    nomor = int(input("Pilih nomor data: ")) - 1
  except ValueError:
    print("Input tidak valid.")
    return
  if 0 <= nomor < len(data_siswa):
    nama = input("Nama baru (kosong = tidak diubah): ").strip()
    kelas = input("Kelas baru (kosong = tidak diubah): ").strip()
    if nama:
      data_siswa[nomor]["nama"] = nama
    if kelas:
      data_siswa[nomor]["kelas"] = kelas
    print("Data berhasil diupdate!")
  else:
    print("Nomor tidak ditemukan.")


def hapus_data():
  lihat_data()
  if len(data_siswa) == 0:
    return
  try:
    nomor = int(input("Pilih nomor yang dihapus: ")) - 1
  except ValueError:
    print("Input tidak valid.")
    return
  if 0 <= nomor < len(data_siswa):
    data_siswa.pop(nomor)
    print("Data berhasil dihapus!")
  else:
    print("Nomor tidak ditemukan.")


def menu():
  while True:
    print("\n===== MENU UTAMA =====")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Logout / Keluar")
    pilih = input("Pilih menu: ").strip()
    if pilih == "1":
      tambah_data()
    elif pilih == "2":
      lihat_data()
    elif pilih == "3":
      edit_data()
    elif pilih == "4":
      hapus_data()
    elif pilih == "5":
      print("Logout berhasil.")
      break
    else:
      print("Menu tidak tersedia!")


if __name__ == "__main__":
  login()
  menu()
  print("Program selesai.")