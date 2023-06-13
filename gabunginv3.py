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
#         print('='*50)
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
#     print('='*50)
#     print("silahkan pilih 'login' jika sudah memiliki akun")
#     print('-'*50)
#     print("silahkan pilih 'reg' jika belum memiliki akun")
#     print('='*50)
#     option = input("silahkan pilih (log/reg)")
#     if(option != "login" and option != "reg"):
#         begin()

# begin()
# access(option)

#perulangan kelar insyaAllah no problem
import json
from tabulate import tabulate
with open('bismillah.json', encoding='utf-8')as f:
    data = json.load(f)

import random

#daftar resto 
namaresto = []
for restoran in data:
    if restoran['restoran']['harga']in ['$','$$','$$$','$$$$']:
        namaresto.append([restoran['restoran']['nama'],restoran['restoran']['desc'],restoran['restoran']['rekomen'],restoran['restoran']['alamat'],restoran['restoran']['jam']['peak'],restoran['restoran']['jam']['operasional'],restoran['restoran']['harga']])

#datar resto jadi kecil
resto_lower = [element[0].lower() for element in namaresto]

#daftar restoran Asia $
restoasia1 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$' and restoran['restoran']['tipe']== 'asia':
        restoasia1.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran Asia $$
restoasia2 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$' and restoran['restoran']['tipe']== 'asia':
        restoasia2.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran Asia $$$
restoasia3 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$' and restoran['restoran']['tipe']== 'asia':
        restoasia3.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran Asia $$$$
restoasia4 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$$' and restoran['restoran']['tipe']== 'asia':
        restoasia4.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran Barat $
restobarat1 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$' and restoran['restoran']['tipe']== 'barat':
        restobarat1.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran Barat $$
restobarat2 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$' and restoran['restoran']['tipe']== 'barat':
        restobarat2.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran Barat $$$
restobarat3 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$' and restoran['restoran']['tipe']== 'barat':
        restobarat3.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran Barat $$$$
restobarat4 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$$' and restoran['restoran']['tipe']== 'barat':
        restobarat4.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran timur $
restotimur1 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$' and restoran['restoran']['tipe']== 'timur tengah':
        restotimur1.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran timur $$
restotimur2 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$' and restoran['restoran']['tipe']== 'timur tengah':
        restotimur2.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran timur $$$
restotimur3 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$' and restoran['restoran']['tipe']== 'timur tengah':
        restotimur3.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran timur $$$$
restotimur4 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$$' and restoran['restoran']['tipe']== 'timur tengah':
        restotimur4.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran asia
restoasia0 = []
for restoran in data:
    if restoran['restoran']['harga'] in ['$','$$','$$$','$$$$'] and restoran['restoran']['tipe']== 'asia':
        restoasia0.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restoasia0)

#daftar restoran barat
restobarat0 = []
for restoran in data:
    if restoran['restoran']['harga'] in ['$','$$','$$$','$$$$'] and restoran['restoran']['tipe']== 'barat':
        restobarat0.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restobarat0)

#daftar restoran timur
restotimur0 = []
for restoran in data:
    if restoran['restoran']['harga'] in ['$','$$','$$$','$$$$'] and restoran['restoran']['tipe']== 'timur tengah':
        restotimur0.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restotimur0)

#daftar restoran $
restoharga1 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$' and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restoharga1.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restoharga1)

#daftar restoran $$
restoharga2 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$' and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restoharga2.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restoharga2)

#daftar restoran $$$
restoharga3 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$' and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restoharga3.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restoharga3)

#daftar restoran $$$$
restoharga4 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$$' and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restoharga4.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restoharga4)

#daftar restoran full
restosemua = []
for restoran in data:
    if restoran['restoran']['harga'] in ['$','$$','$$$','$$$$'] and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restosemua.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])
        random.shuffle(restosemua)

#start code 

print("         Food Travels : Surakarta Edition")
print('='*50)
print('Showing recommended restaurants around Surakarta')
print('='*50)
print('Selamat Datang ke Menu Utama')
print('-'*50)
print('Program ini menyediakan :')
print('1. Filter Jenis Restoran')
print('Asia/Barat/Timur Tengah')
print('2. Filter Range Harga Restoran')
print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)')
print('3. Pencarian Restoran')

#main code
filterutama=input('Apakah anda ingin menggunakan Filter Restoran?    y/n')
if filterutama.lower()== 'y':
    tanyajenis = input('Apakah anda ingin menggunakan filter jenis restoran?    y/n')
    if tanyajenis.lower()=='y':
        print('='*50)
        print('Selamat datang pada filter jenis restoran')
        print('='*50)
        print('Asia/Barat/Timur Tengah')
        while True: 
            jenisresto = input('Masukkan tipe jenis restoran.      Asia, Barat, Timur Tengah')
            if jenisresto.lower() in ['asia', 'barat', 'timur tengah']:
                tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
                if tanyaharga.lower()=='y':
                    print('='*50)
                    print('Selamat datang pada filter harga restoran')
                    print('='*50)
                    print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)')
                    #break
                    #maybe insert here
                    while True:
                        hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
                        if jenisresto == 'asia' and hargaresto == '$':
                            print(tabulate(restoasia1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'asia' and hargaresto == '$$':
                            print(tabulate(restoasia2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'asia' and hargaresto == '$$$':
                            print(tabulate(restoasia3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'asia' and hargaresto == '$$$$':
                            print(tabulate(restoasia4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'barat' and hargaresto == '$':
                            print(tabulate(restobarat1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'barat' and hargaresto == '$$':
                            print(tabulate(restobarat2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'barat' and hargaresto == '$$$':
                            print(tabulate(restobarat3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'barat' and hargaresto == '$$$$':
                            print(tabulate(restobarat4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'timur tengah' and hargaresto == '$':
                            print(tabulate(restotimur1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'timur tengah' and hargaresto == '$$':
                            print(tabulate(restotimur2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'timur tengah' and hargaresto == '$$$':
                            print(tabulate(restotimur3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        elif jenisresto == 'timur tengah' and hargaresto == '$$$$':
                            print(tabulate(restotimur4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                            break
                        else:
                            print('range harga tidak tersedia')             
                else:
                    print('='*50)
                    print('Anda tidak memilih range harga restoran')
                    print('='*50)
                    if jenisresto == 'asia':
                        print(tabulate(restoasia0[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                        break
                    elif jenisresto == 'barat':
                        print(tabulate(restobarat0[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                        break
                    elif jenisresto == 'timur tengah':
                        print(tabulate(restotimur0[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                        break      
            else:
                print("Jenis Restoran tidak tersedia")
    else:
        print('='*50)
        print('Anda tidak memilih jenis restoran')
        print('='*50)
        tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
        if tanyaharga.lower()=='y':
            print('='*50)
            print('Selamat datang pada filter harga restoran')
            print('='*50)
            print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)')
            while True:
                hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
                if hargaresto == '$':
                    print(tabulate(restoharga1[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    break
                elif hargaresto == '$$':
                    print(tabulate(restoharga2[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    break
                elif hargaresto == '$$$':
                    print(tabulate(restoharga3[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    break
                elif hargaresto == '$$$$':
                    print(tabulate(restoharga4[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl")) 
                    break
                else:
                    print("Range harga tidak tersedia")
        else:
            print('='*50)
            print('Anda tidak memilih range harga restoran')
            print('='*50)
            print(tabulate(restosemua[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
else:
    print('Anda tidak menggunakan filter')
    print(tabulate(restosemua[:5],headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))

#problem
#code part 2
# while True:
#     hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
#     if jenisresto == 'asia' and hargaresto == '$':
#         print(tabulate(restoasia1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'asia' and hargaresto == '$$':
#         print(tabulate(restoasia2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'asia' and hargaresto == '$$$':
#         print(tabulate(restoasia3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'asia' and hargaresto == '$$$$':
#         print(tabulate(restoasia4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'barat' and hargaresto == '$':
#         print(tabulate(restobarat1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'barat' and hargaresto == '$$':
#         print(tabulate(restobarat2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'barat' and hargaresto == '$$$':
#         print(tabulate(restobarat3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'barat' and hargaresto == '$$$$':
#         print(tabulate(restobarat4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'timur tengah' and hargaresto == '$':
#         print(tabulate(restotimur1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'timur tengah' and hargaresto == '$$':
#         print(tabulate(restotimur2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'timur tengah' and hargaresto == '$$$':
#         print(tabulate(restotimur3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     elif jenisresto == 'timur tengah' and hargaresto == '$$$$':
#         print(tabulate(restotimur4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
#         break
#     else:
#         print('range harga tidak tersedia')
    

#perulangan nyari resto
search = input("Ingin menelusuri Restoran? y/n     = ")
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
    find = input("Masukkan nama Restoran:   ")
    counter = 0
    for resto in resto_lower:
        if find.lower() in resto:
            index = resto_lower.index(resto)
            print('='*50)
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
    search = input("Ingin menelusuri restoran lagi? y/n     = ")
    if search.lower() == 'y':
        search = True
    else:
        search = False
        