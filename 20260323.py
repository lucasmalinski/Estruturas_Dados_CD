import numpy as np
import matplotlib.pyplot as plt
div = "------------------------------------"
block ="\n#########################################################################\n" 


print(block + "\n")
mylist = [10,20,30,40,50]

vetor = np.array(mylist)

print(f"Vetor:\n{vetor}\n\n") 

matriz = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(f"Matriz: \n{matriz}\n\n")

zeros_1d = np.zeros(5)

# arg as tupla
zeros_2d = np.zeros((3,3))

print(f"zeros_1d:\n{zeros_1d}\n\nzeros_2d: \n{zeros_2d}\n\n")

# Sequenciar com numpy (start, stop(fim exclusivo), step)
# arange = array range

sequencia = np.arange(11,22,2)

print( f"Sequência com inicio, fim, step: \n{sequencia} \n")

# Valores equidistantes em um intervalo
# =======================================
#  (inicio, fim, intervalo,
#   endpoint=True (Padrão) 
#  
# =======================================
espacados = np.linspace(0,100,5)  # Exemplo com quartis para clareza
print(f"Espçados incluindo endpoint: \n{espacados}\n\n")

espacados_sem_endpoint = np.linspace(0,100,5, endpoint=False)  # Exemplo com endpoint=False
print(f"Espaçados sem incluir endpoint\n{espacados_sem_endpoint}")


N = 5 # Constante com número de pontos

y = np.zeros(N) 

# =======================================
# Visualização Gráfica
# =======================================
# plt.plot(espacados, y, 'o')
# plt.plot(espacados_sem_endpoint, y + 0.5, 'o')
# plt.ylim([-0.5, 1])
# plt.show()

# =======================================
# Slicing - Fatiando Arrays
# =======================================


vetor_dados = [
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]
]
dados = np.array(vetor_dados)

elemento = dados[1,2] 

# [1,2] é 0 INDEXED!!!!

print(f"\nElemento:\n{div} {elemento}")

# Acessando 3ª coluna (1 indexed) - 2ª coluna (0 indexed)
todas_linhas_coluna2 = dados[0:3,2] #Ou [:,2]
print(f"\nElementos da coluna 2:\n{todas_linhas_coluna2}\n\n")

# =======================================
# SUBMATRIZ
# =======================================

sub_matriz = dados[0:2,1:3]
print(f"Submatriz:\n{sub_matriz}\n")

# =======================================
# Operações Vetorizadas
# =======================================

nome_produto = ["resma a4","resma envelope","acetato"]
precos = np.array([100.0, 200.50, 299.99])
qtds = np.array([2,5,3])

faturamento_cliente_fabio = precos * qtds 


print(f"Faturamento Fábio:\n{nome_produto}\n{faturamento_cliente_fabio}\n")

# =======================================
# subtração em cada elemento do vetor
# =======================================
precos_com_desconto = precos - 20.50
print(f"Preços com desconto:\n{precos_com_desconto}\n\n")

# =======================================
# Raiz Quadrada
# =======================================
raiz_quadrada = np.sqrt(precos)
print(f"Raiz quadrada: \n{np.round(raiz_quadrada, 2)}\n\n")

# =======================================
# Potência
# =======================================
power = np.pow(precos,2)
print(f"Potência: \n{np.round(power, 2)}\n\n")

# =======================================
# Agregações - Soma, Média e Mediana
# =======================================
soma_total = np.sum(precos)
print(f"Soma de cada preço:\n{div} {soma_total}\n\n")

media = np.mean(precos)
print(f"Média de preços: \n{div} {round(media)}\n\n")

mediana = np.median(precos)
print(f"Mediana de preços: \n{div} {mediana}\n\n")

print(block + "\n")