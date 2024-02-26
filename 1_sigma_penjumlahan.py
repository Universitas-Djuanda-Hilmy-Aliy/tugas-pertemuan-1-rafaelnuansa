# Inisialisasi variabel untuk menyimpan hasil perjumlahan
result = 0

# Menggunakan loop for untuk menjumlahkan hasil ekspresi 2^(2i+1) dari i=1 hingga i=100
for i in range(1, 101):
    result += 2**(2*i+1)

# Cetak hasil perjumlahan
print("Hasil sigma perjumlahan:", result)
