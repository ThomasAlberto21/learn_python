# TODO : Latihan array untuk mencari nilai terbesar dalam suatu array

var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(f"Nilai terbesar dalam array adalah {left_pointer}")
