class Carrinho_compra:
    def __init__(self):
        # iniciando uma lista padrão
        self.P = []
        self.removidos = []

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
        return print(f"item no topo da pilha: {self.P[-1]}")

    def pop(self):
        # Remove elemento do topo da pilha
        if self.is_empty():
            return None
        return self.P.pop()

    def Empilha(self, item):
        # empilha e imprime o estado atual da pilha
        self.push(item)
        print(f"O item '{item}' foi adicionado ao carrinho")

    def Desempilha(self):
        # desempilha e imprime o estado atual da pilha
        x = self.pop()
        if x is None:
            print("Pilha vazia")
        else:
            self.removidos.append(x)
            print(f"O livro '{x}' foi removido")

    def Quantidade(self):
        print(f"Quantidade de livros restantes: {len(self.P)}")

    def Refazer(self):
        # desfaz a remoção do item
        if not self.removidos:
            print("Nenhuma adição para refazer")
            return
        livro = self.removidos.pop()  # remove da pilha de removidos
        self.push(livro)  # empilha novamente na pilha principal
        print(f"O livro '{livro}' foi re-adicionado à pilha")

    def Exibir(self):
        print(self.P)


# Exemplo de uso
pilha = Carrinho_compra()
pilha.Empilha("Celular")
pilha.Empilha("Livro Dom Quixote")
pilha.Empilha("Televisão")
pilha.Empilha("Caixa de som")

while True:
    print('Escolha uma opção:')
    print('1 - Adicionar novo item')
    print('2 - Remover item adicionado')
    print('3 - Item no topo do carrinho')
    print('4 - Verificar se o carrinho está vázio')
    print('5 - Verificar quantidade de itens npo carrinho')
    print('6 - Desfazer a remoção do item')
    print('7 - Mostrar carrinho')
    print('0 - Sair')

    entrada = int(input("Digite a operação: "))

    if entrada == 1:
        item = input('Digite o titulo do item: ')
        pilha.Empilha(item)

    elif entrada == 2:
        pilha.Desempilha()
        pass

    elif entrada == 3:
        livro = pilha.livro_ao_topo()
        if livro:
            print(pilha.livro_ao_topo(), 'itemo no Topo')
        else:
            print('Lista Vazia')

    elif entrada == 4:
        estado_lista = pilha.is_empty()
        if estado_lista:
            print('O carrinho está vázia')
        else:
            print('O carrinho possui itens')

    elif entrada == 5:
        pilha.Quantidade()
        pass

    elif entrada == 6:
        pilha.Refazer()

    elif entrada == 7:
        pilha.Exibir()

    elif entrada == 0:
        print('Saindo...')
        break
