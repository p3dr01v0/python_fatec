fib = [0, 1]

while len(fib) < 15:
    num = fib[-1] + fib[-2]
    fib.append(num)

print(fib)
