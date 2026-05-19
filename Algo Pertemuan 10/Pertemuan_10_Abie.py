# SOAL NOMOR 1
# pangkat = [x ** 2 for x in range(10)]
# print("Bilangan kuadrat 0-9:", pangkat)
#
# dua_pangkat = [2 ** i for i in range(8)]
# print("Bilangan 2 pangkat i (0-7):", dua_pangkat)
#
# ganjil = [x for x in pangkat if x % 2 != 0]
# print("Bilangan ganjil dari list pangkat:", ganjil)
#
# genap = [x for x in pangkat if x % 2 == 0]
# print("Bilangan genap dari list pangkat:", genap)


# SOAL NOMOR 2
# Membuat papan catur 8x8 dengan list comprehension
# KOSONG = "[]"
# papan_catur = [[KOSONG for i in range(8)] for j in range(8)]
#
# Menampilkan papan catur
# print("Papan Catur 8x8:")
# for baris in papan_catur:
#     print(" ".join(baris))
#
# Menempatkan benteng pada posisi tertentu
# print("\nMenempatkan benteng di posisi (0,0) dan (0,7):")
# papan_catur[0][0] = "BR"  # Benteng di baris 1 kolom A
# papan_catur[0][7] = "BR"  # Benteng di baris 1 kolom H
#
# for baris in papan_catur:
#    print(" ".join(baris))


# SOAL NOMOR 3
# Membuat papan catur 8x8 dengan list comprehension
# KOSONG = "[]"
# papan_catur = [[KOSONG for i in range(8)] for j in range(8)]
#
# Menampilkan papan catur
# print("Papan Catur 8x8:")
# for baris in papan_catur:
#    print(" ".join(baris))
#
# Menempatkan benteng pada posisi tertentu
# print("\nMenempatkan benteng di posisi (0,0) dan (0,7):")
# papan_catur[0][0] = "BR"  # Benteng di baris 1 kolom A
# papan_catur[0][7] = "BR"  # Benteng di baris 1 kolom H
#
# for baris in papan_catur:
#     print(" ".join(baris))


# SOAL NOMOR 4
# # Fungsi menghitung diskon belanja
# def hitung_diskon(total_belanja, member=False, kupon=None):
#     diskon = 0
#    
#    # Diskon member 10%
#     if member:
#        diskon += 10
#        print("✅ Diskon Member 10% diterapkan")
#    
#    # Diskon kupon
#    if kupon == "HEMAT20":
#        diskon += 20
#        print("✅ Kupon HEMAT20: diskon 20% diterapkan")
#    if kupon == "HEMAT10":
#        diskon += 10
#        print("✅ Kupon HEMAT10: diskon 10% diterapkan")
#   
#    # Diskon tambahan untuk belanja > 500000
#    if total_belanja > 500000:
#        diskon += 5
#        print("✅ Bonus belanja > Rp500.000: diskon 5% diterapkan")
#    
#    total_diskon = total_belanja * diskon / 100
#    total_bayar = total_belanja - total_diskon
#    
#    return total_bayar, diskon
#
# Demo pemanggilan fungsi
# print("=== TRANSAKSI 1 ===")
# bayar1, diskon1 = hitung_diskon(350000, member=True)
# print(f"Total belanja: Rp350.000")
# print(f"Total diskon: {diskon1}%")
# print(f"Total bayar: Rp{bayar1:,.0f}")
#
# print("\n=== TRANSAKSI 2 ===")
# bayar2, diskon2 = hitung_diskon(750000, kupon="HEMAT20", member=False)
# print(f"Total belanja: Rp750.000")
# print(f"Total diskon: {diskon2}%")
# print(f"Total bayar: Rp{bayar2:,.0f}")
#
# print("\n=== TRANSAKSI 3 ===")
# bayar3, diskon3 = hitung_diskon(600000, member=True, kupon="HEMAT10")
# print(f"Total belanja: Rp600.000")
# print(f"Total diskon: {diskon3}%")
# print(f"Total bayar: Rp{bayar3:,.0f}")


# SOAL NOMOR 5
# # Program: bilangan 1-10, ambil genap, kalikan 3
# hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]
#
# print("Bilangan 1-10 yang genap, dikali 3:")
# print(hasil)


# SOAL NOMOR 6
# Program: bilangan 1-10, ambil genap, kalikan 3
# hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]
#
# print("Bilangan 1-10 yang genap, dikali 3:")
# print(hasil)


# SOAL NOMOR 7
# # Program: flatten list multidimensi
data = [[2, 4], [6, 8], [10, 12]]

# Cara 1: Menggunakan nested loop
# hasil1 = []
# for sublist in data:
#     for elemen in sublist:
#         hasil1.append(elemen)
#
# print("Flatten dengan nested loop:")
# print(hasil1)
#
# Cara 2: Menggunakan list comprehension
# hasil2 = [elemen for sublist in data for elemen in sublist]
#
# print("\nFlatten dengan list comprehension:")
# print(hasil2)


# SOAL NOMOR 8
# # Program: Fungsi menghitung luas persegi panjang
# def hitung_luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas
#
# Memanggil fungsi dengan panjang=8, lebar=5
# p = 8
# l = 5
# hasil = hitung_luas_persegi_panjang(p, l)
#
# print(f"Panjang = {p}")
# print(f"Lebar   = {l}")
# print(f"Luas persegi panjang = {p} x {l} = {hasil}")

 