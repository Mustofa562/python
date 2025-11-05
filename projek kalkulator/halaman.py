import numpy as np
import fungsi
import matplotlib.pyplot as plt

import os
os.system("cls")

while True:

    print("=="*12,"KALKULATOR MATRIX","=="*12)
    print("Silahkan pilih Operasi Matrix")
    print("1. Penjumlahan Matrix")
    print("2. Perkalian Matrix")
    print("3. Transpose Matrix")
    print("4. Determinan Matrix")

    #pilihan operasi
    operasi = input("Pilih Operasi matrix anda dengan angka = ")


    #matrix pertama
    rows = int(input("Masukan jumlah baris untuk matrix pertama: "))
    cols = int(input("Masukan jumlah kolom untuk matrix pertama: "))

    #menjadi matrix
    data = list(map(int,input(f"Masukan {rows*cols} angka agar membentuk matrix yang anda inginkan, angka harus di spasi: ").split()))

    #dijadikan numpy
    matrix = np.array(data).reshape(rows, cols)
    
    print(f"ini matrix pertama anda = {matrix}")


    #matrix Kedua
    rows1 = int(input("Masukan jumlah baris untuk matrix Kedua: "))
    cols2 = int(input("Masukan jumlah kolom untuk matrix kedua: "))

    #menjadi matrix
    data1 = list(map(int,input(f"Masukan {rows1*cols2} angka agar membentuk matrix yang anda inginkan, angka harus di spasi: ").split()))

    #dijadikan numpy
    matrix1 = np.array(data1).reshape(rows1, cols2)
    
    print(f"ini matrix kedua anda = {matrix1}")
    

    #operasi matrix
    if operasi == "1":
        hasil = fungsi.penjumlahan(matrix,matrix1)
        print(f"hasil dari penjumlahan matrix adaalah = {hasil}")

        # visual
        plt.imshow(hasil, cmap="viridis", interpolation="nearest")
        plt.colorbar(label="Nilai")
        plt.title("Hasil Penjumlahan Matrix")
        

        #angka di setiap kotak
        rows,cols = hasil.shape
        for i in range(rows):
            for j in range(cols):
                plt.text(j,i, str(hasil[i,j]), ha="center",va="center", color="white", fontsize=12,fontweight="bold")

        plt.show()
        
    if operasi == "2":
        hasil = np.dot(matrix,matrix1)
        print(f"hasil perkalian matrix anda adalah = {hasil}")

        #visual
        plt.imshow(hasil, cmap="plasma", interpolation="nearest")
        plt.colorbar(label="Nilai")
        plt.title("Hasil Perkalian Matrix")
        
        #angka di setiap kotak
        rows,cols = hasil.shape
        for i in range(rows):
            for j in range(cols):
                plt.text(j,i, str(hasil[i,j]), ha="center",va="center", color="white", fontsize=12,fontweight="bold")

        plt.show()
    
    if operasi =="3":
        hasil = matrix.T
        hasil2 = matrix1.T
        print(f"ini adalah hasil dari transpose matrix pertama anda = {hasil}")
        print(f"ini adalah hasil dari transpose matrix kedua anda = {hasil2}")

        # tampilkan kedua transpose
        fig, axs = plt.subplots(1, 2, figsize=(8, 4))

        # matrix pertama
        axs[0].imshow(hasil, cmap="cividis", interpolation="nearest")
        axs[0].set_title("Transpose Matrix Pertama")
        rows, cols = hasil.shape
        for i in range(rows):
            for j in range(cols):
                axs[0].text(j, i, str(hasil[i, j]),
                    ha="center", va="center", color="white", fontsize=12, fontweight="bold")

        # matrix kedua
        axs[1].imshow(hasil2, cmap="cividis", interpolation="nearest")
        axs[1].set_title("Transpose Matrix Kedua")
        rows2, cols2 = hasil2.shape
        for i in range(rows2):
            for j in range(cols2):
                axs[1].text(j, i, str(hasil2[i, j]),
                    ha="center", va="center", color="white", fontsize=12, fontweight="bold")

        plt.show()

    if operasi == "4":
        hasil = np.linalg.det(matrix)
        hasil1 = np.linalg.det(matrix1)
        print(f"hasil dari operasi determinan matrix pertama = {hasil}")
        print(f"hasil dari operasi determinan matrix kedua = {hasil1}")

        # visualisasikan matriks aslinya (bukan det, karena determinan = angka tunggal)
        fig, axs = plt.subplots(1, 2, figsize=(8, 4))
        axs[0].imshow(matrix, cmap="coolwarm", interpolation="nearest")
        axs[0].set_title(f"Matrix Pertama\nDet = {round(hasil, 2)}")
        axs[1].imshow(matrix1, cmap="coolwarm", interpolation="nearest")
        axs[1].set_title(f"Matrix Kedua\nDet = {round(hasil1, 2)}")
        plt.show()