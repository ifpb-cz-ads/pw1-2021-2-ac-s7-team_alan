L = [15, 7, 27, 39]
p = int(input("Informe o valor a procurar (p):"))
v = int(input("Informe o outro valor a procurar (v):"))
x = 0
achouP = -1
achouV = -1
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = x
    if L[x] == v:
        achouV = x
    x += 1
if achouP != -1:
    print(f"p: {p} encontrado na posição {achouP}")
else:
    print(f"p: {p} não encontrado")
if achouV != -1:
    print(f"v: {v} encontrado na posição {achouV}")
else:
    print(f"v: {v} não encontrado")
if achouP != -1 and achouV != -1:
    if achouP <= achouV:
        print("p foi achado antes de v")
    else:
        print("v foi achado antes de p")