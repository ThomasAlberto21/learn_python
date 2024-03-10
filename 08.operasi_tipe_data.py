# List
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 7, 7]
print(contoh_list)
# len(mengembalikan panjang (jumlah elemen) dari suatu list.)
print(len(contoh_list))
# min(mengembalikan nilai terkecil dari suatu list.)
print(min(contoh_list))
# max(mengembalikan nilai terbesar dari suatu list.)
print(max(contoh_list))
# count(mengetahui berapa kali suatu objek muncul dalam list.)
print(contoh_list.count(5))


kalimat = "Dicoding Indonesia"
# in(mengecek apakah suatu objek ada dalam list.)
print("Dicoding" in kalimat)  # Output: True
# not in(mengecek apakah suatu objek tidak ada dalam list.)
print("University" not in kalimat)  # Output: True

# TODO Memberikan nilai untuk multiple variable
data = ["shirt", "white", "L"]
apparel = data[0]
color = data[1]
size = data[2]
print(apparel)  # Output: shirt
print(color)  # Output: white
print(size)  # Output: L

# sort(mengurutkan elemen dalam list.)
list_sort = [100, 1000, 500, 200, 5]
list_sort.sort()
print(list_sort)  # Output: [5, 100, 200, 500, 1000]