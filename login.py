def login(name,pasword):
    Berhasil = False
    file = open("base.txt", "r")
    for i in file:
        x,y = i.split(",")
        y = y.strip()
        if(x == name and y == pasword):
            Berhasil = True
            break
    file.close()
    if(Berhasil):
        print("login sukses")
    else:
        print("Anda belum memiliki akun, silahkan registrasi akun")
def registrasi(name,pasword):
    file = open("base.txt", "a")
    file.write("\n"+name+","+pasword)

def access(option):
    global name 
    if(option == "login"):
        name = input ("Masukkan ID : ")
        pasword = input ("Masukkan pasword : ")
        login(name,pasword)
    else : 
        print ("Masukkan ID dan Paword anda : ")
        name = input("Masukkan ID : ")
        pasword = input("Masukkan pasword : ")
        registrasi(name,pasword)
        print("Registrasi anda berhasil")

def begin():
    global option
    print("Selamat datang di program kami")
    print("silahkan pilih 'login' jika sudah memiliki akun")
    print("silahkan pilih 'reg' jika belum memiliki akun")
    option = input("silahkan pilih (log/reg)")
    if(option != "login" and option != "reg"):
        begin()

begin()
access(option)