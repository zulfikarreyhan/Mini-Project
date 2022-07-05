nama = input("Siapa nama anda : ") # Nama pemain

print("Selamat datang di permainan petualangan !!!")

pilihan = input("Pilih peta. Lautan/Pegunungan/Labirin/Hutan? ").lower() # Memili peta

if pilihan == "hutan" : #Alur petualangan di hutan
    print("Anda memasuki hutan yang sangat lebat. ")
    pilihan = input("Terdapat dua jalur. (kanan/kiri): ").lower()

    if pilihan == "kanan": #verifikasi pilihan
        print("Anda bertemu dengan ular besar. Anda mati terlilit.")
    elif pilihan == "kiri":
        print("Anda berhasil sampai di pemukiman warga. Anda menang.")
    else:
        print("Anda tidak memilih. Anda keluar permainan")
elif pilihan == "lautan": #Alur petualangan di laut
    print("Anda berada di lautan yang sangat luas dan tenang.")
    pilihan = input("Kompas anda menunjukan arah. (utara/selatan): ").lower()

    if pilihan == "utara": #verifikasi pilihan
        print("Anda menghadapi badai yang sangat besar. Anda mati tenggelam dilaut.")
    elif pilihan == "selatan":
        print("Anda berhasil menemukan pulau. Anda menang.")
    else:
        print("Anda tidak memilih. Anda keluar permainan")
elif pilihan == "labirin": #Alur petualangan di labirin
    pilihan = input("Anda terjebak didalam labirin.\nTerdapat dua jalur di depan mu. (kanan/kiri): ").lower()

    if pilihan == "kanan": #verifikasi pilihan
        print("Anda menemukan jalan buntu. Anda mati kelaparan.")
    elif pilihan == "kiri":
        print("Anda berhasil menemukan pintu. Anda menang.")
    else:
        print("Anda tidak memilih. Anda keluar permainan")
elif pilihan == "pegunungan": #Alur petualangan di pegunungan
    pilihan = input("Anda berada di pegunungan yang sangat dingin dan terjal.\nApa yang ada akan lakukan (maju/bermalam): ").lower()

    if pilihan == "maju": #verifikasi pilihan
        print("Anda ditemukan oleh warga dan berhasil diselamatkan. Anda menang.")
    elif pilihan == "bermalam":
        print("Anda menghadapi badai yang sangat besar. Anda mati kedinginan.")
    else:
        print("Anda tidak memilih. Anda keluar permainan")
else :
    print("Anda tidak memilih. Anda keluar permainan")

print("Terima kasih sudah mencoba permainan petualangan sederhana ini. Selamat tinggal", nama)