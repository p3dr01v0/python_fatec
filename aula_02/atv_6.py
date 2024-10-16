altura = float(input("informe sua altura em M: "))
peso = float(input("informe seu peso em KQ: "))

if altura > 0 and peso > 0:
    imc = float(peso / (altura * altura))

    if imc < 18.5:
        print(f"abaixo do peso -> {round(imc, 2)}")
    elif imc > 18.5 and imc < 24.9:
        print(f"peso normal -> {round(imc, 2)}")
    elif imc > 25 and imc < 29.9:
        print(f"sobrepeso -> {round(imc, 2)}")
    elif imc > 30 and imc < 34.9:
        print(f"obesidade 1 -> {round(imc, 2)}")
    elif imc > 35 and imc < 39.9:
        print(f"obesidade 2 -> {round(imc, 2)}")
    elif imc > 40:
        print(f"obesidade 3 -> {round(imc, 2)}")
else:
    print("Imc inválido")
