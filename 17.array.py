"""
TODO :  Array
Perlu diketahui oleh Anda, array bukan hanya sebuah tipe data, melainkan salah satu tipe struktur data berjenis linear. Array merupakan kata dalam bahasa Inggris yang jika diterjemahkan ke bahasa Indonesia memiliki arti "sebuah kelompok besar yang terdiri dari beberapa hal atau orang". Arti ini mirip dengan array atau tipe data list dalam Python, sebuah kelompok besar yang terdiri dari beberapa nilai atau data. Lalu, apa arti dari struktur data itu sendiri?
"""

# Contoh Kode Array
var_arr = [1, 2, 3, 4, 5]
print(var_arr)

# Contoh Kode Array untuk mendefinisikan nilai default
"""
Pada contoh di atas, kita membuat list dengan nilai default-nya adalah "0" sebanyak 10 elemen. Perhatikan bahwa <default-val> yang ada pada struktur sebelumnya diubah menjadi "0" untuk mendapatkan nilai default "0".
"""
var_arr = [0 for i in range(10)]
print(var_arr)

for i in range(10):
    var_arr[i] = i
print(var_arr)

# Contoh Kode Array untuk mengakses elemen array
"""
Mengakses elemen array dalam Python tidak berbeda dengan mengakses elemen pada list. Hal ini karena kita menggunakan list sebagai "bentuk lain" dari array. Anda dapat melakukan metode indexing untuk mengakses elemen array.
"""
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0]) # Output: 9
