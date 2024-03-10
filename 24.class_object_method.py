# TODO class : Pembuatan class dalam Python mirip seperti fungsi, yakni perlu menggunakan keyword untuk bisa membuatnya. Keyword atau kata kunci untuk membuat kelas dalam Python adalah "class".


# class Mobil:
#     # atribut
#     warna = "merah"

#     # method
#     def start(self):
#         print("Mobil menyala")

#     def stop(self):
#         print("Mobil berhenti")

#     def belok(self, arah):
#         print(f"Mobil belok ke {arah}")

#     def klakson(self):
#         print("Tin! Tin!")

#     # atribut instance
#     def __init__(self):
#         self.warna = "biru"


# # Membuat instance dari kelas Mobil
# mobil1 = Mobil()
# print(mobil1.warna)  # Output: merah

# mobil1.start()  # Output: Mobil menyala
# mobil1.stop()  # Output: Mobil berhenti
# mobil1.belok("kanan")  # Output: Mobil belok ke kanan
# mobil1.klakson()  # Output: Tin! Tin!


class Mobil:
    # Atribut
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    # Method
    def start(self):
        print("Mobil menyala")

    def stop(self):
        print("Mobil berhenti")

    def belok(self, arah):
        print(f"Mobil belok ke {arah}")

    def klakson(self):
        print("Tin! Tin!")


# Membuat instance dari kelas Mobil
mobil1 = Mobil("merah", "Toyota", 100)
print(mobil1.warna)  # Output: merah
print(mobil1.merek)  # Output: Toyota
print(mobil1.kecepatan)  # Output: 100

mobil1.start()  # Output: Mobil menyala
mobil1.stop()  # Output: Mobil berhenti
mobil1.belok("kanan")  # Output: Mobil belok ke kanan
mobil1.klakson()  # Output: Tin! Tin!


# TODO : Inheritance
# Inheritance atau pewarisan adalah konsep dalam pemrograman berorientasi objek yang memungkinkan sebuah kelas (kelas anak) untuk mewarisi properti dan metode dari kelas lain (kelas induk). Dalam Python, kelas anak atau turunan dapat mewarisi properti dan metode dari kelas induk atau parent class dengan cara menuliskan nama kelas induk di dalam tanda kurung setelah nama kelas anak.


# Contoh inheritance
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def description(self):
        return f"{self.name} adalah {self.species} berumur {self.age} tahun"


class Cat(Animal):
    def sound(self):
        return "meow!"

    def description(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"


# Membuat instance dari kelas Cat
myCat = Cat("Neko", 3, "Persian")
print(myCat.description())
