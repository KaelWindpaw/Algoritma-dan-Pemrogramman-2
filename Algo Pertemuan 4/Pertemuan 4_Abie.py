# 1. Membuat fungsi input kemudian tampilkan ke konsol
# name = input("Kael Windpaw Werewolf")
# Werewolf = input()
# print("Handsome", Werewolf, "Inside")

# 2. Membuat fungsi input dengan argumen
# somewhere = input("Are you there?")
# print("i'm arent", somewhere, "here")

# 3. Memahami hasil dari fungsi input
# My_woof = float("Enter a number: ")
# His_name_is_Kael = My_woof * 3.0
# print(str(My_woof) + " have 3 side ", His_name_is_kael)

# 4. Mengkonversi tipe data float pada fungsi input
# My_woof = float("Enter a number: ")
# His_name_is_Kael = My_woof * 3.0
# print(str(My_woof) + " have 3 side ", His_name_is_kael)

# 5. Menghitung sisi miring segitiga (dengan variabel hypo)
# a = float(input("Enter first leg length: "))
# b = float(input("Enter second leg length: "))
# hypo = (a**2 + b**2) ** 0.5
# print("Hypotenuse length is", hypo)

# 6. Menghitung sisi miring segitiga tanpa variabel
# a = float(input("Enter first leg length: "))
# b = float(input("Enter second leg length: "))
# print((a**2 + b**2) ** 0.5)


# soal no 7
# fnam = input("May I have known your first number, please? ")
# lnam = input("May I have known your last number, please? ")
# print("Thank you.")
# print("\nYour number is " + fnam + " " + lnam + ".")
# 


# soal no 8
# print("+" + 25 * "-" + "++")
# print(("|" + " " + 25 + "|\n") * 5, end="")
# print("+" + 25 * "-" + "++")
# 


# soal no 9
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
# 


# soal no 10
# x = input("Enter a Password number : ")
# print (x)
# 


# soal no 11
# # Meminta input dari user untuk variabel a dan b
# a = float(input("Masukkan nilai a: "))
# b = float(input("Masukkan nilai b: "))
# 
# # Menghitung hasil penjumlahan
# penjumlahan = a + b
# print("Hasil penjumlahan:", penjumlahan)
# 
# # Menghitung hasil pengurangan
# pengurangan = a - b
# print("Hasil pengurangan:", pengurangan)
# 
# # Menghitung hasil pembagian
# if b != 0:
#     pembagian = a / b
#     print("Hasil pembagian:", pembagian)
# else:
#     print("Hasil pembagian: Tidak dapat dibagi dengan")
# 
# # Menghitung hasil perkalian
# perkalian = a * b
# print("Hasil perkalian:", perkalian)
# 
# # Menampilkan kalimat selamat
# print("Selamat kamu sudah pintar matematika")
# 


# soal no 12
# # Input nilai x
# x = float(input("Masukkan nilai x: "))
# 
# # Inisialisasi nilai y
# # Untuk pecahan berulang tak hingga seperti ini, kita bisa menggunakan pendekatan iteratif
# # Rumusnya: y = 1/(x + y)
# 
# # Tebakan awal
# y = 0.0
# 
# # Iterasi untuk mendapatkan nilai konvergen
# for i in range(100):  # 100 iterasi cukup untuk konvergensi
#     y = 1.0 / (x + y)
# 
# # Tampilkan hasil
# print(f"Nilai y = {y}")
# 


# soal no 13
# jam = int(input("Waktu mulai (jam): "))
# menit = int(input("Waktu mulai (menit): "))
# durasi = int(input("Durasi Acara (menit): "))
# 
# # Tulis kode kamu disini
# # Hitung total menit dari waktu mulai
# total_menit = jam * 60 + menit + durasi
# 
# # Hitung jam dan menit baru
# jam_selesai = (total_menit // 60) % 24 # Mod 24 untuk format 24 jam
# menit_selesai = total_menit % 60
# 
# # Tampilkan hasil
# print(f"Acara selesai pukul {jam_selesai}:{menit_selesai:02d}")