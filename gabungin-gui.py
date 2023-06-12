# def login(name,pasword):
#     Berhasil = False
#     file = open("base.txt", "r")
#     for i in file:
#         x,y = i.split(",")
#         y = y.strip()
#         if(x == name and y == pasword):
#             Berhasil = True
#             break
#     file.close()
#     if(Berhasil):
#         print("login sukses")
#     else:
#         print("Anda belum memiliki akun, silahkan registrasi akun")
# def registrasi(name,pasword):
#     file = open("base.txt", "a")
#     file.write("\n"+name+","+pasword)

# def access(option):
#     global name 
#     if(option == "login"):
#         name = input ("Masukkan ID : ")
#         pasword = input ("Masukkan pasword : ")
#         login(name,pasword)
#     else : 
#         print ("Masukkan ID dan Paword anda : ")
#         name = input("Masukkan ID : ")
#         pasword = input("Masukkan pasword : ")
#         registrasi(name,pasword)
#         print("Registrasi anda berhasil")

# def begin():
#     global option
#     print("Selamat datang di program kami")
#     print("silahkan pilih 'login' jika sudah memiliki akun")
#     print("silahkan pilih 'reg' jika belum memiliki akun")
#     option = input("silahkan pilih (log/reg)")
#     if(option != "login" and option != "reg"):
#         begin()

# begin()
# access(option)

#ini dibuat gui sabi
#credit anggito
import random
import json
from tabulate import tabulate
with open('bismillah.json', encoding='utf-8')as f:
    data = json.load(f)

#daftar resto 
namaresto = []
for restoran in data:
    if restoran['restoran']['harga']in ['$','$$','$$$','$$$$']:
        namaresto.append([restoran['restoran']['nama'],restoran['restoran']['desc'],restoran['restoran']['rekomen'],restoran['restoran']['alamat'],restoran['restoran']['jam']['peak'],restoran['restoran']['jam']['operasional'],restoran['restoran']['harga']])

#datar resto jadi kecil
resto_lower = [element[0].lower() for element in namaresto]
harga1='$'
harga2 = '$$'
harga3 = '$$$'
harga4 = '$$$$'

def tanya_filter1():

    while True:
        try:
            filter1 = input("Masukkan jenis restoran")
            assert filter1.lower() in ["asia", "barat", "timur tengah", "any"], "Input tidak valid"
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
            assert filter2.lower() in ['$', '$$', '$$$', '$$$$', "any"], "Input tidak valid"
            break
        except AssertionError as er:
            print(er)
    if filter2.lower() == "any":
        return ["$", "$$", "$$$", "$$$$"]
    else:
        return filter2.lower()

filter1 = tanya_filter1()
filter2 = tanya_filter2()

restofilter = []
for restoran in data:
    if restoran['restoran']['harga'] in filter2 and restoran['restoran']['tipe'] in filter1:
        restofilter.append([ restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga'] ])
        random.shuffle(restofilter)
        
print(tabulate(restofilter[:5], headers=["Nama", "tipe", "harga"]))

# #perulangan nyari resto
# search = input("Ingin menelusuri Restoran? y/n ")
# if search.lower()== 'y':
#     print('='*50)
#     print('Selamat datang ke menu pencarian')
#     print('='*50)
#     search = True
# else:
#     print('-'*50)
#     print('Terima kasih telah menggunakan program kami')
#     search = False

# #input resto
# while search:
#     find = input("Masukkan nama Restoran: ")
#     counter = 0
#     for resto in resto_lower:
#         if resto.startswith(find.lower()):
#             index = resto_lower.index(resto)
#             print(f'Nama Restoran\n{namaresto[index][0]}')
#             print('-'*75)
#             print(f'Deskripsi\n{namaresto[index][1]}')
#             print('-'*300)
#             print(f'Recommended Menu\n{namaresto[index][2]}')
#             print('-'*75)
#             print(f'Alamat Restoran\n{namaresto[index][3]}')
#             print('-'*150)
#             print(f'Peak hour\n{namaresto[index][4]}')
#             print('-'*75)
#             print(f'Jam Operasional \n{namaresto[index][5]}')
#             print('-'*75)
#             print(f'Range Harga Restoran \n{namaresto[index][6]}')
#             print('='*75)
#             counter += 1
#     if counter == 0:
#         print('='*50)
#         print("Resto tidak tersedia")
#         print('='*50)
    
#     #input lagi ga
#     search = input("Ingin menelusuri restoran lagi? y/n ")
#     if search.lower() == 'y':
#         search = True
#     else:
#         print('-'*50)
#         print('Terima kasih telah menggunakan program kami')
#         search = False