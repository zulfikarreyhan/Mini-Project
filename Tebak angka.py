import random

angka_tertinggi = input("Masukan angka tertinggi : ")

if angka_tertinggi.isdigit():
    angka_tertinggi = int(angka_tertinggi)
    if angka_tertinggi <= 0 :
        print("Masukan angka diatas 0 !!!")
        quit()
else:
    print("Masukan angka!!!")
    quit()

random_angka = random.randint(0, angka_tertinggi)
banyak_tebakan = 0

while True :
    tebakan = input("Masukan angka tebakan mu : ")
    if tebakan.isdigit():
        tebakan = int(tebakan)
    else:
        print("Harap masukan angka !!!")
        continue

    if tebakan == random_angka :
        banyak_tebakan += 1
        print("Tebakan kamu benar !")
        break
    elif tebakan > random_angka:
        print("Tebakan mu diatas angka")
    else:
        print("Tebakan mu dibawah angka")

print("Kamu sudah menebak sebanyak "+str(banyak_tebakan)+ " kali.")
