import csv
import pwinput 
from prettytable import PrettyTable 
from datetime import datetime

admin = {'nama': 'Manisha', 'password': '12345'}
users = [] # list kosong untuk menyimpan objek data pengguna (User)

# Fungsi untuk menyimpan data pengguna ke dalam file CSV
def simpan_users_ke_csv():
    with open('users.csv', mode='w', newline='') as file:
        fieldnames = ['nama', 'password', 'saldo'] # untuk menulis nama kolom
        writer = csv.DictWriter(file, fieldnames=fieldnames) # objek writer
        writer.writeheader() # untuk menulis kolom header

        for user in users:  # Tulis setiap baris data pengguna ke dalam file CSV
            writer.writerow({'nama': user.nama, 'password': user.password, 'saldo': user.saldo})

# fungsi memuat daata user dari file csv
def load_users_dari_csv():
    try:
        with open('users.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(User(row['nama'], row['password'], int(row['saldo'])))
    except FileNotFoundError:
        print("File 'users.csv' tidak ditemukan. Memulai dengan data kosong.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memuat data pengguna: {e}")

def tambah_saldo(user):
    try:
        jumlah_saldo = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        if jumlah_saldo > 0:
            user.saldo += jumlah_saldo
            simpan_users_ke_csv()
            print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp. {user.saldo}\n")
        else:
            print("Inputan tidak valid, jumlah saldo harus lebih dari nol.")
    except ValueError:
        print("Inputan tidak valid, harap masukkan angka.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan saldo: {e}")


class User:
    def __init__(self, nama, password, saldo=0):
        self.nama = nama # atribut nama
        self.password = password
        self.saldo = saldo
        self.invoices = [] # list buat nyimpan objek invoice


# Definisi class Invoice yang merepresentasikan invoice untuk setiap transaksi
class Invoice:
    def __init__(self, user, code, total_jam, total_biaya):
        self.user = user
        self.code = code
        self.total_jam = total_jam
        self.total_biaya = total_biaya
        self.tanggal_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Menyimpan tanggal dan waktu transaksi


# ini Data list alat berat bisa dibaca dari file CSV atau diinisialisasi di dalam kode
List_AlatBerat = [
    {"Code": "1A", "Jenis Alat": "Crane", "Biaya Rental": "Rp. 300000/Jam", "stok Alat": 5},
    {"Code": "1B", "Jenis Alat": "Excavator", "Biaya Rental": "Rp. 100000/Jam", "stok Alat": 3},
    {"Code": "2B", "Jenis Alat": "Excavator", "Biaya Rental": "Rp. 350000/Jam", "stok Alat": 6},
    {"Code": "1C", "Jenis Alat": "Forklift", "Biaya Rental": "Rp. 150000/Jam", "stok Alat": 2},
    {"Code": "1D", "Jenis Alat": "BullDozer", "Biaya Rental": "Rp. 250000/Jam", "stok Alat": 1},
    {"Code": "2D", "Jenis Alat": "BullDozer", "Biaya Rental": "Rp. 300000/Jam", "stok Alat": 4},
    {"Code": "1E", "Jenis Alat": "Dump Truck", "Biaya Rental": "Rp. 200000/Jam", "stok Alat": 7},
    {"Code": "2E", "Jenis Alat": "Dump Truck", "Biaya Rental": "Rp. 350000/Jam", "stok Alat": 8}   
]

# Simpan data ke dalam file CSV
def dataList_AlatBerat():

    # Membuka file CSV dan menulis data alat berat ke dalamnya
    with open('List_AlatBerat.csv', 'w', newline='') as new_file:
        fieldNames = ["Code", "Jenis Alat", "Biaya Rental", "stok Alat"]
        csv_writer = csv.DictWriter(
            new_file, delimiter=',', fieldnames=fieldNames)
        csv_writer.writeheader() # tulis header

        # Tulis setiap baris data alat berat ke dalam file CSV
        for AlatBerat in List_AlatBerat:
            csv_writer.writerow(AlatBerat)
dataList_AlatBerat() # Memanggil fungsi dataList_AlatBerat untuk menyimpan data alat berat ke dalam file CSV

# Nama file CSV yang akan digunakan
file_name = 'List_AlatBerat.csv'

# Fungsi untuk membaca semua data dari file CSV
def baca_List_AlatBerat():
    data = []  # Inisialisasi list untuk menampung data dari file CSV
    try:
        with open(file_name, mode='r', newline='') as file:  # Buka file CSV
            reader = csv.DictReader(file)  # Membaca file sebagai dictionary
            for row in reader:  # Loop setiap baris data dalam file CSV
                data.append(row)  # Menambahkan setiap baris data ke dalam list data
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data alat berat: {e}")
    return data  # Mengembalikan data yang telah terbaca dari file CSV

# Fungsi untuk menambahkan data alat baru ke file CSV
def tambah_List_AlatBerat(Code, Jenis_Alat, Biaya_Rental, stok_Alat):
    try:
        with open(file_name, mode='r', newline='') as file:  # Membuka file CSV untuk pembacaan
            reader = csv.DictReader(file)  # Membaca file sebagai dictionary
            data = list(reader)  # Membuat list dari data yang terbaca


        if any(row['Code'] == Code for row in data):
            print("Code sudah ada di Data\n")
        else:
            if stok_Alat.isdigit() and int(stok_Alat) >= 0 and Biaya_Rental.replace("Rp. ", "").replace("/Jam", "").isdigit():
                with open(file_name, mode='a', newline='') as file:  # Membuka file CSV untuk menulis
                    fieldnames = ["Code", "Jenis Alat", "Biaya Rental", "stok Alat"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerow({
                        'Code': Code,
                        'Jenis Alat': Jenis_Alat,
                        'Biaya Rental': Biaya_Rental,
                        'stok Alat': stok_Alat
                    })
                print("Data Alat Berat berhasil ditambahkan.\n")
            else:
                print("Isi datanya cuk, jangan kosong\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambah data alat berat: {e}")

# Fungsi untuk memperbarui data dalam file CSV
def perbarui_List_AlatBerat():
    try:
        data = baca_List_AlatBerat()  # Membaca data alat berat dari file CSV
        code = input("Masukkan Code alat yang ingin diperbarui: ")
        alat_ditemukan = False

        for row in data:
            if row['Code'] == code:  # Mencari alat berdasarkan kode
                alat_ditemukan = True
                print("Data Alat yang ditemukan:")
                print(f"Jenis Alat: {row['Jenis Alat']}, Biaya Rental: {row['Biaya Rental']}, Stok Alat: {row['stok Alat']}")
                
                # Memperbarui informasi
                row['Jenis Alat'] = input("Masukkan jenis alat baru: ")
                row['Biaya Rental'] = input("Masukkan biaya rental baru: ")
                stok_baru = input("Masukkan stok alat baru: ")
                
                if stok_baru.isdigit() and int(stok_baru) >= 0:
                    row['stok Alat'] = stok_baru
                else:
                    print("Inputan stok tidak valid, harus berupa angka non-negatif.")
                    return

                break

        if alat_ditemukan:
            # Menyimpan data yang telah diperbarui ke file CSV
            with open(file_name, mode='w', newline='') as file:
                fieldnames = ["Code", "Jenis Alat", "Biaya Rental", "stok Alat"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # Menulis header
                writer.writerows(data)  # Menulis data yang telah diperbarui
            print("Data alat berat berhasil diperbarui.\n")
        else:
            print("Alat tidak ditemukan.\n")

    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memperbarui data alat berat: {e}")


# Fungsi untuk menghapus data dari file CSV
def hapus_List_AlatBerat():
    try:
        data = baca_List_AlatBerat()  # Membaca data alat berat dari file CSV
        code = input("Masukkan Code alat yang ingin dihapus: ")
        alat_ditemukan = False

        for row in data:
            if row['Code'] == code:  # Mencari alat berdasarkan kode
                alat_ditemukan = True
                data.remove(row)  # Menghapus alat dari daftar
                print("Alat berhasil dihapus.\n")
                break

        if alat_ditemukan:
            # Menyimpan data yang telah diperbarui ke file CSV
            with open(file_name, mode='w', newline='') as file:
                fieldnames = ["Code", "Jenis Alat", "Biaya Rental", "stok Alat"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # Menulis header
                writer.writerows(data)  # Menulis data yang telah diperbarui
        else:
            print("Alat tidak ditemukan.\n")

    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus data alat berat: {e}")

def hapus_user():
    try:
        username = input("Masukkan username yang ingin dihapus: ")
        user_ditemukan = next((u for u in users if u.nama == username), None)

        if user_ditemukan:
            users.remove(user_ditemukan)  # Menghapus user dari data
            simpan_users_ke_csv()  # Menyimpan data user ke CSV
            print(f"User  '{username}' berhasil dihapus.\n")
        else:
            print(f"User  '{username}' tidak ditemukan.\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus user: {e}")

# Login sebagai admin
def loginAdmin():
    while True: 
        logUser = input("\nMasukkan Username : ")
        logPW = pwinput.pwinput("Password : ", mask='*')

        # memeriksa username sama password
        if logUser == "Manisha" and logPW == "12345":
            while True: # Jika login berhasil, tampilkan menu utama
                print("\n================================Menu Utama Admin================================\n")
                print("Selamat Datang!")
                print("1. Lihat Daftar Alat")
                print("2. Tambah Alat")
                print("3. Update Alat")
                print("4. Hapus Alat")
                print("5. Hapus User")
                print("6. Keluar")
                pilihan = input("Pilih menu (1/2/3/4/5): ")

                if pilihan == '1':
                    print("\n===============================Lihat Data===============================\n")
                    data = baca_List_AlatBerat()
                    tabel = PrettyTable(["Code", "Jenis Alat", "Biaya Rental", "stok Alat"])
                    for row in data: # Menampilkan data menggunakan PrettyTable
                        tabel.add_row([row['Code'], row['Jenis Alat'], row['Biaya Rental'], row['stok Alat']])
                    print(tabel)

                elif pilihan == '2':
                    print("\n===============================Tambah Data===============================\n")
                    Code = input("Masukkan Code: ")
                    Jenis_Alat = input("Masukkan Jenis Alat: ")
                    Biaya_Rental = input("Masukkan Biaya Rental: ")
                    stok_Alat = (input("Masukkan Stok Alat: "))
                    data = baca_List_AlatBerat()

                    for row in data:
                        if row['Code'] == Code: # Memeriksa jika Code sudah ada di data
                            break
                    if stok_Alat.isnumeric():
                        if int(stok_Alat) < 0:
                            print("Inputan tidak valid")

                    # Memanggil fungsi tambah_List_AlatBerat dengan input yang diberikan
                    tambah_List_AlatBerat(Code, Jenis_Alat, Biaya_Rental, stok_Alat)

                elif pilihan == '3':
                    print("\n=============================== Update Data ===============================\n")
                    perbarui_List_AlatBerat()

                elif pilihan == '4':
                    print("\n=============================== Hapus Data ===============================\n")
                    hapus_List_AlatBerat()

                elif pilihan == '5':
                    print("\n=============================== Hapus User ===============================\n")
                    hapus_user()

                elif pilihan == '6':
                    return

                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.\n")
        else:
            print("Username atau Password anda salah, coba lagi\n")

# Fungsi cek_username memeriksa keberadaan username dalam file CSV
def cek_username(nama):
   
    with open('users.csv', 'r', newline='') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            if row['nama'] == nama: 
                return True
        return False 

# Fungsi untuk mendaftarkan pengguna baru
def registrasi_user():
    print("\n=====================================Registrasi=====================================\n")
    nama = input("Masukkan username anda: ")
    password = pwinput.pwinput("Masukkan password anda: ", mask='*')
    new_user = User(nama, password) # Membuat objek User baru dengan username dan password
    users.append(new_user) # Menambahkan user baru ke dalam list pengguna

    # Memeriksa keberadaan username menggunakan fungsi cek_username
    if not cek_username(nama): # Jika username belum ada, tulis username dan password ke file 'users.csv'
        with open('users.csv', 'a', newline='') as file:
            fieldnames = ['username', 'password']
            writer = csv.DictWriter(file, fieldnames=fieldnames) 
            writer.writerow({'username': nama, 'password': password}) # Menulis username dan password baru ke dalam file CSV
        print(f"Akun dengan username '{nama}' telah berhasil terdaftar.\n")
        print("\nRegistrasi Berhasil.\n")
        simpan_users_ke_csv() # Menyimpan perubahan ke dalam file CSV
    else:
        print(f"Maaf, username '{nama}' sudah digunakan. Silakan pilih username lain.\n")

load_users_dari_csv() # Memuat data pengguna dari file CSV saat aplikasi dijalankan

def login_user():
    while True:
        print("\n=====================================Login User=====================================\n")
        nama = input("Masukkan username anda: ")
        password = pwinput.pwinput("Masukkan password anda: ", mask='*')
        user = next((u for u in users if u.nama == nama and u.password == password), None)
        if user: # Jika pengguna ditemukan
            print("Login berhasil.\n")
            return user
        else:
            print("Username dan password salah. Coba lagi.\n")
            return

def melakukan_transaksi(user):
    data = baca_List_AlatBerat()
    tabel = PrettyTable(["Code", "Jenis Alat", "Biaya Rental", "stok Alat"])
    for row in data:
        tabel.add_row([row['Code'], row['Jenis Alat'], row['Biaya Rental'], row['stok Alat']])
    print(tabel)

    code = input("Masukkan Code alat yang ingin disewa: ")
    Alat = next((item for item in List_AlatBerat if item["Code"] == code), None)  # Mencari alat dengan kode yang dimasukkan

    if Alat:  # Jika alat ditemukan
        try:
            total_jam = input("Masukkan jumlah jam yang ingin disewa: ")  # Meminta pengguna untuk memasukkan jumlah jam yang ingin disewa
            if total_jam.isdigit() and int(total_jam) > 0:  # Periksa apakah input jumlah jam merupakan angka yang positif
                total_jam = int(total_jam)  # Mengubah total_jam menjadi tipe data integer
                total_biaya = int(Alat['Biaya Rental'].replace("Rp. ", "").replace("/Jam", "")) * total_jam  # Menghitung total biaya
                if user.saldo >= total_biaya and Alat['stok Alat'] >= 1:  # Jika saldo dan stok mencukupi
                    user.saldo -= total_biaya  # Mengurangi saldo pengguna
                    invoice = Invoice(user, code, total_jam, total_biaya)  # Membuat objek Invoice untuk transaksi
                    user.invoices.append(invoice)  # Menambahkan invoice ke daftar transaksi pengguna
                    Alat['stok Alat'] -= 1  # Mengurangi stok alat yang disewa
                    simpan_users_ke_csv()  # Menyimpan perubahan saldo pengguna ke file CSV
                    dataList_AlatBerat()  # Memperbarui data stok alat ke file CSV
                    print(f"Transaksi berhasil!\n")
                    print(f"Transaksi berhasil! Total biaya: Rp. {total_biaya}.\n")
                elif user.saldo < total_biaya:  # Jika saldo tidak mencukupi
                    print("Saldo tidak mencukupi.\n")  # Memberi pesan bahwa saldo tidak mencukupi
                else:  # Jika stok alat tidak mencukupi
                    print("Stok Alat tidak mencukupi.\n")  # Memberi pesan bahwa stok alat tidak mencukupi
            else:  # Jika input jumlah jam tidak valid
                print("Jumlah jam harus berupa angka dan lebih besar dari 0.\n")  # Memberi pesan bahwa jumlah jam harus berupa angka positif
        except ValueError:
            print("Inputan tidak valid, harap masukkan angka untuk jumlah jam.\n")  # Menangani kesalahan jika input bukan angka
        except Exception as e:
            print(f"Terjadi kesalahan saat melakukan transaksi: {e}")  # Menangani kesalahan umum
    else:  # Jika alat tidak ditemukan
        print("Alat tidak ditemukan.\n")  # Memberi pesan bahwa alat dengan kode yang dimasukkan tidak ditemukan


# Fungsi untuk menampilkan struk transaksi pengguna
def tampilkan_invoices(user):
    if not user.invoices:
        print("Struk tidak ditemukan.\n")
    else:
        print("Struk Anda:")
        for invoice in user.invoices:
            equipment = next((item for item in List_AlatBerat if item["Code"] == invoice.code), None)
            if equipment:
                print("=" * 50)
                print(f"\nAlat: {equipment['Jenis Alat']}")
                print(f"Total jam: {invoice.total_jam}")
                print(f"Total Biaya: Rp. {invoice.total_biaya}")
                print(f"Tanggal Transaksi: {invoice.tanggal_transaksi}")  # Tampilkan tanggal transaksi
                print("=" * 50)

def tambah_saldo(user):
    try:
        jumlah_saldo = float(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        if jumlah_saldo > 0:  # Jika jumlah saldo lebih dari nol
            user.saldo += jumlah_saldo  # Tambahkan saldo ke saldo pengguna
            simpan_users_ke_csv()  # Simpan perubahan saldo ke file CSV
            print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp. {user.saldo}\n")
        else:
            print("Inputan tidak valid, jumlah saldo harus lebih dari nol.")
    except ValueError:
        print("Inputan tidak valid, harap masukkan angka.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan saldo: {e}")

# Fungsi untuk memungkinkan pengguna memilih opsi terkait transaksi atau saldo
def pilihan_user(user):
    while True:
        print("\n================================Menu Utama User================================\n")
        print("Selamat Datang!\n")
        print("1. Mulai Transaksi")
        print("2. Lihat Struk")
        print("3. Tambah Saldo")
        print("4. Lihat Saldo")
        print("5. Kembali")
        pilih = input("Pilih (1/2/3/4/5): ")

        if pilih == "1":
            print("\n========================== Melakukan Transaksi ==========================\n")
            melakukan_transaksi(user)
        elif pilih == "2":
            print("\n========================== Lihat Transaksi ==========================\n")
            tampilkan_invoices(user)
        elif pilih == "3":
            print("\n========================== Top Up E-Money ==========================\n")
            tambah_saldo(user)
        elif pilih == "4":
            print("\n==========================Lihat Saldo==========================\n")
            print(f"Saldo Anda saat ini: Rp. {user.saldo}\n")
        elif pilih == "5":
            return
        else:
            print("Pilihan tidak valid.\n")

# Main program
def menu():
    while True:
        try:

            print("\n===================================== Sewa Alat Berat Transformer =====================================\n")
            print("1. Admin")
            print("2. User")
            print("3. Keluar")
            pilihan = input("Masukkan pilihan: ")

            if pilihan == "1":
                print("\n=====================================Admin=====================================\n")
                loginAdmin()
            elif pilihan == "2":
                print("\n===================================== Customer =====================================\n")
                while True:
                    print("1. Registrasi")
                    print("2. Login")
                    print("3. Kembali")
                    pilihan_user_login = input("Pilih (1/2/3): ")

                    if pilihan_user_login == "1":
                        registrasi_user() # Jalankan fungsi untuk registrasi user
                    elif pilihan_user_login == "2":
                        user = login_user() # Jalankan fungsi login_user() untuk login
                        if user:
                            pilihan_user(user) # Jika user berhasil login, jalankan fungsi untuk opsi user
                    elif pilihan_user_login == "3":
                        break 
                    else:
                        print("Pilihan tidak valid.\n")
            elif pilihan == "3":
                break
            else:
                print("Pilihan tidak valid. Coba lagi!\n")
        except KeyboardInterrupt:
            print("Hayoloo, jangan ganggu ganggu programnya ya!")
            break

if __name__ == "__main__":
    menu()
