"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""

# Jangan ubah kode ini
dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.
if dico > 500000:
    total_harga = dico - (dico * 0.1)
    print(total_harga)
