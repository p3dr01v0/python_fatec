idade = int(input("digite sua idade: "))

if idade in range(0, 13):
    print("criança")
elif idade in range(13, 18):
    print("adolescente")
elif idade in range(18, 60):
    print("adulto")
elif idade <= 60:
    print("idoso")
else:
    print("idade invalida")
