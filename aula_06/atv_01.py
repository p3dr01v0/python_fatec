class Node:
    def __init__(self, newItem, nextNode=None):
        # Um nó contém um item e uma referência para o próximo nó
        self.item = newItem
        self.next = nextNode


class CircularLinkedList:
    def __init__(self):
        # inicialmente a lista esta vazia, portanto 'final' é None
        self.final = None
        self.count = 0
        self.removidos = []

    def isEmpty(self):
        # verifica se a lista esta vazia
        return self.final is None

    def AddFirst(self, newItem):
        # cria um novo nó para conter o item
        newNode = Node(newItem)

        if not self.isEmpty():
            # Se a lista não esta vazia, o novo nó aponta para o nó que era o primeiro
            newNode.next = self.final.next
            # O final da lista agora aponta para o novo primeiro nó
            self.final.next = newNode
        else:
            # se a lista esta vazia o nono no aponta para ele mesmo
            newNode.next = newNode
            # o novo nó e o primeiro e último (final)
            self.final = newNode

        # incrementa a quantidade de elementos
        self.count += 1

    def AddLast(self, newItem):
        # adiciona um item ao final da lista
        self.AddFirst(newItem)
        # Atualiza o 'final' para o novo nó adicionado
        self.final = self.final.next

    def RemoveFirst(self):
        # remove o primeiro item da lista
        if self.isEmpty():
            raise Exception("Lista vazia")

        item_removido = self.final.next.item
        self.removidos.append(item_removido)

        if self.count == 1:
            # Se há apenas um nó, remover faz com que a lista fique vazia
            self.removidos.append(self.final)
            self.final = None
        else:
            # o segundo nó se torna o novo primeiro nó
            self.final.next = self.final.next.next

        # diminui a quantidade de elementos
        self.count -= 1

    def RemoveLast(self):
        # remove o ultimo item da lista
        if self.isEmpty():
            raise Exception("Lista Vazia")

        # Se há apenas um nó, remover faz com que a lista fique vazia
        if self.count == 1:
            # Armazena o item que será removido
            item_removido = self.final.item
            self.removidos.append(item_removido)

            self.final = None
        else:
            # percorre até o penúltimo nó
            aux = self.final.next
            while aux.next != self.final:
                aux = aux.next
            # Armazena o item que será removido
            item_removido = self.final.item
            self.removidos.append(item_removido)

            # o penúltimo nó se torna o novo último
            aux.next = aux.next.next
            self.final = aux

        # diminui a quantidade de elementos
        self.count -= 1

    def Remove(self, item):
        # remove um no que contem o item especificado
        if self.isEmpty():
            raise Exception("Lista Vazia")
        else:
            self.removidos.append(item)

        aux = self.final.next  # começa do primeiro nó
        anterior = self.final  # começa a busca do último nó

        # busca o nó que contém o item
        while aux != self.final and aux.item != item:
            anterior = aux
            aux = aux.next

        # verifica se o item foi encontrado
        if aux.item != item:
            return False

        if aux == aux.next:
            # Caso a lista tenha apenas um nó
            self.final = None
        else:
            # Remove o nó do encadeamento
            anterior.next = aux.next
            if aux == self.final:
                # atualiza o final da lista se o item removido era o ultimo
                self.final = anterior

        # remove um elemento do contador
        self.count -= 1
        return True

    def desfazer_remove_inicio(self):

        if not self.removidos:
            print("Nenhum item na lista de removidos")
        else:
            self.AddFirst(self.removidos.pop())
            print("Remoção desfeita")

    def desfazer_remove_fim(self):

        if not self.removidos:
            print("Nenhum item na lista de removidos")
        else:
            self.AddLast(self.removidos.pop())
            print("Remoção desfeita")

    def PrintList(self):
        # exibe todos os itens da lista circular
        if self.isEmpty():
            print("Lista vazia")
            return

        aux = self.final.next  # começa do primeiro nó
        while True:
            print(aux.item, end=" -> ")
            aux = aux.next
            if aux == self.final.next:
                break
        print()

# função princiapl para imprimir com o usuario


def main():
    circularList = CircularLinkedList()

    circularList.AddLast(10)
    circularList.AddLast(20)
    circularList.AddLast(30)

    # loop para interagir com o usuario
    while True:
        print("\n1 - Adicionar no inicio")
        print("2 - Adicionar no fim")
        print("3 - Remover no inicio")
        print("4 - Remover do fim")
        print("5 - Remover elemento especifico")
        print("6 - Imprimir lista")
        print("7 - Desfazer remoção e adcionar ao incio")
        print("8 - Desfazer remoção e adcionar ao fim")
        print("0 - sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor = int(input("Digite o numero para adicionar no inicio: "))
            circularList.AddFirst(valor)
        elif opcao == 2:
            valor = int(input("Digite o numero para adicionar no fim: "))
            circularList.AddLast(valor)
        elif opcao == 3:
            try:
                circularList.RemoveFirst()
                print("Elemento removido do inicio.")
            except Exception as e:
                print(e)
        elif opcao == 4:
            try:
                circularList.RemoveLast()
                print("Elemento removido do fim.")
            except Exception as e:
                print(e)
        elif opcao == 5:
            valor = int(input("Digite o valor do elemento a ser removido: "))
            if circularList.Remove(valor):
                print(f"Elemeneto {valor} removido.")
            else:
                print(f"Elemento {valor} não encontrado")
        elif opcao == 6:
            circularList.PrintList()
        elif opcao == 7:
            circularList.desfazer_remove_inicio()
        elif opcao == 8:
            circularList.desfazer_remove_fim()
        elif opcao == 0:
            break
        else:
            print("opção inválida. tente novamente.")


# executa o programa
main()
