alunosams = [8,9,10]
alunosads = [7,8,9]

print(alunosams > alunosads)
print(alunosams == alunosads)
print(alunosams != alunosads)

c1 = set(alunosams)
c2 = set(alunosads)

print(c1 & c2) 
print(c1 - c2)
print(c1 ^ c2) 