xs = [1, 3, 7, 9, 10, 11, 13]
i = 0
while i < len(xs):
    if xs[i] % 2 == 0:
        print("há numero par")
        break
    i += 1
else:
    print("não há numero par")
