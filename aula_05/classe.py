class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Lista_encadeada:
    def __init__(self):
        self.cabeca = None
        self.removidos = []  # Lista para armazenar os itens removidos

    def adicionar_no_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def adicionar_no_fim(self, valor):
        novo_no = No(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def buscar(self, valor):
        atual = self.cabeca
        posicao = 0
        while atual:
            if atual.valor == valor:
                return f"Elemento {valor} encontrado na posição {posicao}"
            atual = atual.proximo
            posicao += 1
        return f"Elemento {valor} não encontrado"

    def remover(self, valor):
        if not self.cabeca:
            return "A lista está vazia"

        if self.cabeca.valor == valor:
            self.removidos.append(self.cabeca)  # Armazena o nó removido
            self.cabeca = self.cabeca.proximo
            return f"Elemento {valor} removido"

        atual = self.cabeca
        anterior = None
        while atual:
            if atual.valor == valor:
                self.removidos.append(atual)  # Armazena o nó removido
                anterior.proximo = atual.proximo
                return f"Elemento {valor} removido."
            anterior = atual
            atual = atual.proximo
        return f"Elemento {valor} não encontrado"

    def desfazer_remocao(self):
        if not self.removidos:
            print("Nenhum item para desfazer a remoção.")
        else:
            no_restaurado = self.removidos.pop()
            # Adiciona o item removido de volta à lista no início
            self.adicionar_no_inicio(no_restaurado.valor)
            print(
                f"Remoção desfeita, item {no_restaurado.valor} adicionado novamente no início.")

    def percorrer_lista(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=' --> ')
            atual = atual.proximo
        print("None")


# Testando as funcionalidades
lista = Lista_encadeada()
lista.adicionar_no_inicio(5)
lista.adicionar_no_inicio(3)
lista.adicionar_no_fim(7)

print("Lista Completa: ")
lista.percorrer_lista()

# Buscar um valor
print(lista.buscar(7))

# Remover um item específico
lista.remover(3)
print("Lista Completa após remoção de 3: ")
lista.percorrer_lista()

# Desfazer a remoção
lista.desfazer_remocao()
print("Lista Completa após desfazer a remoção: ")
lista.percorrer_lista()

# Remover outro item
lista.remover(5)
print("Lista Completa após remoção de 5: ")
lista.percorrer_lista()

# Desfazer a remoção novamente
lista.desfazer_remocao()
print("Lista Completa após desfazer a remoção: ")
lista.percorrer_lista()
