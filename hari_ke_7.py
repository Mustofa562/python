import numpy as np
import pandas as pd

# Data acak
stok = np.random.randint(10, 100, (5, 3))
harga_produk = np.array([[6000000, 2000000, 4000000]])
data = {
    'produk': ['laptop','hp','tablet'],
    'harga': harga_produk.flatten(),
    'stok': stok.mean(axis=0)
}

df = pd.DataFrame(data)
print(df)

#Tambahkan kolom "Total Nilai"
df['total nilai'] = df['harga'] * df['stok']
print(df)

#Hitung
print('total stok tiap produk',stok.sum(axis=0))
print('rata-rata stok tiap produk',stok.mean(axis=0))
print('produk dengan stok lebih tinggi',df['stok'].max())


