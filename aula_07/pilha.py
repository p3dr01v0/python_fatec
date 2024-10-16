def init(P):
    P = []


def push(P, x):
    # empilha novo elemento
    P.append(x)


def top(P):
    # retorna o elemento no topo da pilha mas não desempilha
    if is_empty(P):
        return None
    return P[-1]


def pop(P):
    # Remove elemento do topo da pilha
    if is_empty(P):
        return None
    return P.pop()


# retorna True se a pilha está vazia
def is_empty(P):
    return len(P) == 0


def Empilha(p, z):
    # empilha e imprime o estado atual da pilha
    push(p, z)
    print(p)


def Desempilha(p):
    # desempilha e imprime o estado atual da pilha
    x = pop(p)
    if x is None:
        print("Vazia")
    else:
        print(p)


# inicia a pilha
mp = []
init(mp)


# operacoes
Empilha(mp, 1)
Empilha(mp, "tipo de elemento")
Empilha(mp, (5, 4, 3))
Empilha(mp, True)
print(top(mp))
Desempilha(mp)  # desempilha True
Desempilha(mp)  # desempilha a lista
Desempilha(mp)  # desempilha o texto
Desempilha(mp)  # desempilha o 1
Desempilha(mp)
print(top(mp))
