"""
Dalam pemrograman, sebuah kode program dapat berjalan berdasarkan kondisi tertentu. Maknanya, Anda dapat memberikan instruksi berdasarkan "Jika-maka" (if-else). 

! IF
If adalah statement Python yang akan mengecek nilai variabel di dalamnya memenuhi kriteria suatu kondisi atau tidak. Jika memenuhi kriteria, kondisi tersebut bernilai true. Jika tidak memenuhi kriteria, kondisi akan bernilai false. Jika kondisi if bernilai true, kode yang berada dalam blok kode if akan dieksekusi.

! ELIF
Elif merupakan kependekan dari else if dan alternatif untuk if bertingkat atau switch case. Elif statement berada pada posisi setelah if. Anda dapat menambahkan elif statement lebih dari satu karena tidak dibatasi dan opsional.

! ELSE
Else adalah statement yang menjadi jalan keluar saat kondisi atau hasil evaluasi if statement bernilai false. Maksudnya adalah program akan menjalani blok kode if terlebih dahulu dan jika hasilnya adalah false, program akan menjalankan else statement sebagai jalan keluar atau kondisi terakhir.
"""

# TODO : Contoh Kode Percabangan 1
ketersediaan_barang = "Daging Ayam"

if ketersediaan_barang == "Daging Ayam":
    print("Saya akan membeli 1 kg daging ayam")
else:
    print("Saya tidak akan membeli daging ayam")


# TODO : Contoh Kode Percabangan 2
tinggi_badan = 150

if tinggi_badan >= 150:
    print("Tinggi badan anda sudah memenuhi syarat pendaftaran")
elif tinggi_badan >= 140:
    print("Tinggi badan anda hampir memenuhi syarat pendaftaran")
else:
    print("Tinggi badan anda belum memenuhi syarat pendaftaran")


"""
! TERNARY OPERATOR

Ternary operators termasuk conditional expressions pada Python. Conditional expressions adalah bentuk ekspresi yang bertujuan untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasil evaluasinya. Anda bisa asumsikan bahwa ternary operators ini merupakan versi one-liner dari if dan else. 

Ternary operators dibangun dengan menempatkan "blok kode jika benar" pada posisi awal, lalu diikuti oleh "if statement" serta "kondisi"-nya. Kemudian "else statement" ditempatkan di akhir beserta dengan "blok kode jika salah".
"""

lulus = True
print("Selamat") if lulus else print("Coba lagi")


# TODO : Contoh kode ternary operator yang melibatkan tuple
kelulusan = True
print(("Maaf, anda Tidak Lulus", "Selamat, anda lulus")[kelulusan])
