import numpy as np
import pandas as pd

data = np.array([[10, 15, 20],
                 [25, 30, 35],
                 [40, 45, 50]])

#ubah ke dataframe pandas
df = pd.DataFrame(data, columns=['laptop','Hp','Tablet'])
df.loc[3] = [55,60,65]
print(df)

# total dan rata-rata tiap kolom
print("Total penjualan tiap produk:\n", df.sum())
print("Rata-rata penjualan tiap produk:\n", df.mean())

# total semua per baris
df['Total semua'] = df.sum(axis=1)
print(df)

#baris yang memiliki nilai lebih dari 30 di kolom 'Produk B'
print(df[df['Hp'] > 30])

#nilai yg lebih besar dari rata rata
print(df[df>df.values.mean()])

# Buat array harga
harga = np.array([15000, 20000, 25000])
# Hitung total pendapatan per kolom (produk)
total = df.sum().values * harga

hasil = pd.DataFrame({
    'Produk': ['A', 'B', 'C'],
    'Harga': harga,
    'Total Penjualan': df.sum().values,
    'Total Pendapatan': total
})
print(hasil)
hasil['kategori'] = np.where(hasil['Harga']>20000, 'premium', 'standar')