def hitung_imt(berat, tinggi):
    imt = berat / (tinggi ** 2)
    return imt

bb = float(input("Masukkan berat badan (kg): "))
tb = float(input("Masukkan tinggi badan (m): "))

hasil = hitung_imt(bb, tb)
print("IMT =", hasil)