i = 1
lista = []

while i < 7:
    num = int(input('insira um número: '))
    lista.append(int(num))
    i += 1

num_extra = int(input('insira um numero novo: '))

lista.append(num_extra)

lista_invertida = lista[::-1]

for numero in lista_invertida:
    print(numero)
