"""
TODO : Matriks dalam Matematika
Matriks pada matematika merupakan himpunan yang terdiri dari bilangan atau elemen berdasarkan baris dan kolom.

Contoh matriks dalam matematika beragam jenisnya, beberapa di antaranya sebagai berikut.

- Matriks Pengukuran
Matriks pengukuran adalah jenis matriks dengan indeks (i, j) yang merepresentasikan suatu titik koordinat. Setiap elemen dari matriks ini merepresentasikan hasil pengukuran pada suatu titik koordinat tertentu dan termasuk bilangan real atau tipe data float.

- Matriks Satuan
Selanjutnya adalah matriks satuan dengan elemen bernilai hanya 0 atau 1. Setiap elemen matriks ini bertipe data integer.

TODO : Matriks dalam Pemrograman
Sementara itu dalam pemrograman, matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom. Matriks dalam pemrograman diimplementasikan menggunakan array dua dimensi. Bahkan dalam Python, matriks dapat diimplementasikan menggunakan nested list atau list di dalam list.
"""

# Contoh Kode Matriks dalam Pemrograman tanpa menggunakan library

# TODO : Deklarasi Matriks
matriks = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
print(matriks)

# TODO : Deklarasi dengan nilai default
matrik = [[0 for j in range(4)] for i in range(3)]
print(matrik)


# TODO : Akses Elemen Matriks
var_mat = [
    [1, 2, 3, 4, 5],  # baris ke-0
    [6, 7, 8, 9, 10],  # baris ke-1
    [11, 12, 13, 14, 15],  # baris ke-2
    [16, 17, 18, 19, 20],  # baris ke-3
    [21, 22, 23, 24, 25],  # baris ke-4
]

print(var_mat[2][1])  # Output: 12
