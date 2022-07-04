import random

from pyparsing import And

pemain_menang = 0
computer_menang = 0
suit = ["gunting", 'kertas', 'batu']

print("Selamat bermain permainan suit gunting kerts batu.")

while True :
    pilihan_pemain = input("Masukan pilihan Gunting/Kertas/Batu untuk bermain ATAU Quit/Q untuk keluar : ").lower()
    if pilihan_pemain == "q":
        break
    
    if pilihan_pemain not in suit:
        continue

    random_number = random.randint(0,2)
    # gunting : 0, kertas : 1, batu : 2

    pilihan_computer = suit[random_number]
    print("Komputer memilih", pilihan_computer+".")

    if pilihan_pemain == "gunting" and pilihan_computer == "kertas":
        pemain_menang += 1
        print("Pemain menang !")
    elif pilihan_pemain == "kertas" and pilihan_computer == "batu":
        pemain_menang += 1
        print("Pemain menang !")
    elif pilihan_pemain == "batu" and pilihan_computer == "kertas":
        pemain_menang += 1
        print("Pemain menang !")
    else:
        computer_menang += 1
        print("Komputer menang !")
        
print("Pemain berhasil menang "+ str(pemain_menang)+" kali")
print("Komputer berhasil menang "+ str(computer_menang)+" kali")
print("Selamat tinggal !")