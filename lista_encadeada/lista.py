class No():

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class lista_encadeada():

    def __init__(self):
        self.cabeca = None
        self.qtde = 0

    def adicionar_inicio(self, valor):
        novo_no = No(valor)

        novo_no.proximo = self.cabeca

        self.cabeca = novo_no

        self.qtde += 1

    def adicionar_fim(self, valor):
        novo_no = No(valor)

        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            no_atual = self.cabeca
            while no_atual.proximo is not None:
                no_atual = no_atual.proximo
            no_atual.proximo = novo_no

        self.qtde += 1

    def remover_no(self, valor):
        no_atual = self.cabeca
        anterior = None

        while no_atual is not None:
            if anterior == valor:
                if anterior is None:
                    self.cabeca = no_atual.proximo
                else:
                    anterior.proximo = no_atual.proximo

                self.qtde -= 1
                print(f"Nó {valor} removido")
                return
            anterior = no_atual
            no_atual = no_atual.proximo
        print(f"Nó {valor} não encontrado")

    def buscar_tarefas(self, valor):
        atual = self.cabeca
        posicao = 0
        while atual is not None:
            if atual.valor == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        return -1

    def exibir_lista(self):
        atual = self.cabeca
        print("Lista de tarefas: ")
        while atual is not None:
            print(f"Tarefa {atual.proximo}", end=" -> ")
            atual = atual.proximo
        print("None")
        print(f"Tamanho da lista: {self.qtde}")


lista = lista_encadeada()

# Chamando o método adicionar_no_inicio a partir da instância
lista.adicionar_inicio(1)
lista.adicionar_inicio(2)
lista.adicionar_inicio(3)
lista.adicionar_fim(0)
lista.remover_no(0)
lista.exibir_lista()

lista.buscar_tarefas("teste1")
