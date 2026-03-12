# Estruturas de dados lineares
# Listas []
'''
vazio = []
vazio_2 = list()

numeros = [5,3,8,9,6]
nomes = ["Kleber", "Manuela", 'Nicolas']
mista = ["Kleber", 26, "01234567890", 1.85, 142, True]

letras = list("Paralelepípedo")
print(letras[2])
print(letras[-5])
print(letras[4:8]) 
# Intervalo, numero da esquerda inclusivo
# numero da direita exclusivo
invertida = letras[::-1]
print(invertida)
'''

'''
# Modificando elementos
notas = [8.2, 2.3, 5.6, 7.9, 4.8]
notas[1] = 4
notas[3:5] = [8, 5]

print(notas)
'''

'''
# Adicinar elementos
carros =["Fusca", "Santana", "Opala"]
print(carros)
carros.append("Maverick")   # Adiciona no final
print(carros)
carros.insert(2,"Passat")   # Adicina na posição do índice
print(carros)
carros.extend(["Escort", "Chevette"]) # Adiciona uma nova lista no fim
print(carros)
'''

'''
# Remover elementos
tarefas = [
    "Comprar",
    "Reabastecer",
    "Limpar",
    "Ler",
    "Comprar",
    "Responder"
    ]
print(tarefas)

tarefas.remove("Reabastecer")   # Remove a primeira ocorrencia
print(tarefas)

ultima_tarefa = tarefas.pop()   # Remove o último e pega o retorno
print(ultima_tarefa)
print(tarefas)

del tarefas[1]                  # Deleta no índice indicado
print(tarefas)

t = "Comprar"
while t in tarefas:             # Remove todas as ocorrências
    tarefas.remove(t)

print(tarefas)

tarefas.clear()
print(tarefas)
'''

'''
# Ordenação
armas = ["Machado", "Espada Larga", "Nunchaku", "Katana", "Alabarda"]
print(armas)

armas.sort()                # Ordenar em ordem alfabética
print(armas)

armas.reverse()             # Inverte a ordem da lista
print(armas)

armas.sort(reverse=True)    # Ordena de forma invertida
print(armas)

numeros = [56, 24,1000, 78, 0, -2]
print(numeros)
numeros.sort()
#numeros.sort(reverse = True)

print(numeros)
numeros.reverse()
print(numeros)
'''

'''
# Busca e contagem
cores = ["Vermelho", "Azul", "Verde", "Azul", "Amarelo", "Verde"]

tem_amarelo = "Amarelo" in cores    # Boolean, Verifica se existe na lista
tem_roxo = "Roxo" in cores
print(tem_amarelo)
print(tem_roxo)

# Quantos elementos daquele existem na lista
print(cores.count("Azul"))
print(cores.count("Roxo"))

# Encontrar índice
print(cores.index("Verde"))

# Laço de repetição para printar
for c in cores:
    print("Cor:",c)
'''

'''
# Listas como Pilhas(Stack) - LIFO (Last In, First Out)
historico = []

# Inserindo na pilha
historico.append("google.com")
historico.append("tiktok.com")
historico.append("github.com")

# Pegando o ultimo elemento da pilha(stack)
ultima_pagina = historico.pop() 
print(ultima_pagina)
'''

'''
# Matriz 2D
jogo_da_velha = [
    ["X","O", "X"],
    [" ","X", "O"],
    ["O"," ", "X"]
]
print(jogo_da_velha[1][1])
jogo_da_velha[2][1] = "X"
jogo_da_velha[2][2] = " "

for l in jogo_da_velha:
    print(l)
'''

# Cópia de listas
nums = [1,2,3]
# Copia o endereço de memória, não copia a lista (são dependentes)
nums_2 = nums
# Cria uma cópia independente da original
nums_3 = nums.copy()

nums[2] = 4

print(nums)
print(nums_2)
print(nums_3)
