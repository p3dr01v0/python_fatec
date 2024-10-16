numero = input("Digite um número: ")
soma = 0
i = 0

while i < len(numero):
    digito = int(numero[i])
    soma += digito
    i += 1

print("A soma dos dígitos é:", soma)
