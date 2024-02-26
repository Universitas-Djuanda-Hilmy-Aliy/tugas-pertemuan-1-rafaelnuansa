import numpy as np

# Def matriks pertama
matrix1 = np.array([[2, 3],
                    [1, 5]])

# Defmatriks kedua
matrix2 = np.array([[7, 0.5],
                    [4, 0]])

# perkalian matriks menggunakan np.dot() atau operator @
result = np.dot(matrix1, matrix2)

# hasil perkalian matriks
print("Hasil perkalian matriks:")
print(result)
