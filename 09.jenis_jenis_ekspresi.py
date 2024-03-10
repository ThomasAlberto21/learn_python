"""
# ! EKSPRESI
 Ekspresi pada pemrograman merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan fungsi yang bermakna untuk menghasilkan suatu nilai dalam suatu tipe tertentu.
"""

# TODO Ekspresi Menurut Arity dari Operator
# ? - Operator Biner : Ekspresi biner merupakan jenis yang memiliki dua operan. Operatornya meliputi penjumlahan (+), pengurangan (-), perkalian (*), pembagian (/), perpangkatan (**), lebih kecil dari (<), lebih kecil dari sama dengan (<=), lebih besar dari (>), lebih besar dari sama dengan (>=), modulus (%), sama dengan (==), dan tidak sama dengan (!=).
# biner : (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

# ? - Operator Uniner : Ekspresi uner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan satu operan. Contohnya adalah increment (x+=1), decrement (x-=1), dan negasi (not x).
# uner : (x += 1), (x-=1), (not x).

# TODO Contoh Kode Ekspresi Uner
a = True
a = not a
print(a)  # False

b = 6
b -= 1
print(b)  # 5 (Decrement)

c = 6
c += 1
print(c)  # 7 (Increment)

d = 10
print(-d)  # -10

# TODO Ekspresi Menurut Tipe Data yang Dihasilkan
"""
- Ekspresi aritmetika (jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan numerik.): 
<numerik> <operator> <numerik> = <numerik>
contoh : 2 + 2 = 4, 2 - 2 = 0

- Ekspresi relasional (jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan nilai boolean/logika.): 
<numerik> <operator> <numerik> = <boolean>
contoh : 3 < 10 = True, 1 > 10 = False

- Ekspresi logika (jenis ekspresi yang memiliki operan bertipe boolean/logika dan menghasilkan nilai boolean/logika.): 
<boolean> <operator> <boolean> = <boolean>
contoh : True or False = True

"""

# TODO Contoh Kode Ekspresi Aritmetika
print(2 + 2)  # Ekspresi Aritmetika
print(3 < 10)  # Ekspresi Relasional
print(True or False)  # Ekspresi Logika
