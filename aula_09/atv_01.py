class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def esta_vazia(self):
        return self.raiz is None

    def inserir_raiz(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            print(f"Raiz {valor} adicionada com sucesso")
        else:
            print("A raiz já existe")

    def inserir_esquerda(self, valor_pai, valor):
        pai = self.buscar(self.raiz, valor_pai)
        if pai:
            if pai.esquerda is None:
                pai.esquerda = No(valor)
                print(f"Nó {valor} inserido à esquerda de {
                      valor_pai} com sucesso.")
            else:
                print(f"Nó à esquerda de {valor_pai} já existe.")
        else:
            print(f"Nó {valor_pai} não encontrado")

    def inserir_direita(self, valor_pai, valor):
        pai = self.buscar(self.raiz, valor_pai)
        if pai:
            if pai.direita is None:
                pai.direita = No(valor)
                print(f"Nó {valor} inserido à direita de {
                      valor_pai} com sucesso.")
            else:
                print(f"Nó à direita de {valor_pai} já existe.")
        else:
            print(f"Nó {valor_pai} não encontrado")

    def buscar(self, nodo, valor):
        if nodo is None:
            return None
        if nodo.valor == valor:
            return nodo
        resultado = self.buscar(nodo.esquerda, valor)
        if resultado is not None:
            return resultado
        return self.buscar(nodo.direita, valor)

    def percorrer_pre_ordem(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.percorrer_pre_ordem(nodo.esquerda)
            self.percorrer_pre_ordem(nodo.direita)

    def percorrer_pos_ordem(self, nodo):
        if nodo is not None:
            self.percorrer_pos_ordem(nodo.esquerda)
            self.percorrer_pos_ordem(nodo.direita)
            print(nodo.valor, end=' ')


arvore = ArvoreBinaria()

arvore.inserir_raiz(50)        # Raiz
arvore.inserir_esquerda(50, 30)  # 30 à esquerda de 50
arvore.inserir_direita(50, 40)   # 40 à direita de 50
arvore.inserir_esquerda(30, 20)  # 20 à direita de 30
arvore.inserir_esquerda(40, 70)   # 70 à esquerda de 40
arvore.inserir_direita(40, 60)    # 60 à direita de 40
arvore.inserir_esquerda(70, 80)   # 80 à esquerda de 70

print("Percurso em pré-ordem:")
arvore.percorrer_pre_ordem(arvore.raiz)  # Exibe a ordem de visita em pré-ordem
print("\nPercurso em pós-ordem:")
arvore.percorrer_pos_ordem(arvore.raiz)  # Exibe a ordem de visita em pós-ordem
