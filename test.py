# Data mobil disimpan dalam list
mobil_list = [
    {"nama": "Avanza", "harga/Hari": 30000, "harga/Minggu": 1800000, "harga/Bulan": 7000000, "warna_mobil": "Silver", "bensin": "Bensin", "KM": 50000, "status": "Tersedia"},
    {"nama": "Xenia", "harga/Hari": 28000, "harga/Minggu": 1700000, "harga/Bulan": 6500000, "warna_mobil": "Merah", "bensin": "Bensin", "KM": 60000, "status": "Tersedia"},
    {"nama": "Honda Jazz", "harga/Hari": 25000, "harga/Minggu":160000 , "harga/Bulan": 700000, "warna_mobil": "Hitam", "bensin": "Bensin", "KM": 80000, "status": "Tersedia"},
    {"nama": "Kijang Innova", "harga/Hari": 50000, "harga/Minggu": 300000, "harga/Bulan":1100000, "warna_mobil": "Kuning", "bensin": "Solar", "KM": 60000, "status": "Tersedia"},
    {"nama": "Daihatsu New Terios", "harga/Hari": 40000, "harga/Minggu": 250000, "harga/Bulan": 900000, "warna_mobil": "Hitam", "bensin": "Solar", "KM": 40000, "status": "Tersedia"},
    {"nama": "Avanza", "harga/Hari": 20000, "harga/Minggu": 150000, "harga/Bulan": 550000, "warna_mobil": "Putih", "bensin": "Bensin", "KM": 100000, "status": "Tersedia"},

    ]
sewa_list = []

akun = {"admin": "admin", "user": "user"}

# Fungsi login
def login():
    print("=== LOGIN ===")
    username = input("ID: ")
    password = input("Masukkan password: ")
    if username in akun and akun[username] == password:
        print("Login berhasil!\n")
        return username
    else:
        print("Login gagal! Username atau password salah.\n")
        return None

def tampilkan_mobil():
    if not mobil_list:
        print("Tidak ada mobil yang tersedia.\n")
        return
    print("Daftar Mobil:")
    for i, mobil in enumerate(mobil_list):
        print(f"{i+1}. {mobil['nama']} - Harga: Rp {mobil['harga/Hari']} per hari, Rp {mobil['harga/Minggu']} per minggu, Rp {mobil['harga/Bulan']} per bulan - Warna: {mobil['warna_mobil']} - Bensin: {mobil['bensin']} - KM: {mobil['KM']} - Status: {mobil['status']}")
    print()

def tambah_mobil():
    nama = input("Masukkan nama mobil: ")
    harga_hari = int(input("Masukkan harga sewa per hari: "))
    harga_minggu = int(input("Masukkan harga sewa per minggu: "))
    harga_bulan = int(input("Masukkan harga sewa per bulan: "))
    warna_mobil = input("Masukkan warna mobil: ")
    bensin = input("Masukkan jenis bensin: ")
    KM = int(input("Masukkan jumlah KM: "))

    mobil_list.append({
        "nama": nama,
        "harga/Hari": harga_hari,
        "harga/Minggu": harga_minggu,
        "harga/Bulan": harga_bulan,
        "warna_mobil": warna_mobil,
        "bensin": bensin,
        "KM": KM,
        "status": "Tersedia"
    })
    print("Mobil berhasil ditambahkan!\n")

def perbarui_mobil():
    tampilkan_mobil()
    indeks = int(input("Masukkan nomor mobil yang ingin diperbarui: ")) - 1
    if 0 <= indeks < len(mobil_list):
        mobil_list[indeks]["harga/Hari"] = int(input("Masukkan harga sewa baru per hari: "))
        mobil_list[indeks]["harga/Minggu"] = int(input("Masukkan harga sewa baru per minggu: "))
        mobil_list[indeks]["harga/Bulan"] = int(input("Masukkan harga sewa baru per bulan: "))
        print("Data mobil berhasil diperbarui!\n")
    else:
        print("Nomor tidak valid!\n")

def hapus_mobil():
    tampilkan_mobil()
    indeks = int(input("Masukkan nomor mobil yang ingin dihapus: ")) - 1
    if 0 <= indeks < len(mobil_list):
        mobil_list.pop(indeks)
        print("Mobil berhasil dihapus!\n")
    else:
        print("Nomor tidak valid!\n")

def filter_mobil():
    print("\n=== FILTER MOBIL ===")
    nama = input("Masukkan nama mobil (kosongkan jika tidak ingin menyaring): ")
    warna = input("Masukkan warna mobil (kosongkan jika tidak ingin menyaring): ")
    bensin = input("Masukkan jenis bensin (kosongkan jika tidak ingin menyaring): ")
    status = "Tersedia"  # Hanya menampilkan mobil yang tersedia untuk disewa
    
    filtered_mobil = [mobil for mobil in mobil_list if
                      (not bensin or mobil['bensin'].lower() == bensin.lower()) and
                      (mobil['status'].lower() == status.lower())]
    
    if not filtered_mobil:
        print("Tidak ada mobil yang sesuai dengan filter.\n")
        return []
    
    print("Daftar Mobil yang Sesuai Filter:")
    for i, mobil in enumerate(filtered_mobil):
        print(f"{i+1}. {mobil['nama']} - Harga: Rp {mobil['harga/Hari']} per hari, Rp {mobil['harga/Minggu']} per minggu, Rp {mobil['harga/Bulan']} per bulan - Warna: {mobil['warna_mobil']} - Bensin: {mobil['bensin']} - KM: {mobil['KM']} - Status: {mobil['status']}")
    print()
    return filtered_mobil

def cetak_bon(mobil, durasi, total_harga):
    print("\n=== BON PENYEWAAN MOBIL ===")
    print(f"Nama Mobil: {mobil['nama']}")
    print(f"Warna Mobil: {mobil['warna_mobil']}")
    print(f"Jenis Bensin: {mobil['bensin']}")
    print(f"KM Mobil: {mobil['KM']}")
    print(f"Durasi Sewa: {durasi}")
    print(f"Total Harga: Rp {total_harga}")
    print("===========================\n")

def sewa_mobil():
    tampilkan_mobil()
    indeks = int(input("Masukkan nomor mobil yang ingin disewa: ")) - 1
    if 0 <= indeks < len(mobil_list) and mobil_list[indeks]["status"] == "Tersedia":
        durasi = input("Masukkan durasi sewa (Hari/Minggu/Bulan): ").capitalize()
        if durasi not in ["Hari", "Minggu", "Bulan"]:
            print("Durasi tidak valid! Harap masukkan Hari, Minggu, atau Bulan.\n")
            return
        
        # Meminta jumlah hari, minggu, atau bulan
        if durasi == "Hari":
            jumlah = int(input("Masukkan jumlah hari: "))
            total_harga = mobil_list[indeks]["harga/Hari"] * jumlah
        elif durasi == "Minggu":
            jumlah = int(input("Masukkan jumlah minggu: "))
            total_harga = mobil_list[indeks]["harga/Minggu"] * jumlah
        elif durasi == "Bulan":
            jumlah = int(input("Masukkan jumlah bulan: "))
            total_harga = mobil_list[indeks]["harga/Bulan"] * jumlah
        
        mobil = mobil_list.pop(indeks)  # Hapus mobil dari daftar mobil tersedia
        mobil["status"] = "Disewa"
        sewa_list.append(mobil)  # Tambahkan mobil ke daftar sewa
        print(f"🚗 Mobil {mobil['nama']} berhasil disewa untuk {jumlah} {durasi}!\n")
        cetak_bon(mobil, f"{jumlah} {durasi}", total_harga)
    else:
        print("Nomor tidak valid atau mobil sudah disewa!\n")
        
def sewa_mobil():
    filtered_mobil = filter_mobil()
    if not filtered_mobil:
        return
    
    indeks = int(input("Masukkan nomor mobil yang ingin disewa: ")) - 1
    if 0 <= indeks < len(filtered_mobil):
        mobil = filtered_mobil[indeks]
        durasi = input("Masukkan durasi sewa (Hari/Minggu/Bulan): ").capitalize()
        if durasi not in ["Hari", "Minggu", "Bulan"]:
            print("Durasi tidak valid! Harap masukkan Hari, Minggu, atau Bulan.\n")
            return
        
        if durasi == "Hari":
            jumlah = int(input("Masukkan jumlah hari: "))
            total_harga = mobil["harga/Hari"] * jumlah
        elif durasi == "Minggu":
            jumlah = int(input("Masukkan jumlah minggu: "))
            total_harga = mobil["harga/Minggu"] * jumlah
        elif durasi == "Bulan":
            jumlah = int(input("Masukkan jumlah bulan: "))
            total_harga = mobil["harga/Bulan"] * jumlah
        
        mobil_list.remove(mobil)  # Hapus mobil dari daftar mobil tersedia
        mobil["status"] = "Disewa"
        sewa_list.append(mobil)  # Tambahkan mobil ke daftar sewa
        print(f"🚗 Mobil {mobil['nama']} berhasil disewa untuk {jumlah} {durasi}!\n")
        cetak_bon(mobil, f"{jumlah} {durasi}", total_harga)
    else:
        print("Nomor tidak valid atau mobil sudah disewa!\n")

def menu():
    user = None
    while user is None:
        user = login()
    
    while True:
        print("\n=== RENTAL MOBIL ===")
        if user == "admin":
            print("1. Tambah Mobil")
            print("2. Perbarui Mobil")
            print("3. Hapus Mobil")
            print("4. Tampilkan Mobil")
            print("5. Keluar")
        elif user == "user":
            print("1. Tampilkan Mobil")
            print("2. Sewa Mobil")
            print("3. Kembalikan Mobil")
            print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if user == "admin":
            if pilihan == "1":
                tambah_mobil()
            elif pilihan == "2":
                perbarui_mobil()
            elif pilihan == "3":
                hapus_mobil()
            elif pilihan == "4":
                tampilkan_mobil()
            elif pilihan == "5":
                print("Terima kasih! Keluar dari program.")
                break
        elif user == "user":
            if pilihan == "1":
                tampilkan_mobil()
            elif pilihan == "2":
                sewa_mobil()
            elif pilihan == "3":
                kembalikan_mobil()
            elif pilihan == "4":
                print("Terima kasih! Keluar dari program.")
                break
menu()
