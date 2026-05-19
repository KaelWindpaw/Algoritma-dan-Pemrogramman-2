# SOAL NOMOR 1
# def fungsi_tanpa_return():
#     print("Halo dari fungsi")
#
# fungsi_tanpa_return()


# SOAL NOMOR 2
# def fungsi_check(harapan):
#     if harapan == False:
#         return
#     print("Berhasil")
#
# fungsi_check(False)


# SOAL NOMOR 3
# def fungsi_hasil():
#     return 123
#
# x = fungsi_hasil()
# print(x)


# SOAL NOMOR 4
# def fungsi_hasil():
#     print("Dipanggil")
#     return 123
# 
# fungsi_hasil()


# SOAL NOMOR 5
# def fungsi_none():
#     return None
#
# hasil = fungsi_none()
# print(hasil)


# SOAL NOMOR 6
# def cetak_list(data):
#     for item in data:
#         print(item)
#
# cetak_list([1, 2, 3])


# SOAL NOMOR 7
# def tambah_list(data):
#     data.append(100)
#     return data
#
# print(tambah_list([1, 2, 3]))


# SOAL NOMOR 8
# def buat_list():
#     return [10, 20, 30]
#
# hasil = buat_list()
# print(hasil)


# SOAL NOMOR 9
# def kabisat(tahun):
#     if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#         return True
#     return False
#
# data_uji = [2000, 1900, 2024, 2023]
# data_hasil = [True, False, True, False]
#
# for i in range(len(data_uji)):
#     print(kabisat(data_uji[i]) == data_hasil[i])


# SOAL NOMOR 10
# def kabisat(tahun):
#     return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
#
# def jumlah_hari(tahun, bulan):
#     if bulan < 1 or bulan > 12:
#         return None
#    
#     if bulan == 2:
#         return 29 if kabisat(tahun) else 28
#    
#     elif bulan in [4, 6, 9, 11]:
#         return 30
#    
#     else:
#         return 31
#
# print(jumlah_hari(2024, 2))


# SOAL NOMOR 11
# def kabisat(tahun):
#     return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
#
# def jumlah_hari(tahun, bulan):
#     if bulan < 1 or bulan > 12:
#         return None
#    
#     if bulan == 2:
#         if kabisat(tahun):
#             return 29
#         else:
#             return 28
#    
#     elif bulan in [4, 6, 9, 11]:
#         return 30
#     
#     else:
#         return 31
#
# def valid_tanggal(tahun, bulan, hari):
#     jml = jumlah_hari(tahun, bulan)
#     
#     if jml is None:
#         return None
#    
#     if 1 <= hari <= jml:
#         return True
#     else:
#         return False
# 
#
# TEST
# print(valid_tanggal(2024, 2, 29))  # True
# print(valid_tanggal(2023, 2, 29))  # False
# print(valid_tanggal(2024, 13, 10)) # None


# SOAL NOMOR 12
# def cek_prima(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(cek_prima(7))


# SOAL NOMOR 13
# def cek_prima(n):
#     if n <= 1:
#         return False
#    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     
#     return True
#
# for i in range(1, 11):
#     print(i, cek_prima(i))


# SOAL NOMOR 14
# def Liter100km_ke_mpg(l):
#     return 235.215 / l
#
# def mpg_ke_Liter100km(mpg):
#     return 235.215 / mpg
#
# print(Liter100km_ke_mpg(5))
# print(mpg_ke_Liter100km(30))