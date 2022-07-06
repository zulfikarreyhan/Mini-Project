print("PENYMPANAN PASSWORD")
def tambah (): #fungsi menambahkan akun dan password
    nama = input("Nama akun: ")
    pwd = input("Masukan password: ")

    with open('password.text', 'a') as f:
        f.write(nama + "|" + pwd + "\n")

def lihat (): #fungsi melihat akun dan password
    with open('password.text', 'r') as f:
        for line in f.readlines():
            pw = line.rstrip()
            nama, pwd = pw.split("|")
            print("Nama akun:", nama, "| Password:",pwd)

while True : #perulangan aplikasi
    awal = input("tambah untuk menambahkan password, lihat untuk melihat password, q untuk keluar. (tambah/lihat/q): ").lower()
    if awal == "q":
        print("Terima Kasih.")
        break
    elif awal == "tambah":
        tambah()
    elif awal == "lihat":
        lihat()
    else:
        print("Yang anda masukan salah. Ketik yang benar.")
        continue