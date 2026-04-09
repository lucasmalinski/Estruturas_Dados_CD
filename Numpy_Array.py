# Array com Numpy (ndarray)
# Utiliza arrays em cima da linguagem C que são
# muito mais efiientes do que listas

import numpy as np
'''
# 1. Criação de Array
vetor = np.array([10,20,30,40,50])
print(vetor)    # Similar à lista comum

matriz = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(matriz)   # Similar à matriz comum

zeros_1d = np.zeros(5)     # array com 5 zeros
print(zeros_1d)

zeros_2d = np.zeros((3,3)) # matriz com dimensões 3x3(x,y)
print(zeros_2d)

# Intervalo
sequencia = np.arange(11,22,2) # (inicio, fim_exclusivo, passo)
print(sequencia)

# Valores espaçados
espacados = np.linspace(0,1,5) # (inicio, fim, quantidade de elementos)
print(espacados)
'''

'''
# 2. Slicing (fatiamento) de Array 2D
dados = np.array([
  [10,20,30,40],
  [50,60,70,80],
  [90,100,110,120]
 ])

elemento = dados[1,2]   # Linha 1, coluna 2. Diferente de [1][2]
print(elemento)

todas_linhas_coluna_dois = dados[:,2]  # [linhas inicio:fim, colunas inicio:fim]
print(todas_linhas_coluna_dois)

primeira_linha_todas_colunas = dados[0,:] # Linha 0 com todas as colunas
print(primeira_linha_todas_colunas)

sub_matriz = dados[0:2,1:3]  # linhas 0 e 1, colunas 1 e 2l matriz quadrada
print(sub_matriz)
'''

'''
# 3. Operações Vetorizadas - Não utilizam FOR e são mais rápidas

precos = np.array([100.0, 200.50, 299.99])
quantidades = np.array([2,5,3])

faturamento = precos * quantidades      # Faz a operação * pelos pares de índices (o com 0, 1 com 1, 2 com 2)
print(faturamento)

precos_com_descontos = precos - 20.50   # Faz a operação de subtração em todos os elementos
print(precos_com_descontos)

raiz_quadrada = np.sqrt(precos)         # Função que calcula a raiz de todos
print(raiz_quadrada)

soma_total = np.sum(precos)             # Função que faz a soma de todos
print(soma_total)

media_precos = np.mean(precos)          # Função que calcula a média
print(media_precos)

mediana_precos = np.median(precos)      # Função que calcula a mediana
print(mediana_precos)

potencia_precos = np.pow(precos,2)      # Fução que calcula potência (array, potencia)
print(potencia_precos)

quartil_precos = np.quantile(precos,0.5)# Função que calcula os quartis = 0-1 (%)
print(quartil_precos)

desvio_padrao_precos = np.std(precos)   # Função de desvio padrão
print(desvio_padrao_precos)
'''

# Indexação Booleana (Filtros Vetorizados)
idades = np.array([18,25,32,45,19,50])

# Condição Lógica, gera array de booleans
filtro_maiores_30 = idades > 30 
print(filtro_maiores_30)

# Aplicando o filtro na array original
filtrados = idades[filtro_maiores_30]
print(filtrados)

#Forma resumida 
# & = and  , | = or
idades_validas = idades[(idades >= 18) & (idades < 40)]
print(idades_validas)
