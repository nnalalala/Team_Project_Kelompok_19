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

#daftar restoran barat
restobarat0 = []
for restoran in data:
    if restoran['restoran']['harga'] in ['$','$$','$$$','$$$$'] and restoran['restoran']['tipe']== 'barat':
        restobarat0.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran timur
restotimur0 = []
for restoran in data:
    if restoran['restoran']['harga'] in ['$','$$','$$$','$$$$'] and restoran['restoran']['tipe']== 'timur tengah':
        restotimur0.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran $
restoharga1 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$' and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restoharga1.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran $$
restoharga2 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$' and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restoharga2.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran $$$
restoharga3 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$' and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restoharga3.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran $$$$
restoharga4 = []
for restoran in data:
    if restoran['restoran']['harga'] == '$$$$' and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restoharga4.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

#daftar restoran full
restosemua = []
for restoran in data[:5]:
    if restoran['restoran']['harga'] in ['$','$$','$$$','$$$$'] and restoran['restoran']['tipe'] in ['asia','barat','timur tengah']:
        restosemua.append([restoran['restoran']['nama'],restoran['restoran']['tipe'],restoran['restoran']['harga']])

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
    filterutama = False
    tanyajenis = input('Apakah anda ingin menggunakan filter jenis restoran?    y/n')
    if tanyajenis.lower()=='y':
        tanyajenis = False
        print('='*50)
        print('Selamat datang pada filter jenis restoran')
        print('='*50)
        print('Asia/Barat/Timur Tengah')
        jenisresto = input('Masukkan tipe jenis restoran.      Asia, Barat, Timur Tengah')
        if jenisresto.lower() in ['asia', 'barat', 'timur tengah']:
            jenisresto = False
            tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
            if tanyaharga.lower()=='y':
                tanyaharga = False
                print('='*50)
                print('Selamat datang pada filter harga restoran')
                print('='*50)
                print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)')
                hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
                if jenisresto == 'asia' and hargaresto == '$':
                    
                    print(tabulate(restoasia1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'asia' and hargaresto == '$$':
                    
                    print(tabulate(restoasia2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'asia' and hargaresto == '$$$':
                    
                    print(tabulate(restoasia3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'asia' and hargaresto == '$$$$':
                    
                    print(tabulate(restoasia4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat' and hargaresto == '$':
                   
                    print(tabulate(restobarat1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat' and hargaresto == '$$':
                    
                    print(tabulate(restobarat2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat' and hargaresto == '$$$':
                    
                    print(tabulate(restobarat3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat' and hargaresto == '$$$$':
                    
                    print(tabulate(restobarat4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah' and hargaresto == '$':
                    
                    print(tabulate(restotimur1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah' and hargaresto == '$$':
                    
                    print(tabulate(restotimur2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah' and hargaresto == '$$$':
                    
                    print(tabulate(restotimur3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah' and hargaresto == '$$$$':
                    
                    print(tabulate(restotimur4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                else :
                    print('Range Harga tidak tersedia')
                    hargaresto = True
            elif tanyaharga.lower()=='n':
                tanyaharga = False
                print('-'*50)
                print('Anda tidak memilih range harga restoran')
                print('-'*50)
                if jenisresto == 'asia':
                    print(tabulate(restoasia0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat':
                    print(tabulate(restobarat0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah':
                    print(tabulate(restotimur0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            else :
                tanyaharga = True
        else:
            print('Jenis Resto tidak tersedia')
            jenisresto = True
    elif tanyajenis.lower()== 'n':
        tanyajenis = False
        print('-'*50)
        print('Anda tidak memilih jenis restoran')
        print('-'*50)
        tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
        if tanyaharga.lower()=='y':
            print('Selamat datang pada filter harga restoran')
            hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
            print('-'*50)
            if hargaresto == '$':
                print(tabulate(restoharga1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif hargaresto == '$$':
                print(tabulate(restoharga2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif hargaresto == '$$$':
                print(tabulate(restoharga3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif hargaresto == '$$$$':
                print(tabulate(restoharga4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl")) 
        elif tanyaharga.lower()=='n':
            print('-'*50)
            print('Anda tidak memilih range harga restoran')
            print('-'*50)
            print(tabulate(restosemua,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    else:
        tanyajenis = True
elif filterutama.lower() == 'n':
    filterutama = False
    print('Anda tidak menggunakan filter')
    print(tabulate(restosemua,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
else :
    filterutama = True

#perulangan filter utama (filterutama)
while filterutama:
    filterutamaulang=input('Apakah anda ingin menggunakan Filter Restoran?    y/n')
    if filterutamaulang.lower()== 'y':
        filterutama = False
        tanyajenis = input('Apakah anda ingin menggunakan filter jenis restoran?    y/n')
        if tanyajenis.lower()=='y':
            tanyajenis = False
            print('='*50)
            print('Selamat datang pada filter jenis restoran')
            print('='*50)
            print('Asia/Barat/Timur Tengah')
            jenisresto = input('Masukkan tipe jenis restoran.      Asia, Barat, Timur Tengah')
            if jenisresto.lower() in ['asia', 'barat', 'timur tengah']:
                jenisresto = False
                tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
                if tanyaharga.lower()=='y':
                    tanyaharga = False
                    print('='*50)
                    print('Selamat datang pada filter harga restoran')
                    print('='*50)
                    print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)')
                    hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
                    if jenisresto == 'asia' and hargaresto == '$':
                        hargaresto=False
                        print(tabulate(restoasia1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'asia' and hargaresto == '$$':
                        hargaresto=False
                        print(tabulate(restoasia2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'asia' and hargaresto == '$$$':
                        hargaresto=False
                        print(tabulate(restoasia3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'asia' and hargaresto == '$$$$':
                        hargaresto=False
                        print(tabulate(restoasia4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'barat' and hargaresto == '$':
                        hargaresto=False
                        print(tabulate(restobarat1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'barat' and hargaresto == '$$':
                        hargaresto=False
                        print(tabulate(restobarat2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'barat' and hargaresto == '$$$':
                        hargaresto=False
                        print(tabulate(restobarat3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'barat' and hargaresto == '$$$$':
                        hargaresto=False
                        print(tabulate(restobarat4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'timur tengah' and hargaresto == '$':
                        hargaresto=False
                        print(tabulate(restotimur1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'timur tengah' and hargaresto == '$$':
                        hargaresto=False
                        print(tabulate(restotimur2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'timur tengah' and hargaresto == '$$$':
                        hargaresto=False
                        print(tabulate(restotimur3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'timur tengah' and hargaresto == '$$$$':
                        hargaresto=False
                        print(tabulate(restotimur4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    else :
                        print('Range Harga tidak tersedia')
                        hargaresto = True
                elif tanyaharga.lower()=='n':
                    tanyaharga = False
                    print('-'*50)
                    print('Anda tidak memilih range harga restoran')
                    print('-'*50)
                    if jenisresto == 'asia':
                        print(tabulate(restoasia0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'barat':
                        print(tabulate(restobarat0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                    elif jenisresto == 'timur tengah':
                        print(tabulate(restotimur0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                else :
                    tanyaharga = True
            else:
                print('Jenis Resto tidak tersedia')
                jenisresto = True
        elif tanyajenis.lower()== 'n':
            tanyajenis = False
            print('-'*50)
            print('Anda tidak memilih jenis restoran')
            print('-'*50)
            tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
            if tanyaharga.lower()=='y':
                print('Selamat datang pada filter harga restoran')
                hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
                print('-'*50)
                if hargaresto == '$':
                    print(tabulate(restoharga1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif hargaresto == '$$':
                    print(tabulate(restoharga2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif hargaresto == '$$$':
                    print(tabulate(restoharga3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif hargaresto == '$$$$':
                    print(tabulate(restoharga4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl")) 
            elif tanyaharga.lower()=='n':
                print('-'*50)
                print('Anda tidak memilih range harga restoran')
                print('-'*50)
                print(tabulate(restosemua,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        else:
            tanyajenis = True
    elif filterutamaulang.lower() == 'n':
        filterutama = False
        print('Anda tidak menggunakan filter')
        print(tabulate(restosemua,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    else :
        filterutama = True
    

#perulangan tanya filter jenis restoran (tanyajenis)
while tanyajenis:
    tanyajenisulang = input('Apakah anda ingin menggunakan filter jenis restoran?    y/n')
    if tanyajenisulang.lower()=='y':
        tanyajenis = False
        print('='*50)
        print('Selamat datang pada filter jenis restoran')
        print('='*50)
        print('Asia/Barat/Timur Tengah')
        jenisresto = input('Masukkan tipe jenis restoran.      Asia, Barat, Timur Tengah')
        if jenisresto.lower() in ['asia', 'barat', 'timur tengah']:
            jenisresto = False
            tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
            if tanyaharga.lower()=='y':
                tanyaharga = False
                print('='*50)
                print('Selamat datang pada filter harga restoran')
                print('='*50)
                print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)')
                hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
                if jenisresto == 'asia' and hargaresto == '$':
                    hargaresto=False
                    print(tabulate(restoasia1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'asia' and hargaresto == '$$':
                    hargaresto=False
                    print(tabulate(restoasia2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'asia' and hargaresto == '$$$':
                    hargaresto=False
                    print(tabulate(restoasia3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'asia' and hargaresto == '$$$$':
                    hargaresto=False
                    print(tabulate(restoasia4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat' and hargaresto == '$':
                    hargaresto=False
                    print(tabulate(restobarat1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat' and hargaresto == '$$':
                    hargaresto=False
                    print(tabulate(restobarat2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat' and hargaresto == '$$$':
                    hargaresto=False
                    print(tabulate(restobarat3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat' and hargaresto == '$$$$':
                    hargaresto=False
                    print(tabulate(restobarat4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah' and hargaresto == '$':
                    hargaresto=False
                    print(tabulate(restotimur1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah' and hargaresto == '$$':
                    hargaresto=False
                    print(tabulate(restotimur2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah' and hargaresto == '$$$':
                    hargaresto=False
                    print(tabulate(restotimur3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah' and hargaresto == '$$$$':
                    hargaresto=False
                    print(tabulate(restotimur4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                else :
                    print('Range Harga tidak tersedia')
                    hargaresto = True
            elif tanyaharga.lower()=='n':
                tanyaharga = False
                print('-'*50)
                print('Anda tidak memilih range harga restoran')
                print('-'*50)
                if jenisresto == 'asia':
                    print(tabulate(restoasia0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'barat':
                    print(tabulate(restobarat0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
                elif jenisresto == 'timur tengah':
                    print(tabulate(restotimur0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            else :
                tanyaharga = True
        else:
            print('Jenis Resto tidak tersedia')
            jenisresto = True
    elif tanyajenis.lower()== 'n':
        tanyajenis = False
        print('-'*50)
        print('Anda tidak memilih jenis restoran')
        print('-'*50)
        tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
        if tanyaharga.lower()=='y':
            print('Selamat datang pada filter harga restoran')
            hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
            print('-'*50)
            if hargaresto == '$':
                print(tabulate(restoharga1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif hargaresto == '$$':
                print(tabulate(restoharga2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif hargaresto == '$$$':
                print(tabulate(restoharga3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif hargaresto == '$$$$':
               print(tabulate(restoharga4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl")) 
        elif tanyaharga.lower()=='n':
            print('-'*50)
            print('Anda tidak memilih range harga restoran')
            print('-'*50)
            print(tabulate(restosemua,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    else:
        tanyajenis = True
        
#perulangan jenis restoran (jenisresto)
while jenisresto:
    jenisrestoulang = input('Masukkan tipe jenis restoran.      Asia, Barat, Timur Tengah')
    if jenisrestoulang.lower() in ['asia', 'barat', 'timur tengah']:
        jenisresto = False
        tanyaharga = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
        if tanyaharga.lower()=='y':
            tanyaharga = False
            print('='*50)
            print('Selamat datang pada filter harga restoran')
            print('='*50)
            print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)')
            hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
            if jenisresto == 'asia' and hargaresto == '$':
                hargaresto=False
                print(tabulate(restoasia1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'asia' and hargaresto == '$$':
                hargaresto=False
                print(tabulate(restoasia2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'asia' and hargaresto == '$$$':
                hargaresto=False
                print(tabulate(restoasia3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'asia' and hargaresto == '$$$$':
                hargaresto=False
                print(tabulate(restoasia4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'barat' and hargaresto == '$':
                hargaresto=False
                print(tabulate(restobarat1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'barat' and hargaresto == '$$':
                hargaresto=False
                print(tabulate(restobarat2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'barat' and hargaresto == '$$$':
                hargaresto=False
                print(tabulate(restobarat3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'barat' and hargaresto == '$$$$':
                hargaresto=False
                print(tabulate(restobarat4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'timur tengah' and hargaresto == '$':
                hargaresto=False
                print(tabulate(restotimur1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'timur tengah' and hargaresto == '$$':
                hargaresto=False
                print(tabulate(restotimur2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'timur tengah' and hargaresto == '$$$':
                hargaresto=False
                print(tabulate(restotimur3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'timur tengah' and hargaresto == '$$$$':
                hargaresto=False
                print(tabulate(restotimur4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            else :
                print('Range Harga tidak tersedia')
                hargaresto = True
        elif tanyaharga.lower()=='n':
            tanyaharga = False
            print('-'*50)
            print('Anda tidak memilih range harga restoran')
            print('-'*50)
            if jenisresto == 'asia':
                print(tabulate(restoasia0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'barat':
                print(tabulate(restobarat0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
            elif jenisresto == 'timur tengah':
                print(tabulate(restotimur0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        else :
            tanyaharga = True
    else:
        print('Jenis Resto tidak tersedia')
        jenisresto = True

#perulangan tanya filter harga (tanyaharga)
while tanyaharga:
    tanyahargaulang = input('Apakah anda ingin menggunakan filter harga restoran?     y/n')
    if tanyahargaulang.lower()=='y':
        tanyaharga = False
        print('='*50)
        print('Selamat datang pada filter harga restoran')
        print('='*50)
        print('$(1-25K)/$$(25k-50k)/$$$(35k-100k)/$$$$(70k and up)')
        hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
        if jenisresto == 'asia' and hargaresto == '$':
            hargaresto=False
            print(tabulate(restoasia1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'asia' and hargaresto == '$$':
            hargaresto=False
            print(tabulate(restoasia2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'asia' and hargaresto == '$$$':
            hargaresto=False
            print(tabulate(restoasia3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'asia' and hargaresto == '$$$$':
            hargaresto=False
            print(tabulate(restoasia4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'barat' and hargaresto == '$':
            hargaresto=False
            print(tabulate(restobarat1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'barat' and hargaresto == '$$':
            hargaresto=False
            print(tabulate(restobarat2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'barat' and hargaresto == '$$$':
            hargaresto=False
            print(tabulate(restobarat3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'barat' and hargaresto == '$$$$':
            hargaresto=False
            print(tabulate(restobarat4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'timur tengah' and hargaresto == '$':
            hargaresto=False
            print(tabulate(restotimur1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'timur tengah' and hargaresto == '$$':
            hargaresto=False
            print(tabulate(restotimur2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'timur tengah' and hargaresto == '$$$':
            hargaresto=False
            print(tabulate(restotimur3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'timur tengah' and hargaresto == '$$$$':
            hargaresto=False
            print(tabulate(restotimur4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        else :
            print('Range Harga tidak tersedia')
            hargaresto = True
    elif tanyahargaulang.lower()=='n':
        tanyaharga = False
        print('-'*50)
        print('Anda tidak memilih range harga restoran')
        print('-'*50)
        if jenisresto == 'asia':
            print(tabulate(restoasia0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'barat':
            print(tabulate(restobarat0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
        elif jenisresto == 'timur tengah':
            print(tabulate(restotimur0,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    else :
        tanyaharga = True

#perulangan filter harga resto (hargaresto)
while hargaresto:
    hargaresto = input('Masukkan range harga restoran.      $/$$/$$$/$$$$')
    if jenisresto == 'asia' and hargaresto == '$':
        hargaresto=False
        print(tabulate(restoasia1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'asia' and hargaresto == '$$':
        hargaresto=False
        print(tabulate(restoasia2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'asia' and hargaresto == '$$$':
        hargaresto=False
        print(tabulate(restoasia3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'asia' and hargaresto == '$$$$':
        hargaresto=False
        print(tabulate(restoasia4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'barat' and hargaresto == '$':
        hargaresto=False
        print(tabulate(restobarat1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'barat' and hargaresto == '$$':
        hargaresto=False
        print(tabulate(restobarat2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'barat' and hargaresto == '$$$':
        hargaresto=False
        print(tabulate(restobarat3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'barat' and hargaresto == '$$$$':
        hargaresto=False
        print(tabulate(restobarat4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'timur tengah' and hargaresto == '$':
        hargaresto=False
        print(tabulate(restotimur1,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'timur tengah' and hargaresto == '$$':
        hargaresto=False
        print(tabulate(restotimur2,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'timur tengah' and hargaresto == '$$$':
        hargaresto=False
        print(tabulate(restotimur3,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    elif jenisresto == 'timur tengah' and hargaresto == '$$$$':
        hargaresto=False
        print(tabulate(restotimur4,headers=['Nama Restoran', 'Jenis Restoran', ' Range Harga'], tablefmt="orgtbl"))
    else :
        print('Range Harga tidak tersedia')
        hargaresto = True


#perulangan nyari resto
search = input("Ingin menelusuri Restoran? y/n ")
if search.lower()== 'y':
    print('Selamat datang ke menu pencarian')
    search = True
else:
    print('-'*50)
    print('Terima kasih telah menggunakan program kami')
    search = False

#input resto
while search:
    find = input("Masukkan nama Restoran: ")
    if find.lower() in resto_lower:
        index = resto_lower.index(find.lower())
        print(tabulate([namaresto[index]], headers=['Restoran','Deskripsi','Recommended Menu','Alamat','Peak Hour','Operasional Hour','Harga'], tablefmt="orgtbl"))
    else:
        print("Resto tidak tersedia")
    print("-"*30+"\n")
    
    #input lagi ga
    search = input("Ingin menelusuri restoran lagi? y/n ")
    if search.lower() == 'y':
        search = True
    else:
        search = False