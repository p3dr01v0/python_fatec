i = 1
lista = []

while i < 4:
    cliente = input("insira o nome do cliente: ")
    lista.append(cliente)
    i += 1

print("\nClientes cadastrados")
lista.sort()

for nome in lista:
    print(nome)

print("\nlista dos clientes ao contrario: ")

lista.reverse()

for nome in lista:
    print(nome)
