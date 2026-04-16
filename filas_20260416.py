# fila_lista = []

# fila_lista.append("Paciente 2")
# fila_lista.append("Paciente 1")
# fila_lista.append("Paciente 3")
# 
# atendido = fila_lista.pop(0) # Remove e retorna o primeiro da lista
# 
# print("Atendido:", atendido)
# 
# print("Fila Restante:", fila_lista)
# 
# # Quebra a regra da fila (Fura a fila)
# fila_lista.insert(0, "Paciente 4")
# 
# print("Fila Restante:", fila_lista)
# 
# # Quebra a regra da fila (Remove sem atender)
# fila_lista.remove("Paciente 3")
# print("Fila Restante:", fila_lista)
# 
# atendido2 = fila_lista.pop()
# # Quebra a regra da fila
# print(atendido2)
# 


from collections import deque
#Filas (Quere) com CLasse(objeto) sem prioridade

class Fila:
    def __init__(self):
        self.itens = deque()

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.itens.popleft() #Remove do início da fila
        raise IndexError("A fila está vazia!")

    def __str__(self):
        return str(list(self.itens))

# Objeto Fila
fila_classe = Fila()

# print(fila_classe.is_empty())

fila_classe.enqueue("Ana")
fila_classe.enqueue("Bernardo")
fila_classe.enqueue("Carlos")

print("Fila:", fila_classe)