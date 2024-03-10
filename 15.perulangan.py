"""
TODO : for loop

For termasuk sintaks dalam Python yang bersifat definite iteration. Definite iteration adalah sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.

range(start , stop , step)
Berikut adalah penjelasan detail terkait fungsi "range()".

- "Start" merupakan nilai awal dari urutan bilangan yang bersifat opsional, jika Anda tidak memasukkannya, nilai awal akan dianggap 0. 
= "Stop" merupakan nilai batas yang wajib dimasukkan. Urutan akan berhenti sebelum mencapai nilai "stop" (eksklusif). 
- "Step" merupakan nilai penambahan antara setiap dua bilangan dalam urutan yang bersifat opsional. Jika nilai tersebut tidak diberikan, secara default nilai yang dimasukkan adalah 1.
"""

# Contoh Kode For Loop
for i in range(20):
    print(i)

for i in range(1, 20, 2):
    print(i)


"""
TODO : while loop

While termasuk sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.
"""

# Contoh Kode While Loop
counter = 1
while counter <= 10:
    print("Perulangan ke-", counter)
    counter += 1


"""
TODO : for bersarang / nested loop
"""

# Contoh Kode For Bersarang
for i in range(1, 3):
    for j in range(1, 3):
        print(f"Perulangan i ke-{i}, Perulangan j ke-{j}")


"""
TODO : break
Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya. Jika Anda memiliki perulangan yang bertingkat seperti for bersarang, break akan menghentikan perulangan sesuai dengan tingkatan atau letak perulangannya berada.
"""

# Contoh Kode Break
for i in range(2):  # Perulangan tingkat pertama
    print(f"Perulangan i ke-{i}")
    for j in range(3):  # Perulangan tingkat kedua
        print(f"Perulangan j ke-{j}")
        if j == 1:
            break  # Hentikan perulangan j jika sudah sampai angka 1


"""
TODO : continue
Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. Continue seolah mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok.
"""

# Contoh Kode Continue
for huruf in "Dico ding":
    if huruf == " ":
        continue
    print(f"Huruf sekarang: {huruf})")


"""
TODO : else setelah for
Pada Python juga dikenal else setelah for yang berfungsi untuk perulangan bersifat pencarian. Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.
"""

# Contoh Kode Else Setelah For
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        print("Angka 3 ditemukan")
        break
else:
    print("Angka 3 tidak ditemukan!")


"""
TODO : else setelah while
Berbeda dengan else setelah for, pada statement else setelah while, blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah.
"""

# Contoh Kode Else Setelah While
count = 0
while count <= 3:
    print(f"Perulangan ke-{count}")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")


"""
TODO : pass
Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.
"""

# Contoh Kode Pass
x = 10
if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")


"""
TODO : List Comprehension
Masih terkait perulangan, terkadang ada kalanya Anda perlu membuat sebuah list baru berdasarkan list yang sudah ada.
"""

# Contoh Kode List Comprehension
angka = [1, 2, 3, 4, 5]
pangkat = []

for n in angka:
    pangkat.append(n**2)
print(pangkat)


# Contoh Kode List Comprehension simple

angka = [1, 2, 3, 4, 5]
pangkat = [n**2 for n in angka]
print(pangkat)
