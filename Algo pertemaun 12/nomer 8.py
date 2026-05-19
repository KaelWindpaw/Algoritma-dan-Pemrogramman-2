def segitiga(a, b, c):
    return all([a + b > c, a + c > b, b + c > a])

print(segitiga(3, 4, 5))