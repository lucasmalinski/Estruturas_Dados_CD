# Lista Duplamente Ligada

# Classe do Node com ponteiro duplo
class NodeDuplo:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None     # Ponteiro
        self.anterior = None    # Ponteiro

class ListaDuplamenteLigada:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,dado):
        novo_node = NodeDuplo(dado)

        # Se a lista estiver vazia, o novo
        # node é o início e o fim
        if self.head is None:
            self.head = novo_node
            self.tail = novo_node
            return
        
        # Se não estiver vazia, adiciona no final(tail)

        # O antigo último aponta para o novo
        self.tail.proximo = novo_node

        # O novo aponta para o antigo último
        novo_node.anterior = self.tail

        # Atualizamos quem é o último(tail)
        self.tail = novo_node

    def display_frente(self):
        # Percorre do início ao fim
        elementos = []
        atual = self.head
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print("None <-" + " <-> ".join(elementos)+" -> None")

    def display_tras(self):
        # Percorre do fim ao início (contrário)
        elementos = []
        atual = self.tail
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.anterior
        print("De trás pra frente: None -> "+" -> ".join(elementos))

lista_dupla_ligada = ListaDuplamenteLigada()
lista_dupla_ligada.append("Paciente A")
lista_dupla_ligada.append("Paciente B")
lista_dupla_ligada.append("Paciente C")
lista_dupla_ligada.append("Paciente D")

print("Lista Duplamente Ligada - Fila do SUS\n")
lista_dupla_ligada.display_frente()
print("\n")
lista_dupla_ligada.display_tras()
