import random

pemain_menang = 0 #Variabel pemain menang suit
computer_menang = 0 #variabel komputer menang suit
suit = ["gunting", 'kertas', 'batu'] #list pilihan suit

print("Selamat bermain permainan suit gunting kerts batu.")

while True :
    pilihan_pemain = input("Masukan pilihan Gunting/Kertas/Batu untuk bermain ATAU Quit/Q untuk keluar : ").lower() #pemain memilih suit atau keluar dari permainan
    if pilihan_pemain == "q": #jika memilih keluar akan break
        break
    
    if pilihan_pemain not in suit:
        continue

    random_number = random.randint(0,2) #suit akan diacak
    # gunting : 0, kertas : 1, batu : 2

    pilihan_computer = suit[random_number] #Menentukan pilihan komputer
    print("Komputer memilih", pilihan_computer+".")

    #validasi siapa yang menang suit
    if pilihan_pemain == "gunting" and pilihan_computer == "kertas": 
        pemain_menang += 1 #menambah poin ke pemain
        print("Pemain menang !")
    elif pilihan_pemain == "kertas" and pilihan_computer == "batu":
        pemain_menang += 1
        print("Pemain menang !")
    elif pilihan_pemain == "batu" and pilihan_computer == "kertas":
        pemain_menang += 1
        print("Pemain menang !")
    elif pilihan_pemain == pilihan_computer: #kalo seri
        print("Seri !!!")
    else:
        computer_menang += 1 #menambah poin ke komputer
        print("Komputer menang !")

print("Pemain berhasil menang "+ str(pemain_menang)+" kali") #menampilkan poin pemain
print("Komputer berhasil menang "+ str(computer_menang)+" kali") #menampilkan poin komputer
print("Selamat tinggal !")