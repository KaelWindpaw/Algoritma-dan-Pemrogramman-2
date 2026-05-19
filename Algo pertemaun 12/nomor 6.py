def segitiga(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Bisa membentuk segitiga")
    else:
        print("Tidak bisa")

segitiga(3, 4, 5)