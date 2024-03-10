"""
# ! TIPE DATA PRIMITIF
Tipe data primitif merupakan jenis paling dasar dalam pemrograman. Tipe data ini menyimpan single value.

TODO 1. Numbers
-   Integer (int) : Bilangan bulat positif atau negatif dan tidak memiliki angka desimal.
Contoh: 1; -20; 999; dan 0.
-   Float (float) : Bilangan riil yang dapat mewakili bilangan bulat atau bilangan desimal.
Contoh: 3.14; 1; dan 4.01E+1
-   Complex (complex) : Bilangan kompleks yang terdiri dari bilangan real dan imajiner.
Contoh: 3 + 4j; 1 + 2j; dan 5 - 6j

# ! PENTING
Perlu diperhatikan bahwa tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah. 

TODO 2. Boolean
-   Boolean (bool) : Tipe data ini hanya memiliki dua nilai yaitu True dan False.
Contoh: True & False

TODO 3. String
-   String (str) : Tipe data ini merupakan kumpulan dari karakter.
Contoh: "Hello World"; "Python"; dan "12345"

"""

# TODO Contoh Kode Tipe Data Numbers
# integer
x = 6
print(x, "is of type", type(x))

# float
y = 7.0
print(y, "is of type", type(y))

# complex
z = 5 + 6j
print(z, "is of type", type(z))

# Contoh Kode Tipe Data Boolean
# True
a = True
print(a, "is of type", type(a))

# False
b = False
print(b, "is of type", type(b))


# TODO Contoh Kode Tipe Data String
# String
name = "John Doe"

# indexing dan slicing
name2 = "Dicoding"
print(name2[2:])  # Output: coding

# formatted string
name3 = "John"
print(f"Hello, {name3}!")  # Output: Hello, John!

# %-formatting
name4 = "Doe"
print("Hello, %s!" % name4)  # Output: Hello, Doe!

# str.format()
name5 = "John Doe"
print("Hello, {}!".format(name5))  # Output: Hello, John Doe!
