def multiplica(x, y):
    global total
    total = x * y
    print(f"Valores multiplicados da função: {total}")


y = 5
x = 10
global total
total = x * y
multiplica(7, 5)
print(f"multiplicação programa: {total}")
