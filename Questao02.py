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
terceiraLista = primeiraLista[:]
terceiraLista.extend(segundaLista)
x = 0
while x < len(terceiraLista):
    print(f"{x}: {terceiraLista[x]}")
    x = x + 1