# Lista Simplesmente Ligada (conhece apenas uma direção, próximo)

# Classe que representa cada elemento(Node) da lista
class NodeSimples:
    def __init__(self,dado):
        self.dado = dado
        # Inicialmente não aponta para ninguém (nulo)
        self.proximo = None

# Classe da lista simplesmente ligada (um lado)
class ListaSimplesmenteLigada:
    def __init__(self):
        self.head = None # Início da lista

    def is_empty(self):
        return self.head is None
        
    def append(self,dado):
        # Adiciona elemento no final da lista
        novo_node = NodeSimples(dado)

        if self.is_empty():
            self.head = novo_node
            return
        
        #Percorre a lista até achar o último node
        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo_node

    def display(self):
        #Printar a lista de forma visual
        elementos = []
        atual = self.head
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(elementos)+"-> None")


lista_s_ligada = ListaSimplesmenteLigada()
lista_s_ligada.append("Locomotiva")
lista_s_ligada.append("Vagão A")
lista_s_ligada.append("Vagão B")
lista_s_ligada.append("Vagão C")

print("Lista Simplesmente Ligada")
lista_s_ligada.display()
