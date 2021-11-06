a = int(input("masukan angka bilangan 1: "))
b = int(input("masukan angka bilangan 2: "))
c = int(input("masukan angka bilangan 3: "))

if a > b:
    terbesar = a
else:
    terbesar = b
if terbesar < c:
    terbesar = c
print ("bilangan terbesar adalah",terbesar)