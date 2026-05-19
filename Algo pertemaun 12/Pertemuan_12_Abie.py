# SOAL NOMOR 1
# def hitung_luas():
#     panjang = 10   # variabel lokal
#     lebar = 5      
#     luas = panjang * lebar  
#     print("Luas =", luas)
#
# hitung_luas()


# SOAL NOMOR 2
# bilangan = 2
# def perkalian_bilangan(X):
#     return X*bilangan
#
# print(perkalian_bilangan(14))


# SOAL NOMOR 3
# def perkalian_bilangan(X):
#     bilangan = 7
#     return X*bilangan
#
# bilangan = 3
# print(perkalian_bilangan(15))


# SOAL NOMOR 4
# total = 0  # variabel global
#
# def tambah():
#     global total  
#     total = total + 10
#     print("Di dalam fungsi:", total)
#
# tambah()
# print("Di luar fungsi:", total)


# SOAL NOMOR 5
# def hitung_imt(berat, tinggi):
#     imt = berat / (tinggi ** 2)
#     return imt
#
# bb = float(input("Masukkan berat badan (kg): "))
# tb = float(input("Masukkan tinggi badan (m): "))
#
# hasil = hitung_imt(bb, tb)
# print("IMT =", hasil)


# SOAL NOMOR 6
# def segitiga(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         print("Bisa membentuk segitiga")
#     else:
#         print("Tidak bisa")
#
# segitiga(3, 4, 5)


# SOAL NOMOR 7
# def segitiga(a, b, c):
#     return a + b > c and a + c > b and b + c > a
#
# print(segitiga(3, 4, 5))


# SOAL NOMOR 8
# def segitiga(a, b, c):
#     return all([a + b > c, a + c > b, b + c > a])
#
# print(segitiga(3, 4, 5))


# SOAL NOMOR 9
# def faktorial(n):
#     hasil = 1
#     for i in range(1, n+1):
#         hasil *= i
#     return hasil
#
# print(faktorial(5))


# SOAL NOMOR 10
# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n-2):
#         a, b = b, a + b
#     return b
#
# print(fibonacci(6))


# SOAL NOMOR 11
# def faktorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n-1)
# 
# print(faktorial(5))


# SOAL NOMOR 12
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(6))
