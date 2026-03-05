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
