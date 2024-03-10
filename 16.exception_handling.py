"""
TODO : exception handling
 Program Python yang Anda bangun dapat dilengkapi penanganan terhadap pengecualian dari tipe kesalahan yang Anda tentukan. Konsep ini dikenal dengan exceptions handling yang menggunakan pernyataan try-except untuk menangani pengecualian tersebut.
"""

# Contoh Kode Exception Handling
z = 0
try:  # Blok kode yang mungkin terjadi pengecualian
    print(1 / z)
except ZeroDivisionError:  # Blok kode yang akan dieksekusi jika terjadi pengecualian
    print("Tidak bisa membagi angka dengan nol")
else:  # Blok kode yang akan dieksekusi jika tidak terjadi pengecualian
    print("Tidak ada pengecualian")
finally:  # Blok kode yang akan dieksekusi setelah blok try selesai dieksekusi
    print("Eksekusi blok kode try selesai")


"""
TODO : raise exception
Jika sebelumnya kita menangani kesalahan yang TIDAK DISENGAJA, kali ini kita akan mempelajari cara menangani kesalahan yang DISENGAJA. Umumnya, ketika membuat kode program kita ingin membatasi program tersebut dengan kondisi tertentu.

Perlu diingat bahwa umumnya, raise digunakan bersamaan dengan if-else statement.

Misalnya, Anda ingin membuat kode program untuk menampilkan angka dari 1 hingga 10 berdasarkan input atau masukan pengguna. Namun, dalam program tersebut kita ingin mengontrol dengan cara berikut: jika user memberikan input berupa bilangan negatif, program akan memunculkan pesan error dengan keterangan "Bilangan negatif tidak diperbolehkan".
"""
var = -1
if var <= 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i)
