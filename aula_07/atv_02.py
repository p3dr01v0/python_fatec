class Pilha:
    def __init__(self):
        # iniciando uma lista padrão
        self.P = []

    def push(self, x):
        # empilha novo elemento
        self.P.append(x)

    def is_empty(self):
        # retorna True se a pilha está vazia
        return len(self.P) == 0

    def top(self):
        # retorna o elemento no topo da pilha mas não desempilha
        if self.is_empty():
            return None
        return print(f"livro no topo da pilha: {self.P[-1]}")

    def pop(self):
        # Remove elemento do topo da pilha
        if self.is_empty():
            return None
        return self.P.pop()

    def Empilha(self, livro):
        # empilha e imprime o estado atual da pilha
        self.push(livro)
        print(f"O livro '{livro}' foi adicionado à pilha")

    def Desempilha(self):
        # desempilha e imprime o estado atual da pilha
        x = self.pop()
        if x is None:
            print("Pilha vazia")
        else:
            print(f"O livro '{x}' foi removido")

    def Quantidade(self):
        print(f"Quantidade de itens restantes: {len(self.P)}")

    def Carrinho_atual(self):
        print(self.P)


pilha = Pilha()
# Exemplo de uso
pilha.Empilha("Celular")
pilha.Empilha("Televisão")
pilha.Empilha("Caixa de Som")
pilha.Empilha("Carro")
pilha.Desempilha()
pilha.Desempilha()
pilha.top()
pilha.Quantidade()
