print("Selamat datang di permainan kuis !!!")

play = input("Apakah anda mau bermain kuis ? ") #Mengkonfirmasi mau bermain
if play.lower() != "iya":
    quit()

print("Selamat Bermain !")
poin = 0 #point jika jawaban benar

jawaban = input("Siapa Hokage Petama Konoha ? ")#Pertanyaan pertama
if jawaban.lower() == "hasirama senju": #Konformasi jawaban pertama
    print("Benar !")
    poin += 1
else:
    print("Salah!")

jawaban = input("Siapa Jincuriki Kyubi ? ")#Pertanyaan kedua
if jawaban.lower() == "naruto uzumaki" or "uzumaki naruto": #Konformasi jawaban kedua
    print("Benar !")
    poin += 1
else:
    print("Salah!")

jawaban = input("Siapa Hokage Kedua Konoha ? ")#Pertanyaan ketiga
if jawaban.lower() == "minato": #Konformasi jawaban ketiga
    print("Benar !")
    poin += 1
else:
    print("Salah!")

print("Anda berhasil menjawab "+str(poin)+" pertanyaan")#nampilin jumlah jawaban yang benar
print("Anda berhasil "+str(poin/3*100)+"%")#nampilin dalam persen
