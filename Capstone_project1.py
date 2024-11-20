# Data dari toko rental
data_rental = [
    {
        "id_mobil": 101,
        "tipe_mobil": "Mustang",
        "harga_sewa": "Rp 500,000",
        "id_pelanggan": "10011",
        "nama_pelanggan": "Budi Susanto"
    },
    {
        "id_mobil": 102,
        "tipe_mobil": "Avanza",
        "harga_sewa": "Rp 400,000",
        "id_pelanggan": "10012",
        "nama_pelanggan": "Juju Suherman"
    },
     {
        "id_mobil": 103,
        "tipe_mobil": "Kijang",
        "harga_sewa": "Rp 300,000",
        "id_pelanggan": "10013",
        "nama_pelanggan": "Sasa Karimah"
    }
]

# Fungsi untuk Validasi agar tidak terjadi kesalahan dalam menginput
def validasi_id(value):
    return value.isdigit() and len(value) == 3

def validasi_nama(value):
    return value.replace(" ", "").isalpha()

def validasi_harga(value):
    return value.isdigit()

def validasi_idpelanggan(value):
    return value.isdigit() and len(value) == 5

def nama_kapital(value):
    return " ".join([n.capitalize() for n in value.split()])

# Untuk menambah data 
def tambah_data():
    while True:
        print("\nSubmenu Tambah Data Rental:")
        print("1. Tambah Data")
        print("2. Kembali ke Menu Utama")
        
        pilih_submenu = input("Pilih submenu: ")
        
        if pilih_submenu == "1":
            id_mobil = input("Masukkan ID Mobil (harus 3 angka): ")
            if not validasi_id(id_mobil):
                print("ID Mobil harus 3 angka, silahkan masukkan angka kembali!")
                continue  

            # Untuk mengetahui mobil sudah dirental
            for rental in data_rental:
                if rental['id_mobil'] == int(id_mobil):
                    print("Mobil ini sudah disewa dan tidak dapat disewa kembali!")
                    continue  

            tipe_mobil = input("Masukkan Tipe Mobil (hanya huruf): ")
            if not validasi_nama(tipe_mobil):
                print("Tipe Mobil hanya boleh berisi huruf!")
                continue  

            harga_sewa = input("Masukkan Harga Sewa per Hari (hanya angka): ")
            if not validasi_harga(harga_sewa):
                print("Harga sewa harus berupa angka!")
                continue  

            id_pelanggan = input("Masukkan Nomor ID Pelanggan (5 digit): ")
            if not validasi_idpelanggan(id_pelanggan):
                print("Nomor KTP harus 5 digit angka!")
                continue  

            nama_pelanggan = input("Masukkan Nama Pelanggan (Nama Depan dan Belakang): ")
            if not validasi_nama(nama_pelanggan):
                print("Nama Pelanggan hanya boleh berisi huruf!")
                continue  

            confirm = input("Apakah Anda yakin ingin menambah data ini? (Y/T): ").upper()
            if confirm == 'Y':
                data_rental.append({
                    "id_mobil": int(id_mobil),
                    "tipe_mobil": tipe_mobil.capitalize(),
                    "harga_sewa": f"Rp {int(harga_sewa):,}",
                    "id_pelanggan": id_pelanggan,
                    "nama_pelanggan": nama_kapital(nama_pelanggan)
                })
                print("Data rental berhasil ditambahkan!")
                break  # Kembali ke menu utama setelah sukses
            else:
                print("Gagal menambahkan data, kembali ke submenu.")
        
        elif pilih_submenu == "2":
            break  # Kembali ke menu utama
        
        else:
            print("Pilihan tidak valid, coba lagi.")

# Melihat Data Rental
def lihat_data():
    if not data_rental:
        print("Tidak ada data rental!")
        return

    print("\nData Rental Mobil:")
    print(f"{'ID Mobil':<10}{'Tipe Mobil':<15}{'Harga Sewa':<15}{'ID Pelanggan':<20}{'Nama Pelanggan':<20}")
    print("=" * 80)
    for rental in data_rental:
        print(f"{rental['id_mobil']:<10}{rental['tipe_mobil']:<15}{rental['harga_sewa']:<15}{rental['id_pelanggan']:<20}{rental['nama_pelanggan']:<20}")

# Menghapus data rental
def hapus_data():
    while True:
        print("\nSubmenu Hapus Data Rental:")
        print("1. Hapus Data")
        print("2. Kembali ke Menu Utama")
        
        pilihan_submenu = input("Pilih submenu: ")
        
        if pilihan_submenu == "1":
            if not data_rental:
                print("Tidak ada data untuk dihapus!")
                continue  

            id_mobil = input("Masukkan ID Mobil yang ingin dihapus: ")
            if not validasi_id(id_mobil):
                print("ID Mobil harus berupa angka!")
                continue  

            for rental in data_rental:
                if rental["id_mobil"] == int(id_mobil):
                    konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (Y/T): ").upper()
                    if konfirmasi == 'Y':
                        data_rental.remove(rental)
                        print(f"Data rental dengan ID Mobil {id_mobil} berhasil dihapus!")
                        break  
                    else:
                        print("Kembali ke submenu.")
                        break
            else:
                print(f"Data rental dengan ID Mobil {id_mobil} tidak ditemukan.")
        
        elif pilihan_submenu == "2":
            break  
        
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menambahkan data rental baru
def update_data():
    while True:
        print("\nSubmenu Update Data Rental:")
        print("1. Update Data")
        print("2. Kembali ke Menu Utama")
        
        pilihan_submenu = input("Pilih submenu: ")
        
        if pilihan_submenu == "1":
            if not data_rental:
                print("Tidak ada data untuk diperbarui!")
                continue  

            id_mobil = input("Masukkan ID Mobil yang ingin diperbarui: ")
            if not validasi_id(id_mobil):
                print("ID Mobil harus berupa angka!")
                continue  

            for rental in data_rental:
                if rental["id_mobil"] == int(id_mobil):
                    print("\nData yang ditemukan:")
                    print(f"ID Mobil: {rental['id_mobil']}")
                    print(f"Tipe Mobil: {rental['tipe_mobil']}")
                    print(f"Harga Sewa: {rental['harga_sewa']}")
                    print(f"ID Pelanggan: {rental['id_pelanggan']}")
                    print(f"Nama Pelanggan: {rental['nama_pelanggan']}")

                    print("\nMasukkan data baru (kosongkan untuk tidak mengubah):")
                    tipe_mobil = input("Tipe Mobil (hanya huruf): ")
                    if tipe_mobil:
                        if validasi_nama(tipe_mobil):
                            rental["tipe_mobil"] = tipe_mobil.capitalize()
                        else:
                            print("Tipe Mobil tidak valid!")

                    harga_sewa = input("Harga Sewa per Hari (hanya angka): ")
                    if harga_sewa:
                        if validasi_harga(harga_sewa):
                            rental["harga_sewa"] = f"Rp {int(harga_sewa):,}"
                        else:
                            print("Harga sewa tidak valid!")

                    id_baru = input("Nomor ID Pelanggan (5 digit): ")
                    if id_baru:
                        if validasi_idpelanggan(id_baru):
                            rental["id_pelanggan"] = id_baru
                        else:
                            print("Nomor ID tidak valid!")

                    nama_baru = input("Nama Pelanggan (Nama Depan dan Belakang): ")
                    if nama_baru:
                        if validasi_nama(nama_baru):
                            rental["nama_pelanggan"] = nama_kapital(nama_baru)
                        else:
                            print("Nama pelanggan tidak valid!")

                    konfirmasi = input("Apakah Anda yakin ingin memperbarui data ini? (Y/T): ").upper()
                    if konfirmasi == 'Y':
                        print("Data rental berhasil diperbarui!")
                        break  
                    elif konfirmasi == 'T':
                        print("Perubahan dibatalkan, kembali ke submenu.")
                        break
                    else:
                        print("Pilihan tidak valid, kembali ke submenu.")
        
        elif pilihan_submenu == "2":
            break  
        
        else:
            print("Pilihan tidak valid, coba lagi.")

# Main Menu
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Rental")
        print("2. Lihat Data Rental")
        print("3. Hapus Data Rental")
        print("4. Update Data Rental")
        print("5. Keluar")

        choice = input("Pilih menu: ")
        if choice == "1":
            tambah_data()
        elif choice == "2":
            lihat_data()
        elif choice == "3":
            hapus_data()
        elif choice == "4":
            update_data()
        elif choice == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
