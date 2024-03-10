"""
# ! TIPE DATA COLLECTION
Tipe data collection merupakan tipe data yang menyimpan satu atau lebih data primitif sebagai satu kelompok

TODO 1. List
List merupakan jenis kumpulan data terurut (ordered sequence) dan salah satu tipe data yang sering digunakan pada Python. List dalam Python ini serupa, tetapi tak sama dengan array pada bahasa pemrograman lainnya. List Python tidak mengharuskan memiliki tipe data yang sama di dalamnya, sedangkan array sebaliknya, List bersifat mutable yang berarti setiap elemen di dalam list dapat diubah.

TODO 2. Tuple
Tuple adalah jenis dari list yang tidak dapat diubah elemennya. Umumnya, tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat. Tuple didefinisikan dengan kurung “()“ dan setiap elemen di dalamnya dipisahkan dengan koma, Tuple bersifat immutable yang artinya tidak dapat diubah.

TODO 3. Set
Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection), dan dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma.
Tidak sama seperti list, dalam set kita tidak bisa melakukan indeksing karena set tidak memiliki indeks. Hal ini merujuk pada definisi nya yang menyatakan bahwa set merupakan kumpulan item tanpa urutan. Selain tanpa urutan (unordered collection). Set juga bersifat unik, artinya, data yang Anda simpan pada set tidak akan ada duplikat. Anda dapat memanfaatkan hal ini untuk menghilangkan duplikat pada suatu data.

TODO 4. Dictionary
Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Pada Python, dictionary didefinisikan dengan kurawal dan tambahan definisi berikut.
-   Setiap elemen pasangan key-value dipisahkan dengan koma (,).
-   Key dan value dipisahkan dengan titik dua (:).
-   Key dan value dapat berupa tipe variabel/objek apa pun.
"""

# TODO Contoh Kode Tipe Data List
# List
x = [1, 2, 3, 4, 5, "Dicoding"]
print(x)
print(type(x))

# mengakses elemen
print(x[0])  # Output: 1

# mengubah elemen
x[4] = "Belajar"
print(x)  # Output: [1, 2, 3, 4, 'Belajar', 'Dicoding']

# slicing
y = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
# Rumus : [start:stop:step]
"""
Start merupakan indeks pertama yang Anda ambil. 
Stop merupakan indeks terakhir yang ingin Anda ambil. 
Step merupakan jumlah elemen yang ingin Anda lewati di antara setiap elemen slice. Secara default, nilai step adalah 1.
"""
print(y[0:5:2])  # Output: ['laptop', 'mouse', 'keyboard']
print(y[0:5])  # Output: ['laptop', 'monitor', 'mouse', 'mousepad', 'keyboard']
print(y[0:5:1])  # Output: ['laptop', 'monitor', 'mouse', 'mousepad', 'keyboard']
print(y[0:5:3])  # Output: ['laptop', 'mousepad']


# TODO Contoh Kode Tipe Data Tuple
# Tuple
z = (1, "dicoding", 1 + 3j)
print(z)
print(type(z))

# indexing & slicing
print(z[0])  # Output: 1
print(z[0:3])  # Output: 1, 'dicoding', (1+3j)


# TODO Contoh Kode Tipe Data Set
# Set
a = {1, 2, 2, 3, 3, 3}
print(a)  # Output: {1, 2, 3} (Duplikasi akan dihilangkan)
print(type(a))  # Output: <class 'set'>
# print(a[0])  # Output: TypeError: 'set' object is not subscriptable

# Union (Gabungan)
set1 = {1, 2, 3, 4, 5}
union = set.union(set1, {6, 7, 8})
print(union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (Irisan)
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print(intersection)  # Output: {4, 5}


# TODO Contoh Kode Tipe Data Dictionary
# Dictionary
b = {"nama": "Dicoding", "tahun": 2013}
print(b)
print(type(b))
print(b["nama"])  # Output: Dicoding

# menambah elemen
b["alamat"] = "Indonesia"
print(b)

# menghapus elemen
del b["tahun"]
print(b)

# mengubah nilai
b["nama"] = "Dicoding Indonesia"
print(b)