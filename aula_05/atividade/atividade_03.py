import math as mat

while True:
    try:
        print("\nInforme os seguintes valores")
        a = int(input("Insira o valor de A: "))
        b = int(input("Insira o valor de B: "))
        c = int(input("Insira o valor de C: "))

        if a != 0 and b != 0 and c != 0:
            break
        else:
            print("Valores inválidos, os coeficientes devem ser maiores que 0")
    except:
        print("Valores inválidos, insira smente números")


# print(a, b, c)

delta = b**2 - 4*a*c

raiz_delta = mat.sqrt(delta)

x_mais = ((-b) + raiz_delta) / (2 * a)
x_menos = ((-b) - raiz_delta) / (2 * a)

print(f"Resultado X positivo -> {x_mais}\nResultado X negativo -> {x_menos}")
