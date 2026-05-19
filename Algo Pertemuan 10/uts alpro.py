# ================================
# SISTEM CAFE SEDERHANA
# ================================

# Variabel Global
pesanan = []
total_harga = 0
nama_pelanggan = ""
tipe_pesanan = ""
wishlist = []  # List of tuple (nama_item, harga)

# =====================================
# AUFA
# INPUT NAMA DAN TAKEAWAY / DINE IN
# =====================================

def input_pelanggan():
    global nama_pelanggan
    global tipe_pesanan

    print("===== SELAMAT DATANG DI CAFE =====")

    nama_pelanggan = input("Masukkan Nama Pelanggan: ")

    print("\nPilih Tipe Pesanan:")
    print("1. Takeaway")
    print("2. Dine In")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        tipe_pesanan = "Takeaway"

    elif pilihan == "2":
        tipe_pesanan = "Dine In"

    else:
        print("Pilihan tidak valid, program dihentikan.")
        exit()

# =====================================
# FUNGSI BANTU UNTUK PESANAN & WISHLIST
# =====================================

def tambah_ke_pesanan(nama_item, harga):
    """Tambahkan item langsung ke pesanan utama."""
    global total_harga
    pesanan.append(nama_item)
    total_harga += harga
    print(f"{nama_item} ditambahkan ke pesanan.")

def tambah_ke_wishlist(nama_item, harga):
    """Tambahkan item ke wishlist."""
    wishlist.append((nama_item, harga))
    print(f"{nama_item} ditambahkan ke wishlist.")

def lihat_wishlist():
    """Tampilkan isi wishlist."""
    if not wishlist:
        print("\nWishlist kosong.")
        return
    print("\n===== WISHLIST =====")
    for idx, (item, harga) in enumerate(wishlist, start=1):
        print(f"{idx}. {item} - {harga}")
    return wishlist

def pindah_dari_wishlist():
    """Pindahkan item dari wishlist ke pesanan utama."""
    if not wishlist:
        print("Wishlist kosong. Tidak ada yang bisa dipindah.")
        return
    lihat_wishlist()
    try:
        pilihan = int(input("Masukkan nomor item yang ingin dipesan (0 untuk batal): "))
        if pilihan == 0:
            print("Pembatalan.")
            return
        if 1 <= pilihan <= len(wishlist):
            item, harga = wishlist.pop(pilihan - 1)
            tambah_ke_pesanan(item, harga)
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang benar.")

# =====================================
# ABIE
# MENU MAKANAN, DESSERT, CEMILAN
# =====================================

def menu_makanan():
    print("\n===== MENU MAKANAN =====")
    print("1. Nasi Goreng - 15000")
    print("2. Mie Goreng - 14000")

    pilihan = input("Pilih makanan: ")

    if pilihan == "1":
        nama = "Nasi Goreng"
        harga = 15000
    elif pilihan == "2":
        nama = "Mie Goreng"
        harga = 14000
    if pilihan == "3":
        nama = "Beef Aussie Rice Bowl"
        harga = 45000
    elif pilihan == "4":
        nama = "Chicken Steak Crispy"
        harga = 38500
    if pilihan == "5":
        nama = "Salmon Mentai Rice"
        harga = 63000
    elif pilihan == "6":
        nama = "Salmon Mentai rice"
        harga = 29000
    if pilihan == "7":
        nama = "Nasi Telur Dadar"
        harga = 10000
    elif pilihan == "8":
        nama = "Ramen Enoboruki"
        harga = 37000
    if pilihan == "9":
        nama = "Sushi Salmon Mix Beef Spicy"
        harga = 64800
    elif pilihan == "10":
        nama = "Rice Bowl Ayam Bakar Madu"
        harga = 29000
    if pilihan == "11":
        nama = "Caribbean Chicken Steak"
        harga = 89000
    elif pilihan == "11":
        nama = "Exotic Grilled Beef"
        harga = 150000
    if pilihan == "12":
        nama = "Mentai Fish Baked Rice With Mushroom"
        harga = 50000
    elif pilihan == "13":
        nama = "Chicken Cordon Blue"
        harga = 61450
    if pilihan == "14":
        nama = "Fish And Chips"
        harga = 46000
    elif pilihan == "15":
        nama = "Wagyu Steak"
        harga = 189000  
    else:
        print("Pilihan tidak valid")
        return

    # Tanya ingin langsung pesan atau simpan ke wishlist

        tambah_ke_wishlist(nama, harga)
    print("\nPilih aksi:")
    print("1. Pesan langsung")
    print("2. Tambahkan ke wishlist")
    aksi = input("Masukkan pilihan: ")

    if aksi == "1":
        tambah_ke_pesanan(nama, harga)
    elif aksi == "2":
        tambah_ke_wishlist(nama, harga)
    if aksi == "3":
        tambah_ke_wishlist(nama, harga)
    elif aksi == "4":
        tambah_ke_wishlist(nama, harga)
    if aksi == "5":
        tambah_ke_wishlist(nama, harga)
    elif aksi == "6":
        tambah_ke_wishlist(nama, harga)
    if aksi == "7":
        tambah_ke_wishlist(nama, harga)
    elif aksi == "8":
        tambah_ke_wishlist(nama, harga)
    if aksi == "9":
        tambah_ke_wishlist(nama, harga)
    elif aksi == "10":
        tambah_ke_wishlist(nama, harga)
    if aksi == "11":
        tambah_ke_wishlist(nama, harga)
    elif aksi == "12":
        tambah_ke_wishlist(nama, harga)
    if aksi == "13":
        tambah_ke_wishlist(nama, harga) 
    elif aksi == "14":
        tambah_ke_wishlist(nama, harga) 
    if aksi == "15":
        tambah_ke_wishlist(nama, harga)       
    else:
        print("Aksi tidak valid.")

        # Tambahkan ke list pesanan
def menu_makanan():
    global total_harga

    print("\n===== MENU MAKANAN =====")
    print("1. Nasi Goreng - 15000")
    print("2. Mie Goreng - 14000")
    print("3. Beef Aussie Rice Bowl - 45000")
    print("4. Chicken Steak Crispy - 38500")
    print("5. Salmon Mentai Rice - 63000")
    print("6. Salted Egg Chicken Rice Bowl - 29000")
    print("7. Nasi Telur Dadar - 10000")
    print("8. Ramen Enoboruki - 37000")
    print("9. Sushi Salmon Mix Beef Spicy - 64800")
    print("10. Rice Bowl Ayam Bakar Madu - 29000")
    print("11. Caribbean Chicken Steak - 89000")
    print("12. Mentai Fish Baked Rice With Mushroom - 50000")
    print("13. Chicken Cordon Blue - 61450")
    print("14. Fish And Chips - 46000")
    print("15. Wagyu Steak - 189000")

    pilihan = input("Pilih makanan: ")

    menu = {
        "1": ("Nasi Goreng", 15000),
        "2": ("Mie Goreng", 14000),
        "3": ("Beef Aussie Rice Bowl", 45000),
        "4": ("Chicken Steak Crispy", 38500),
        "5": ("Salmon Mentai Rice", 63000),
        "6": ("Salted Egg Chicken Rice Bowl", 29000),
        "7": ("Nasi Telur Dadar", 10000),
        "8": ("Ramen Enoboruki", 37000),
        "9": ("Sushi Salmon Mix Beef Spicy", 64800),
        "10": ("Rice Bowl Ayam Bakar Madu", 29000),
        "11": ("Caribbean Chicken Steak", 89000),
        "12": ("Mentai Fish Baked Rice With Mushroom", 50000),
        "13": ("Chicken Cordon Blue", 61450),
        "14": ("Fish And Chips", 46000),
        "15": ("Wagyu Steak", 189000)
    }

    if pilihan in menu:
        nama, harga = menu[pilihan]
        pesanan.append(f"{nama} - {harga}")
        total_harga += harga
        print(f"{nama} ditambahkan ke pesanan.")
    else:
        print("Pilihan tidak valid")

def menu_dessert():
    print("\n===== MENU DESSERT =====")
    print("1. Ice Cream - 10000")
    print("2. Pudding - 8000")

    pilihan = input("Pilih dessert: ")

    if pilihan == "1":
        nama = "Ice Cream"
        harga = 10000
    elif pilihan == "2":
        nama = "Pudding"
        harga = 8000
    else:
        print("Pilihan tidak valid")
        return

    print("\nPilih aksi:")
    print("1. Pesan langsung")
    print("2. Tambahkan ke wishlist")
    aksi = input("Masukkan pilihan: ")

    if aksi == "1":
        tambah_ke_pesanan(nama, harga)
    elif aksi == "2":
        tambah_ke_wishlist(nama, harga)
    else:
        print("Aksi tidak valid.")

        # Tambahkan pesanan
    pesanan.append(f"Ice Cream - 10000" if pilihan == "1" else f"Pudding - 8000")
    global total_harga
    total_harga += 10000 if pilihan == "1" else 8000

def menu_cemilan():
    print("\n===== MENU CEMILAN =====")
    print("1. Kentang Goreng - 12000")
    print("2. Nugget - 13000")

    pilihan = input("Pilih cemilan: ")

    if pilihan == "1":
        nama = "Kentang Goreng"
        harga = 12000
    elif pilihan == "2":
        nama = "Nugget"
        harga = 13000
    else:
        print("Pilihan tidak valid")
        return

    print("\nPilih aksi:")
    print("1. Pesan langsung")
    print("2. Tambahkan ke wishlist")
    aksi = input("Masukkan pilihan: ")

    if aksi == "1":
        tambah_ke_pesanan(nama, harga)
    elif aksi == "2":
        tambah_ke_wishlist(nama, harga)
    else:
        print("Aksi tidak valid.")

    # Tambahkan pesanan
    pesanan.append(f"Kentang Goreng - 12000" if pilihan == "1" else f"Nugget - 13000")
    global total_harga
    total_harga += 12000 if pilihan == "1" else 13000

# =====================================
# NALA
# MENU MINUMAN
# =====================================

def menu_minuman():
    print("\n===== MENU MINUMAN =====")
    print("1. Es Teh - 5000")
    print("2. Kopi - 10000")
    print("3. Jus - 12000")

    pilihan = input("Pilih minuman: ")

    if pilihan == "1":
        nama = "Es Teh"
        harga = 5000
    elif pilihan == "2":
        nama = "Kopi"
        harga = 10000
    elif pilihan == "3":
        nama = "Jus"
        harga = 12000
    else:
        print("Pilihan tidak valid")
        return

    print("\nPilih aksi:")
    print("1. Pesan langsung")
    print("2. Tambahkan ke wishlist")
    aksi = input("Masukkan pilihan: ")

    if aksi == "1":
        tambah_ke_pesanan(nama, harga)
    elif aksi == "2":
        tambah_ke_wishlist(nama, harga)
    else:
        print("Aksi tidak valid.")

        # Tambahkan pesanan
    if pilihan == "1":
        pesanan.append("Es Teh - 5000")
        global total_harga
        total_harga += 5000
    elif pilihan == "2":
        pesanan.append("Kopi - 10000")
        total_harga += 10000
    elif pilihan == "3":
        pesanan.append("Jus - 12000")
        total_harga += 12000
    # Tambahkan harga
    else:
        print("Pilihan tidak valid")

# =====================================
# PASYA
# PAYMENT DAN CETAK STRUK
# =====================================

def payment():
    global total_harga

    print("\n===== PAYMENT =====")
    print("Total Harga:", total_harga)

    uang = int(input("Masukkan uang: "))

    kembalian = uang - total_harga

    print("Kembalian:", kembalian)

    print_struk()

def print_struk():
    print("\n===== STRUK PEMBELIAN =====")
    print("Nama:", nama_pelanggan)
    print("Tipe:", tipe_pesanan)

    print("\nPesanan:")
    for item in pesanan:
        print("-", item)

    print("Total:", total_harga)
    print("\nTerima kasih telah berkunjung!")

# =====================================
# MENU UTAMA (MENU KEDUA)
# =====================================

def menu_utama():
    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Daftar Makanan")
        print("2. Daftar Minuman")
        print("3. Dessert")
        print("4. Cemilan")
        print("5. Lihat Wishlist")
        print("6. Pesan dari Wishlist")
        print("7. Payment")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_makanan()
        elif pilihan == "2":
            menu_minuman()
        elif pilihan == "3":
            menu_dessert()
        elif pilihan == "4":
            menu_cemilan()
        elif pilihan == "5":
            lihat_wishlist()
        elif pilihan == "6":
            pindah_dari_wishlist()
        elif pilihan == "7":
            payment()
            break
        else:
            print("Pilihan tidak valid")

# =====================================
# PROGRAM UTAMA
# =====================================

def main():
    input_pelanggan()
    menu_utama()

main()