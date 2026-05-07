# Array 2D (Matriz) com lista nativa 
# Lista de Listas
# matriz_nativa = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# elemento = matriz_nativa[1][2]
# print(f"Elemento da linha 2, coluna 3: {matriz_nativa[1][2]}")

# # Multiplicando cada elemento por 2
# for linha in range(len(matriz_nativa)):
#     for coluna in range(len(matriz_nativa[linha])):
#         matriz_nativa[linha][coluna] *=2

# for linha in matriz_nativa:
#     print(linha)
############################################################


# Array 2D do Numpy
# import numpy as np

# matriz_numpy = np.array([
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]) 

# # Shape (formato linhas x colunas)
# print(f"Formato da matriz: {matriz_numpy.shape}")

# # Vetorização
# matriz_dobrada = matriz_numpy * 2
# print(f"Matriz com valores dobrados:\n {matriz_dobrada}")

# # Filtragem
# valores_altos = matriz_dobrada[matriz_dobrada > 100]
# print(f"Apenas valores acima de 100: {valores_altos}")

# # Estatística
# # Mean, media axis=0(coluna) axis=1(linha) 
# media_coluna = np.mean(matriz_numpy, axis = 0)
# media_linha = np.mean(matriz_numpy, axis = 1)
# print(f"Media por coluna:{media_coluna}\nMedia por linha:{media_linha}")

import numpy as np
import matplotlib.pyplot as plt

scratchpad_blk = np.array([
    [0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0],
    [0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0],
    [0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0],
    [0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0],
    [0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255],
    [255, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 255],
    [0, 255, 255, 255, 0, 0, 155, 0, 0, 155, 0, 0, 255, 255, 255, 0],
    [0, 0, 255, 0, 0, 0, 155, 0, 0, 155, 0, 0, 0, 255, 0, 0],
    [0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0],
    [0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0],
    [0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0],
])

scratchpad_wht = 255 - scratchpad_blk


plt.imshow(scratchpad_wht, cmap='gray')
plt.axis('off')
plt.savefig("output_wht.png")




