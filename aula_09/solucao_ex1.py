# Classe que define o nó de uma árvore binária
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None  # Subárvore à esquerda
        self.direita = None   # Subárvore à direita

# Classe que define a árvore binária


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    # Método para verificar se a árvore está vazia
    def esta_vazia(self):
        return self.raiz is None

    # Inserir o primeiro nó, ou seja, a raiz da árvore
    def inserir_raiz(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            print(f"Raiz {valor} adicionada com sucesso.")
        else:
            print("A raiz já existe.")

    # Inserir um nó à esquerda de um nó específico
    def inserir_esquerda(self, valor_pai, valor):
        pai = self.buscar(self.raiz, valor_pai)
        if pai:
            if pai.esquerda is None:
                pai.esquerda = No(valor)
                print(f"Nó {valor} inserido à esquerda de {valor_pai}.")
            else:
                print(f"O nó à esquerda de {valor_pai} já existe.")
        else:
            print(f"Nó {valor_pai} não encontrado.")

    # Inserir um nó à direita de um nó específico
    def inserir_direita(self, valor_pai, valor):
        pai = self.buscar(self.raiz, valor_pai)
        if pai:
            if pai.direita is None:
                pai.direita = No(valor)
                print(f"Nó {valor} inserido à direita de {valor_pai}.")
            else:
                print(f"O nó à direita de {valor_pai} já existe.")
        else:
            print(f"Nó {valor_pai} não encontrado.")

    # Buscar um nó na árvore
    def buscar(self, no, valor):
        if no is None:
            return None
        if no.valor == valor:
            return no
        # Busca recursiva nos subárvores à esquerda e direita
        esquerda = self.buscar(no.esquerda, valor)
        if esquerda is not None:
            return esquerda
        return self.buscar(no.direita, valor)

    # Exibir os nós da árvore em ordem (esquerda, raiz, direita)
    def exibir_em_ordem(self, no):
        if no:
            self.exibir_em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.exibir_em_ordem(no.direita)

    # Exibir os nós da árvore em pré-ordem (raiz, esquerda, direita)
    def exibir_pre_ordem(self, no):
        if no:
            print(no.valor, end=" ")
            self.exibir_pre_ordem(no.esquerda)
            self.exibir_pre_ordem(no.direita)

    # Contar o número total de nós na árvore
    def contar_nos(self, no):
        if no is None:
            return 0
        return 1 + self.contar_nos(no.esquerda) + self.contar_nos(no.direita)

    # Excluir um nó da árvore
    def excluir(self, valor):
        self.raiz, excluido = self._excluir(self.raiz, valor)
        if excluido:
            print(f"Nó {valor} excluído com sucesso.")
        else:
            print(f"Nó {valor} não encontrado.")

    # Função auxiliar para exclusão de nó
    def _excluir(self, no, valor):
        if no is None:
            return no, False
        if valor < no.valor:
            no.esquerda, excluido = self._excluir(no.esquerda, valor)
            return no, excluido
        elif valor > no.valor:
            no.direita, excluido = self._excluir(no.direita, valor)
            return no, excluido
        else:
            # Caso 1: Nó sem filhos
            if no.esquerda is None and no.direita is None:
                return None, True
            # Caso 2: Nó com um filho
            elif no.esquerda is None:
                return no.direita, True
            elif no.direita is None:
                return no.esquerda, True
            # Caso 3: Nó com dois filhos
            else:
                sucessor = self._encontrar_minimo(no.direita)
                no.valor = sucessor.valor
                no.direita, _ = self._excluir(no.direita, sucessor.valor)
                return no, True

    # Função auxiliar para encontrar o valor mínimo em uma subárvore
    def _encontrar_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

# Função de interação com o usuário para operações na árvore binária


def interagir_com_usuario():
    arvore = ArvoreBinaria()

    while True:
        print("\nEscolha uma operação:")
        print("1 - Inserir raiz")
        print("2 - Inserir nó à esquerda")
        print("3 - Inserir nó à direita")
        print("4 - Exibir árvore em ordem")
        print("5 - Exibir árvore em pré-ordem")
        print("6 - Contar nós da árvore")
        print("7 - Excluir um nó")
        print("8 - Sair")

        opcao = input("Digite a opção: ")

        if opcao == "1":
            valor = int(input("Digite o valor da raiz: "))
            arvore.inserir_raiz(valor)
        elif opcao == "2":
            valor_pai = int(input("Digite o valor do nó pai: "))
            valor = int(input("Digite o valor do novo nó à esquerda: "))
            arvore.inserir_esquerda(valor_pai, valor)
        elif opcao == "3":
            valor_pai = int(input("Digite o valor do nó pai: "))
            valor = int(input("Digite o valor do novo nó à direita: "))
            arvore.inserir_direita(valor_pai, valor)
        elif opcao == "4":
            print("Árvore em ordem (esquerda, raiz, direita): ", end="")
            arvore.exibir_em_ordem(arvore.raiz)
            print()
        elif opcao == "5":
            print("Árvore em pré-ordem (raiz, esquerda, direita): ", end="")
            arvore.exibir_pre_ordem(arvore.raiz)
            print()
        elif opcao == "6":
            print(f"Número total de nós: {arvore.contar_nos(arvore.raiz)}")
        elif opcao == "7":
            valor = int(input("Digite o valor do nó a ser excluído: "))
            arvore.excluir(valor)
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Programa principal
if __name__ == "__main__":
    interagir_com_usuario()
