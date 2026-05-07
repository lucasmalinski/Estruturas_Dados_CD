
# =======================================
#  PILHAS
# =======================================

pilha = []


pilha.append("Entrada 1")
pilha.append("Entrada 2")
pilha.append("Entrada 3")
print("Pilha:\n", pilha)

pilha.pop()
print("Pilha:\n", pilha)


class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self): 
        if not self.is_empty():
            return self.itens.pop()
        raise IndexError("Pilha vazia")

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        return None

carros = Pilha()
print(carros.is_empty())
carros.push("Polo")
carros.push("Bora")
carros.push("Ecosport")
print(carros.peek())

carros.pop()
print(carros.peek())