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

#ini dibuat gui sabi
#credit a
import random
import json
from tabulate import tabulate
with open('bismillah.json', encoding='utf-8')as f:
    data = json.load(f)

#beberapa list resto
restosemua = []
for restoran in data:
    if restoran['restoran']['harga'] in ['$','$$','$$$','$$$$'] and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restosemua.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restosemua)

#daftar resto 
namaresto = []
for restoran in data:
    if restoran['restoran']['harga']in ['$','$$','$$$','$$$$']:
        namaresto.append([restoran['restoran']['nama'],restoran['restoran']['desc'],restoran['restoran']['rekomen'],restoran['restoran']['alamat'],restoran['restoran']['jam']['peak'],restoran['restoran']['jam']['operasional'],restoran['restoran']['harga']])

#datar resto jadi kecil
resto_lower = [element[0].lower() for element in namaresto]

print("         Food Travels : Surakarta Edition")
print('='*50)
print('Showing recommended restaurants around Surakarta')
print('='*50)
print('Selamat Datang ke Menu Utama')
print('-'*50)
print('Program ini menyediakan :')
print('1. Filter Jenis Restoran')
print('Asia/Barat/Timur Tengah/Any')
print('2. Filter Range Harga Restoran')
print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)/Any')
print('3. Pencarian Restoran')

#list def
def tanya_filter1():
    while True:
        try:
            filter1 = input("Masukkan jenis restoran")
            assert filter1.lower() in ["asia", "barat", "timur tengah", "any"], "Jenis restoran tidak tersedia"
            break
        except AssertionError as er:
            print(er)
    if filter1.lower() == "any":
        return ["asia", "barat", "timur tengah"]
    else:
        return filter1.lower()

def tanya_filter2():
    while True:
        try:
            filter2 = input("Masukkan range harga restoran")
            assert filter2.lower() in ['$', '$$', '$$$', '$$$$', "any"], "Range harga tidak tersedia"
            break
        except AssertionError as er:
            print(er)
    if filter2.lower() == "any":
        return ["$", "$$", "$$$", "$$$$"]
    else:
        return filter2.lower()

# filter1 = tanya_filter1()
# filter2 = tanya_filter2()    


#main code
filterutama=input('Apakah anda ingin menggunakan Filter Restoran?    y/n')
if filterutama.lower()== 'y':
    tanyajenis = input('Apakah anda ingin menggunakan filter jenis restoran?    y/n')
    if tanyajenis.lower()=='y':
        print('='*50)
        print('Selamat datang pada filter jenis restoran')
        print('='*50)
        print('Asia/Barat/Timur Tengah/Any')
        filter1 = tanya_filter1()
        tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
        if tanyaharga.lower()=='y':
            print('='*50)
            print('Selamat datang pada filter harga restoran')
            print('='*50)
            print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)/Any')
            filter2 = tanya_filter2()
            restofilter = []
            for restoran in data:
                if restoran['restoran']['harga'] in filter2 and restoran['restoran']['tipe'] in filter1:
                    restofilter.append([ restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga'] ])
                    random.shuffle(restofilter)
            print(tabulate(restofilter[:5], headers=["Nama", "tipe", "harga"]))
        else:
            print('Anda tidak memilih range harga')
            resto1filter1 = []
            for restoran in data:
                if restoran['restoran']['tipe'] in filter1:
                    resto1filter1.append([ restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga'] ])
                    random.shuffle(resto1filter1)
            print(tabulate(resto1filter1[:5], headers=["Nama", "tipe", "harga"]))
    else:
        print('='*50)
        print('Anda tidak menggunakan filter jenis restoran')
        print('='*50)
        tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
        if tanyaharga.lower()=='y':
            print('='*50)
            print('Selamat datang pada filter harga restoran')
            print('='*50)
            print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)/Any')
            filter2 = tanya_filter2()
            resto1filter2 = []
            for restoran in data:
                if restoran['restoran']['harga'] in filter2:
                    resto1filter2.append([ restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga'] ])
                    random.shuffle(resto1filter2)
            print(tabulate(resto1filter2[:5], headers=["Nama", "tipe", "harga"]))
        else:
            print('='*50)
            print('Anda tidak memilih range harga restoran')
            print('='*50)
            print(tabulate(restosemua[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
else: 
    print('Anda tidak menggunakan filter')
    print(tabulate(restosemua[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            

#perulangan nyari resto
search = input("Ingin menelusuri Restoran? y/n ")
if search.lower()== 'y':
    print('='*50)
    print('Selamat datang ke menu pencarian')
    print('='*50)
    search = True
else:
    print('-'*50)
    print('Terima kasih telah menggunakan program kami')
    search = False

#input resto
while search:
    find = input("Masukkan nama Restoran: ")
    counter = 0
    for resto in resto_lower:
        if resto.startswith(find.lower()):
            index = resto_lower.index(resto)
            print(f'Nama Restoran\n{namaresto[index][0]}')
            print('-'*75)
            print(f'Deskripsi\n{namaresto[index][1]}')
            print('-'*300)
            print(f'Recommended Menu\n{namaresto[index][2]}')
            print('-'*75)
            print(f'Alamat Restoran\n{namaresto[index][3]}')
            print('-'*150)
            print(f'Peak hour\n{namaresto[index][4]}')
            print('-'*75)
            print(f'Jam Operasional \n{namaresto[index][5]}')
            print('-'*75)
            print(f'Range Harga Restoran \n{namaresto[index][6]}')
            print('='*75)
            counter += 1
    if counter == 0:
        print('='*50)
        print("Resto tidak tersedia")
        print('='*50)
    
    #input lagi ga
    search = input("Ingin menelusuri restoran lagi? y/n ")
    if search.lower() == 'y':
        search = True
    else:
        print('-'*50)
        print('Terima kasih telah menggunakan program kami')
        search = False