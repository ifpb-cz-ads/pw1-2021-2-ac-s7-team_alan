notas = [0] * 7
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f"Nota {x+1}:"))
    soma += notas[x]
    x+= 1
x = 0
while x < 7:
    print(f"Nota {x+1}: {notas[x]:5.2f}")
    x+= 1
print(f"Media: {soma/x:5.2f}")