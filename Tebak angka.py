import random

angka_tertinggi = input("Masukan angka tertinggi : ") # Menentukan angka tertinggi untuk ditebak

if angka_tertinggi.isdigit(): # Memastikan angka tertinggi yang dimasukan adalah angka bukan huruf
    angka_tertinggi = int(angka_tertinggi)
    if angka_tertinggi <= 0 : # Memastikan angka diatas 0
        print("Masukan angka diatas 0 !!!")
        quit()
else:
    print("Masukan angka!!!")
    quit()

random_angka = random.randint(0, angka_tertinggi) # Membuat angka acak yang harus ditebak
banyak_tebakan = 0 # variabel banyak nya tebakan yang dilakukan

while True :
    tebakan = input("Masukan angka tebakan mu : ") # Memasukan angka tebakan
    if tebakan.isdigit(): # Memastikan angka tebakan adalah angka buka huruf
        tebakan = int(tebakan)
    else:
        print("Harap masukan angka !!!")
        continue

    if tebakan == random_angka : # Memastikan angka tebakan dan angaka acak sama atau tidak
        banyak_tebakan += 1 # Menambah angka tebakan ke variabel banyak tebakan.
        print("Tebakan kamu benar !")
        break
    elif tebakan > random_angka:
        print("Tebakan mu diatas angka")
    else:
        print("Tebakan mu dibawah angka")

print("Kamu sudah menebak sebanyak "+str(banyak_tebakan)+ " kali.") # Menampilkan banyak tebakan sampai berhasil sama
