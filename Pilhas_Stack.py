# Pilhas (Stack) com lista nativa

'''
pilha_lista = []

# Inserindo elementos (Push) com append(insere no fim)
pilha_lista.append("Prato 1")
pilha_lista.append("Prato 2")
pilha_lista.append("Prato 3")
print("Pilha atual:",pilha_lista)

# Removendo elementos (Pop) - Remove o último a entrar
topo = pilha_lista.pop()
print("Removido:",topo)   # Topo da pilha
print("Pilha após POP:",pilha_lista)

# DESVANTAGEM - Permite utiliar funções que não são de pilha
pilha_lista.insert(1,"Prato 7")
print(pilha_lista)
'''

# Pilha (Stack) como Classe (Objeto)
class Pilha:
    def __init__(self):
        self.itens = []
    
    def is_empty(self):     # Verifica se está vazia
        return len(self.itens) == 0
    
    def push(self,item):    # Adiciona no topo
        self.itens.append(item)
      
    def pop(self):          # Remove e retorna o topo
        if not self.is_empty(): # Chama função da classe is_empty
          return self.itens.pop()
        raise IndexError("A pilha está vazia!")
    
    def peek(self):         # Retorna o topo sem remover
      if not self.is_empty():
        return self.itens[-1]
      return None


pilha_classe = Pilha()
print(pilha_classe.is_empty())
pilha_classe.push("6_Espadas")
pilha_classe.push("A_Ouros")
pilha_classe.push("Q_Copas")

print("Pilha cartas:",pilha_classe.itens)
print("Carta do topo (peek):",pilha_classe.peek())
print("Removido do topo (pop)",pilha_classe.pop())
print("Pilha cartas nova:",pilha_classe.itens)
