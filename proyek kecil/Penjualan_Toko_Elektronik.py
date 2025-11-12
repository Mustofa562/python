import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#perintah untuk user 
data ={}

jumlah_stok = int(input('berapa produk yang anda ingin masukan? = '))

produk = []
harga = []
terjual = []

for i in range(jumlah_stok):
    nama_barang = input(f'masukan nama barang anda ke-{i+1} = ')
    harga_barang = int(input(f'masukan harga barang anda ke-{i+1}= '))
    produk_terjual = int(input(f'masukan jumlah produk yg terjual ke-{i+1}= '))

    produk.append(nama_barang)
    harga.append(harga_barang)
    terjual.append(produk_terjual)

#simpan ke data dict
data['produk'] = produk
data['harga'] = harga
data['terjual'] = terjual 

#hasil dataset
df = pd.DataFrame(data)
print(df)
