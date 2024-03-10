# TODO TRANSFORMASI TIPE DATA

# TODO Mengubah Huruf Besar dan Huruf Kecil
kata = "Dicoding"
# upper(mengubah menjadi huruf besar)
kata = kata.upper()  # Output: 'DICODING'
print(kata)
# lower(mengubah menjadi huruf kecil)
kata = kata.lower()  # Output: 'dicoding'
print(kata)

# TODO Awalan Dan Akhiran
# rstrip(menghapus whitespace pada sebelah kanan atau akhir string.)
print("Dicoding         ".rstrip())  # Output: 'Dicoding'
# lstrip(menghapus whitespace pada sebelah kiri atau awal string.)
print("         Dicoding".lstrip())  # Output: 'Dicoding'
# strip(menghapus whitespace pada kedua sisi string.)
print("         Dicoding         ".strip())  # Output: 'Dicoding'
# startswith(mengecek apakah string diawali dengan teks tertentu.)
print("Dicoding Indonesia".startswith("Dicoding"))  # Output: True
# endswith(mengecek apakah string diakhiri dengan teks tertentu.)
print("Dicoding Indonesia".endswith("Indonesia"))  # Output: True

# TODO Memisah Dan Menggabungkan String
# join(menggabungkan string dengan menggunakan separator tertentu.)
print(" ".join(["Dicoding", "Indonesia", "!"]))  # Output: 'Dicoding Indonesia !'
print("123".join(["Dicoding", "Indonesia"]))  # Output: 'Dicoding123Indonesia

# split(memisahkan string berdasarkan separator tertentu.)
print("Dicoding Indonesia !".split())  # Output: ['Dicoding', 'Indonesia', '!']

# new line(\n) sebagai separator
print("Dicoding\nIndonesia\n!".split("\n"))  # Output: ['Dicoding', 'Indonesia', '!']

# TODO Mengganti Element String
string = "Ayo belajar Coding di Dicoding!"
print(
    string.replace("Coding", "Pemrograman")
)  # Output: 'Ayo belajar Pemrograman di Dicoding!'


# TODO Pengecekan String
kata = "dicoding"
# isupper(mengecek apakah semua huruf dalam string adalah huruf besar.)
print(kata.isupper())  # Output: False
# islower(mengecek apakah semua huruf dalam string adalah huruf kecil.)
print(kata.islower())  # Output: True
# isalpha(mengecek apakah semua karakter dalam string adalah huruf.)
print(kata.isalpha())  # Output: True
# isalnum(mengecek apakah semua karakter dalam string adalah huruf atau angka.)
print(kata.isalnum())  # Output: True
# isdecimal(mengecek apakah semua karakter dalam string adalah angka.)
print(kata.isdecimal())  # Output: False
# isspace(mengecek apakah semua karakter dalam string adalah whitespace.)
print(kata.isspace())  # Output: False
# istitle(mengecek apakah string diawali dengan huruf kapital dan dilanjutkan dengan huruf kecil seterusnya.)
print(kata.istitle())  # Output: False

# TODO Formatting Pada String
teks = "Code"
# zfill(menambahkan angka 0 di depan string hingga panjang karakter tertentu.)
tambah_number = teks.zfill(5)
print(tambah_number)  # Output: 0Code
# rjust(menambahkan spasi di depan string hingga panjang karakter tertentu.)
tambah_space = teks.rjust(8)
print(tambah_space)
# ljust(menambahkan spasi di belakang string hingga panjang karakter tertentu.)
tambah_space = teks.ljust(8)
print(tambah_space)
# center(menambahkan spasi di depan dan belakang string hingga panjang karakter tertentu.)
tambah_space = teks.center(8)
print(tambah_space)  # Output: '  Code  '

# TODO String Literals
str1 = "Jum'at"
str2 = "Jum'at"
print(str1)
print(str2)

# TODO Raw String
# Raw string adalah string yang diawali dengan huruf r. Raw string berguna ketika Anda ingin mengabaikan escape sequence.
print(r"Newline akan diabaikan \n newline akan diabaikan")
# Output: Newline akan diabaikan \n newline akan diabaikan
print("Dicoding\tIndonesia")  # Output: Dicoding    Indonesia
