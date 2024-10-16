i = 0
lista = []

limite = int(input("Quantas notas vão ser lançadas: "))

while i < limite:
    nota = float(input(f"informe a nota {i + 1}: "))
    lista.append(nota)
    i += 1

media = float(sum(lista) / len(lista))

print(f"a media das notas é: {media}")
