"""
TODO : Pemrosesan data sekuensial menggunakan array
pemrosesan sekuensial adalah sebuah pemrosesan setiap elemen array yang dimulai dari elemen pada indeks terkecil hingga terbesar. Pemrosesan sekuensial lebih sering menggunakan pengulangan (loop/iterasi) dalam setiap prosesnya.

Sebab pemrosesan sekuensial melibatkan semua elemen di dalamnya, ada beberapa hal yang perlu diperhatikan.

- Setiap elemen array diakses secara langsung melalui indeksnya (metode indexing).
- Elemen pertama (first element) adalah elemen array dengan indeks terkecil yang selalu dimulai dari 0. 
- Elemen selanjutnya (next element) dicapai melalui suksesor indeks.
- Kondisi berhenti dicapai jika indeks yang diproses adalah indeks terbesar yang sudah terdefinisi.
- Suatu array tidak boleh kosong, minimal memiliki satu elemen di dalamnya.
"""

# Contoh Kode Pemrosesan Sekuensial
var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next elements: {next_element}")
