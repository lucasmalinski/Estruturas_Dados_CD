# Filas com prioridade
import heapq # Transforma listas comuns em filas de prioridade

class FilaPrioridade:
    def __init__(self):
        self.heap = []
        # Usado para desempate quando as prioridades são iguais
        self.indice = 0  

    def enqueue(self, item, prioridade):
        # Tupla Salva (prioridade,ordem de chegada, item)
        # Quanto menor o valor maior a prioridade
        heapq.heappush(self.heap,(prioridade,self.indice,item))
        self.indice += 1

    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)[-1]
        raise IndexError("Fila de prioridade vazia")
    
# Instanciar objeto fila com prioridade
pronto_socorro = FilaPrioridade()
# Prioridade 1 é a mais alta
pronto_socorro.enqueue("Paciente com dor de cabeça", 3)
pronto_socorro.enqueue("Paciente com parada cardíaca", 1)
pronto_socorro.enqueue("Paciente com pé quebrado", 2)
pronto_socorro.enqueue("Paciente idoso com febre",2)

# Prioridade 1
print("Atendimento 1:",pronto_socorro.dequeue())

# Chegou depois de todos
pronto_socorro.enqueue("Paciente com sinais de AVC",1)

# Prioridade 1 chegou depois de todos
print("Atendimento 2:",pronto_socorro.dequeue())

# Prioridade 2, primeiro a chegar
print("Atendimento 3:",pronto_socorro.dequeue())

# Prioridade 2, segundo a chegar
print("Atendimento 4:",pronto_socorro.dequeue())

# Prioridade 3
print("Atendimento 5:",pronto_socorro.dequeue())
