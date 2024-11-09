# Proyek Akhir Dasar Pemograman
# Sistem-Penyewaan-Alat-Berat
Nama : Syawe Manisha P. Siregar,    NIM : 2409116058

Nama : Nayla Lelyanggraheni Hutomo,    NIM : 2409116061

Nama : Elmy Fadillah,    NIM : 2409116075

# Flowchart
![Flowchart PA-Menu Utama drawio](https://github.com/user-attachments/assets/53728b90-450f-4911-9802-ceb42fb77a18)


![Flowchart PA-menu admin drawio](https://github.com/user-attachments/assets/72f62767-4f0e-44ca-b05f-427fbb318653)

![Flowchart PA-Menu User drawio](https://github.com/user-attachments/assets/40937d2f-96f6-4688-9446-d149271a86aa)



# Input Program
![image](https://github.com/user-attachments/assets/ac2a333b-6147-436b-9169-d304a6449ddb)

=> CSV digunakan untuk membaca dan menulis data dalam format csv yang digunakan untuk menyimpan data.

=> Pwinput digunakan untuk menyembunyikan password pengguna yang berfungsi untuk menjaga keamanan dan informasi sensitif pengguna.

=> Prettytable digunakan untuk menampilkan data dalam tabel sehingga data tertata rapi.

=> Datetime digunakan untuk menampilkan tanggal dan waktu saat ini.

![image](https://github.com/user-attachments/assets/0bc6b82b-81fd-4454-b981-57288e5028c7)

=> Program diatas digunakan untuk menyimpan data admin dan user ke dalam dictionary. Untuk dictionary data admin sudah memiliki data yang pasti, sehingga saat menjalankan program harus menggunakan data yang telah ditetapkan. Sedangkan program untuk user adalah data kosong, sehingga kita dapat bebas untuk mengisi datanya tanpa ada ketentuan harus menggunakan data yang telah ditentukan.

![image](https://github.com/user-attachments/assets/cfe62e97-795d-403a-a015-6fe703b317cb)

=> Program diatas berfungsi untuk menyimpan data pengguna ke dalam file CSV. Variabel fieldnames digunakan untuk menulis nama kolom dan sebagai objek writer. lalu fungsi writerheader digunakan untyk menulis kolom header.

![image](https://github.com/user-attachments/assets/ec444381-8786-4300-8ebc-d858a837c2a3)

=> Program diatas berfungsi untuk memuat data user dari file CSV. Penggunaan fungsi with open yaitu untuk membuka file csv dalam mode baca 'r'  sedangkan fungsi newline digunakan untuk menangani baris baru secara konsisten. Fungsi csv.DictReader(file) digunakan untuk membaca file CSV dan mengonversi setiap baris menjadi kamus (dictionary) di mana nama kolom menjadi kunci. Dalam loop fungsi for row in reader, dictionary diambil dan digunakan untuk membuat objek User  dengan atribut nama, password, dan saldo. Objek ini kemudian ditambahkan ke dalam list users. Fungsi FileNotFoundError digunakan jika file users.csv tidak ditemukan, program akan mencetak pesan yang menyatakan bahwa file tidak ada dan memulai dengan data kosong.

![image](https://github.com/user-attachments/assets/5ad87c67-263b-497f-a006-2d3bda87eb61)

=> Fungsi tambah saldo digunakan untuk menambahkan saldo ke akun user. Fungsi ini didefinisikan dengan nama tambah_saldo dan menerima satu parameter yaitu user.Fungsi variabel jumlah_saldo yaitu untuk meminta pengguna untuk memasukkan jumlah saldo yang ingin ditambahkan. Input ini kemudian diubah menjadi integer. Fungsi if pada program yaitu untuk memeriksa apakah jumlah saldo yang dimasukkan lebih besar dari nol. Fungsi simpan_users_ke_csv() dipanggil untuk menyimpan perubahan saldo ke dalam file CSV . Fungsi ValueError digunakan jika pengguna memasukkan nilai yang tidak dapat diubah menjadi integer (misalnya, huruf atau simbol), program akan menangkap kesalahan ini dan mencetak pesan yang sesuai. Fungsi Exception as e digunakan untuk menangani kesalahan lain yang mungkin terjadi saat menambahkan saldo, program mencetak pesan kesalahan yang spesifik.

![image](https://github.com/user-attachments/assets/bbaa6030-7c42-4abe-af13-b9b9034657d6)

=> Fungsi Class User digunakan untuk merepresentasikan pengguna dalam sistem. Fungsi __init__ Method adalah metode konstruktor yang dipanggil ketika objek dari kelas User dibuat. Parameternya yaitu nama (nama user), password, saldo (Saldo pengguna, dengan nilai bawaan 0 jika tidak diberikan). Atributnya yaitu self.nama, self.password, self.saldo, self.invoice yang digunakan untuk menyimpan masing masing data. Fungsi Class digunakan untuk mempresentasikan invoice untuk setiap transaksi yang dilakukan oleh pengguna. Parameternya yaitu user (Objek User  yang terkait dengan invoice ini), code yaitu Kode unik untuk invoice ini, total_jam yaitu Total jam yang digunakan dalam transaksi, total_biaya yaitu Total biaya yang harus dibayar untuk transaksi tersebut. Atributnya yaitu self.user yang digunakan untuk menyimpan referensi ke objek User  yang terkait dengan invoice ini, self.code yang digunakan untuk menyimpan kode invoice, self.total_jam yang digunakan untuk menyimpan total jam yang digunakan dalam transaksi, self.total_biaya yang digunakan untuk menyimpan total biaya dari transaksi, self.tanggal_transaksi yang digunakan untuk menyimpan tanggal dan waktu transaksi saat invoice dibuat. Ini menggunakan datetime.now() untuk mendapatkan waktu saat ini dan memformatnya menjadi string

![image](https://github.com/user-attachments/assets/d752106b-1a03-4488-8b96-f5558faff8e1)

=> Program diatas merupakan dictionary alat yang ditawarkan, data list alat berat bisa dibaca dari file CSV atau diinisialisasi di dalam kode.

![image](https://github.com/user-attachments/assets/41ab63b7-6f1a-49bb-ace0-64454ee51644)

=> Program diatas berfungsi untuk menyimpan dataList_AlatBerat ke dalam file CSV. Fungsi with open yaitu untuk membuka file CSV dan menulis data alat berat ke dalamnya. Variabel fieldnames digunakan untuk menulis nama kolom dan sebagai objek writer. lalu fungsi writerheader digunakan untyk menulis kolom header. fungsi for adalah melakukan perulangan yang memiliki batas sedangkan writerow berfungsi untuk menulis setiap baris data alat berat ke dalam file CSV. Fungsi dataList_AlatBerat() digunakan untuk memanggil fungsi dataList_AlatBerat untuk menyimpan data alat berat ke dalam file CSV.
Variabel file_name merupakan nama file CSV yang akan digunakan.

![image](https://github.com/user-attachments/assets/d2f3a783-8b8f-4b42-8dcd-c575bc084318)

=> Program diatas berfungsi untuk membaca semua data dari file CSV. Variabel data digunakan sebagai inisialisasi list untuk menampung data dari file CSV. Fungsi with open digunakan untuk membuka file CSV, variabel reader digunakan untuk membaca file sebagai dictionary, Fungsi for row in reader digunakan untuk loop setiap baris data dalam file CSV, sedangkan data.append(row) digunakan untuk menambahkan setiap baris data ke dalam list data. Fungsi return yaitu untuk mengembalikan data yang telah terbaca dari file csv .

![image](https://github.com/user-attachments/assets/58066e1f-7f8c-42c8-9ac6-6ef7ef86fda6)

=> Program diatas berfungsi untuk menambahkan data alat baru ke file CSV. Fitur yang lain kurang lebih sama dengan yang dijelaskan sebelumnya.

![image](https://github.com/user-attachments/assets/bfb1a5c1-3ec3-4252-839d-e54dbf33a7b2)

![image](https://github.com/user-attachments/assets/680fb62c-4eb8-4a79-be66-f2a4f4b0b157)

=> Program diatas berfungsi untuk memperbarui data dalam file CSV. Fungsi variabel data ini memanggil baca_List_AlatBerat() untuk membaca data alat berat yang tersimpan dalam file CSV. Data ini akan disimpan dalam variabel data, yang berupa list dari dictionary, di mana setiap dictionary merepresentasikan satu alat berat. Fungsi variabel code yaitu user diminta untuk memasukkan kode alat yang ingin diperbarui yang akan digunakan untuk mencari alat yang relevan dalam data. Fungsi variabel alat_ditemukan berfungsi untuk melakukan iterasi melalui setiap baris dalam data untuk mencari alat yang memiliki kode yang sesuai. Jika ditemukan, variabel alat_ditemukan diatur ke True, dan informasi mengenai alat tersebut ditampilkan. Jika alat ditemukan, program menampilkan informasi saat ini dari alat seperti gambar dibawah ini

![image](https://github.com/user-attachments/assets/bf33b9c2-1897-469d-8175-85b476b7d5ac)

=> Kemudian, pengguna diminta untuk memasukkan informasi baru dengan program dibawah ini

![image](https://github.com/user-attachments/assets/a9fcfc44-f3b4-4879-8aa9-054082d83463)

=> Untuk stok, program memeriksa apakah input adalah angka non-negatif dengan program dibawah ini

![image](https://github.com/user-attachments/assets/8bb93e4b-2059-4c86-ba1f-b79513918b75)

=> Jika alat ditemukan dan informasi diperbarui, data yang telah diperbarui disimpan kembali ke file CSV menggunakan program di bawah ini

![image](https://github.com/user-attachments/assets/9839db54-5427-434d-93be-f3f1a3bf990d)

=> Dalam program ini, file dibuka dalam mode tulis ('w'), yang akan menghapus konten lama dan menulis konten baru. Header ditulis kembali, diikuti dengan data yang telah diperbarui.

![image](https://github.com/user-attachments/assets/ca0607a4-17b0-42ac-aa23-4f624693c311)

=> Program diatas berfungsi untuk menghapus data dari file CSV. Fungsi Fitur lainnya kurang lebih sama dengan fungsi fitur yang telah di jelaskan sebelumnya.

![image](https://github.com/user-attachments/assets/fb7e5277-e9fa-4249-a07d-2f2b6bb7db44)

=> Program diatas berfungsi untuk menghapus user dari file CSV. jika user terdapat pada file csv maka program dapat menghapus user dengan fungsi users.remove dan akan mencetak user 'username' berhasil dihapus. dan jika program tidak menemukan user maka program akan mencetak Use 'username' tidak ditemukan. jika terjadi error maka fungsi except akan mencetak terjadi kesalahan saat menghapus user.

![image](https://github.com/user-attachments/assets/94d57072-6b77-40ce-b961-ff277eeaf3fe)

=> Program diatas merupakam Fitur menu login admin. variabel loguser bermaksud agar memasukkan username admin dan logpw adalah melakukan input password admin. Fungsi pwinput adalah menyembunyikan karakter password. fungsi if adalah jika username dan password admin sesuai maka program akan menampilkan menu admin.

![image](https://github.com/user-attachments/assets/0fd669a1-9b8f-4c7c-83f8-628979ef02d3)

=> jika memilih '1' maka program akan menampilkan data menggunakan prettytable

![image](https://github.com/user-attachments/assets/c14ccba4-daaf-4e32-a444-9fdd8cb9fbe9)

=> jika memilih '2' maka program akan menjalankan fungsi untuk menginput data agar admin dapat menambahkan alat

![image](https://github.com/user-attachments/assets/029571df-80f9-4869-b0cf-8e63ee0a05c2)

=> Program diatas digunakan untuk memeriksa apakah kode sudah ada di data. Sedangkan fungsi tambah_List_AlatBerat digunakan untuk memanggil fungsi dengan input yang diberikan.

![image](https://github.com/user-attachments/assets/3eb8f824-c3be-4d9c-9c9b-cfc9d5c86ca0)

=> Jika memilih '3' maka program akan memanggil fungsi perbarui_List_AlatBerat.

![image](https://github.com/user-attachments/assets/94aaca54-44a7-4a1b-aea4-3b93e0c71e03)

=> Jika memilih '6' maka program akan memanggil fungsi hapus_List_AlatBerat.

![image](https://github.com/user-attachments/assets/a93398be-fa50-45e9-8558-f941da440ae4)

=> Jika memilih '5' maka program akan memanggil fungsi hapus_user.

![image](https://github.com/user-attachments/assets/852ad115-4bc3-414f-a8b4-f8f53f80426d)

=> Jika memilih '6' maka program akan kembali ke menu pilih role (menu utama)

![image](https://github.com/user-attachments/assets/6e10252f-e39c-443c-a46e-425fbbab109d)

=> jika data tidak valid maka program akan mencetak "pilihan tidak valid. Silahkan pilih lagi". Jika username atau password salah maka program akan mencetak " username atau password salah, coba lagi."







