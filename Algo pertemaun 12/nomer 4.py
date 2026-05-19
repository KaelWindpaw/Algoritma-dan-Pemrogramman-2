total = 0  # variabel global

def tambah():
    global total  
    total = total + 10
    print("Di dalam fungsi:", total)

tambah()
print("Di luar fungsi:", total)