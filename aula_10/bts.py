class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)
    
    def exibir_em_ordem(self):
        valores = []
        self._em_ordem(self.raiz, valores)
        print("Valores em ordem crescente:", valores)

    def _em_ordem(self, no_atual, valores):
        if no_atual is not None:
            self._em_ordem(no_atual.esquerda, valores)
            valores.append(no_atual.valor)
            self._em_ordem(no_atual.direita, valores)

    def buscar(self, valor):
        encontrado = self._buscar_recursivo(self.raiz, valor)
        if encontrado:
            print(f"Valor {valor} encontrado na árvore.")
        else:
            print(f"Valor {valor} não encontrado na árvore.")

    def _buscar_recursivo(self, no_atual, valor):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        elif valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)

    def altura(self):
        altura_arvore = self._calcular_altura(self.raiz)
        print("Altura da árvore:", altura_arvore)
        return altura_arvore

    def _calcular_altura(self, no_atual):
        if no_atual is None:
            return -1  # Retorna -1 para que uma árvore com um único nó tenha altura 0
        altura_esquerda = self._calcular_altura(no_atual.esquerda)
        altura_direita = self._calcular_altura(no_atual.direita)
        return 1 + max(altura_esquerda, altura_direita)

# Menu de opções
def menu():
    arvore = BST()
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar valor")
        print("2. Buscar valor")
        print("3. Exibir valores em ordem crescente")
        print("4. Exibir altura da árvore")
        print("5. Finalizar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valor = int(input("Digite o valor a ser adicionado: "))
            arvore.inserir(valor)
            print(f"Valor {valor} adicionado na árvore.")
        
        elif opcao == "2":
            valor = int(input("Digite o valor a ser buscado: "))
            arvore.buscar(valor)
        
        elif opcao == "3":
            arvore.exibir_em_ordem()
        
        elif opcao == "4":
            arvore.altura()
        
        elif opcao == "5":
            print("Finalizando o programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    menu()
