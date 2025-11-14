import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#perintah untuk user 
data ={}

jumlah_stok = int(input('berapa produk yang anda ingin masukan? = '))

produk = []
harga = []
terjual = []
stok = []

#sistem untuk masukan data 
for i in range(jumlah_stok):
    nama_barang = input(f'masukan nama barang anda (pisahkan dengan koma) = ')
    stok_barang = input(f'masukan stok barang anda yang ke-{i+1} = ')
    harga_barang = int(input(f'masukan harga barang anda yang ke-{i+1}= '))
    produk_terjual = int(input(f'masukan jumlah produk yg terjual yang ke-{i+1}= '))

    produk.append(nama_barang)
    harga.append(harga_barang)
    terjual.append(produk_terjual)
    stok.append(stok_barang)

#simpan ke data dict
data['produk'] = produk
data['harga'] = harga
data['terjual'] = terjual 
data['stok'] = stok

#hasil dataset
df = pd.DataFrame(data)

#pendapatan
df['pendapatan'] = df[harga] * df['terjual']

#rata-rata produk terjual
print('rata-rata produk terjual adalah = ', df[df['produk']==df['terjual'].mean()])

