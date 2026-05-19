# langkah 2 (append manual)
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

# langkah 3 (pakai loop)
tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]

for anggota in tambahan:
    exo.append(anggota)

# langkah 4 (hapus anggota)
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")

# langkah 5 (insert posisi ke-3 dari belakang)
exo.insert(len(exo)-2, "Xiumin")

print(exo)