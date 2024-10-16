class Tarefa:

    def __init__(self, numero):
        # Cada tarefa tem um número (identificador) e uma referência para a próxima tarefa
        self.numero = numero
        self.proximo = None


class ListaDeTarefas:

    def __init__(self):
        # A lista começa sem nenhuma tarefa (cabeça vazia) e com quantidade zero
        self.cabeca = None
        self.quantidade = 0

    def adicionar_no_inicio(self, numero):
        # Cria uma nova tarefa
        nova_tarefa = Tarefa(numero)
        # A nova tarefa aponta para a cabeça atual
        nova_tarefa.proximo = self.cabeca
        # A nova tarefa passa a ser a cabeça da lista
        self.cabeca = nova_tarefa
        # Incrementa a quantidade de tarefas
        self.quantidade += 1
        print(f"Tarefa {numero} adicionada no início da lista.")

    def adicionar_no_fim(self, numero):
        # Cria uma nova tarefa
        nova_tarefa = Tarefa(numero)
        # Se a lista estiver vazia, a nova tarefa será a cabeça
        if self.cabeca is None:
            self.cabeca = nova_tarefa

        else:
            # Percorre até o final da lista
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            # Adiciona a nova tarefa no final
            atual.proximo = nova_tarefa
        # Incrementa a quantidade de tarefas
        self.quantidade += 1
        print(f"Tarefa {numero} adicionada no fim da lista.")

    def remover_tarefa(self, numero):
        # Começa a buscar a tarefa a partir da cabeça
        atual = self.cabeca
        anterior = None
        while atual is not None:
            # Se a tarefa for encontrada
            if atual.numero == numero:
                # Se for a primeira tarefa (cabeça)
                if anterior is None:
                    # A cabeça agora será a próxima tarefa
                    self.cabeca = atual.proximo
                else:
                    # Remove a tarefa da lista
                    anterior.proximo = atual.proximo
                # Decrementa a quantidade de tarefas
                self.quantidade -= 1
                print(f"Tarefa {numero} removida.")
                return
            # Continua a busca para a próxima tarefa
            anterior = atual
            atual = atual.proximo
        # Se não encontrou a tarefa
        print(f"Tarefa {numero} não encontrada.")

    def buscar_tarefas(self, numero):
        atual = self.cabeca
        posicao = 0
        while atual is not None:
            if atual.numero == numero:
                return posicao
            atual = atual.proximo
            posicao += 1
        return -1

    def exibir_tarefas(self):
        atual = self.cabeca
        print("Lista de tarefas: ")
        while atual is not None:
            print(f"Tarefa {atual.proximo}", end=" -> ")
            atual = atual.proximo
        print("None")
        print(f"Tamanho da lista: {self.quantidade}")


# chamando as funções

# Criando uma instância da ListaDeTarefas
lista = ListaDeTarefas()

# Chamando o método adicionar_no_inicio a partir da instância
lista.adicionar_no_inicio(1)
