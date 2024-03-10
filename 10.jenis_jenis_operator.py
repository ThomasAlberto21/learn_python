# Jenis - Jenis Operator

# TODO Operator Aritmetika
# Operator aritmetika merupakan operator yang digunakan untuk melakukan operasi matematika. Operator ini meliputi penjumlahan (+), pengurangan (-), perkalian (*), pembagian (/), pembagian bulat (//), perpangkatan (**), dan modulus (%).
"""
- Penjumlahan (+) : Menambahkan nilai dari kedua operan.
contoh : 2 + 2 = 4
- Pengurangan (-) : Mengurangi nilai dari kedua operan.
contoh : 2 - 2 = 0
- Perkalian (*) : Mengalikan nilai dari kedua operan.
contoh : 2 * 2 = 4
- Pembagian (/) : Membagi nilai dari kedua operan.
contoh : 2 / 2 = 1
- Pembagian Bulat (//) : Membagi nilai dari operan pertama dengan operan kedua dan mengembalikan hasil pembagian bulat.
contoh : 2 // 2 = 1
- Perpangkatan (**) : Memangkatkan nilai dari operan pertama dengan operan kedua.
contoh : 2 ** 2 = 4
- Modulus (%) : Mengembalikan sisa hasil bagi dari operan pertama dengan operan kedua.
contoh : 2 % 2 = 0
"""

# TODO Contoh Kode Operator Aritmetika
x = 11
y = 5

print(x + y)  # Pnjumlahan
print(x - y)  # Pengurangan
print(x * y)  # Perkalian
print(x // y)  # Pembagian
print(x / y)  # Pembagian
print(x % y)  # Modulus
print(x**y)  # Perpangkatan


# TODO Operator Relasional
# Operator relasional merupakan operator perbandingan antara dua operan yang berupa integer, float, string, ataupun boolean. Hasil akhir dari operator ini adalah nilai bertipe boolean.
"""
- Sama dengan (==) : Menghasilkan True, jika kedua operan bernilai sama.
contoh : x == y, menghasilkan False.
- Tidak sama dengan (!=) : Menghasilkan True, jika kedua operan bernilai berbeda.
contoh : x != y, menghasilkan True.
- Lebih besar dari (>) : Menghasilkan True, jika operan pertama lebih besar dari operan kedua.
contoh : x > y, menghasilkan True.
- Kurang dari (<) : Menghasilkan True, jika operan pertama lebih kecil dari operan kedua.
contoh : x < y, menghasilkan False.
- Lebih besar dari sama dengan (>=) : Menghasilkan True, jika operan pertama lebih besar dari atau sama dengan operan kedua.
contoh : x >= y, menghasilkan True.
- Kurang dari sama dengan (<=) : Menghasilkan True, jika operan pertama lebih kecil dari atau sama dengan operan kedua.
contoh : x <= y, menghasilkan False.
"""

# TODO Contoh Kode Operator Relasional
x = 5
y = 10

print(x == y)  # Sama dengan
print(x != y)  # Tidak sama dengan
print(x > y)  # Lebih besar dari
print(x < y)  # Kurang dari
print(x >= y)  # Lebih besar dari sama dengan
print(x <= y)  # Kurang dari sama dengan


# TODO Operator Logika
# Operator logika merupakan jenis operator untuk melakukan operasi logika dengan kedua operannya bertipe boolean. Hasil akhir dari operasi ini adalah nilai bertipe boolean.
"""
- "AND" atau "&" : Logika yang hanya menghasilkan True jika kedua operan bernilai True.
contoh : True and False, menghasilkan False.
- "OR" atau "|" : Logika yang menghasilkan True jika salah satu operan bernilai True.
contoh : True or False, menghasilkan True.
- "NOT" atau "!" : Logika yang bertujuan untuk membalikkan nilai logika dari operannya.
contoh : not True, menghasilkan False.
"""

# TODO Contoh Kode Operator Logika
# AND
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# OR
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# NOT
print(not True)  # False
print(not False)  # True


# TODO Operator Assignment
#  Operator ini bertujuan untuk melakukan proses assignment atau pemberian nilai pada suatu variabel dengan nilai tetap.
"""
- += : Menyederhanakan operasi x = x + y.
contoh : x += y, sama dengan x = x + y.
- -= : Menyederhanakan operasi x = x - y.
contoh : x -= y, sama dengan x = x - y.
- *= : Menyederhanakan operasi x = x * y.
contoh : x *= y, sama dengan x = x * y.
- /= : Menyederhanakan operasi x = x / y.
contoh : x //= y, sama dengan x = x // y.
- %= : Menyederhanakan operasi x = x % y.
contoh : x %= y, sama dengan x = x % y.
"""

# TODO Contoh Kode Operator Assignment
# +=
x = 11
x += 5
print(x) # 16

# -=
x = 11
x -= 5
print(x) # 6

# *=
x = 11
x *= 5
print(x) # 55

# /=
x = 11
x /= 5
print(x) # 2.2

# %=
x = 11
x %= 5
print(x) # 1
