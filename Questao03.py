primeiraLista = []
segundaLista = []
while True:
    e = int(input("Informe um valor para a primeira lista (Digite 0 para terminar): "))
    if e == 0:
        break
    primeiraLista.append(e)
while True:
    e = int(input("Informe um valor para a segunda lista (Digite 0 para terminar): "))
    if e == 0:
        break
    segundaLista.append(e)
terceiraLista = []
listaAux = primeiraLista[:]
listaAux.extend(segundaLista)
x = 0
while x < len(listaAux):
    y = 0
    while y < len(terceiraLista):
        if listaAux[x] == terceiraLista[y]:
            break
        y = y + 1
    if y == len(terceiraLista):
        terceiraLista.append(listaAux[x])
    x = x + 1
x = 0
while x < len(terceiraLista):
    print(f"{x}: {terceiraLista[x]}")
    x = x + 1