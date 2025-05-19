import random

def agregar_arista(grafo, u, v):
    if v not in grafo[u]:
        grafo[u].append(v)
    if u not in grafo[v]:
        grafo[v].append(u)

def generar_grafo(n, k):
    if k >= n:
        raise ValueError("k debe ser menor que n")

    grafo = [[] for _ in range(n)]

    for i in range(k):
        for j in range(i + 1, k):
            agregar_arista(grafo, i, j)

    for i in range(k, n):
        posibles_vecinos = list(range(n))
        posibles_vecinos.remove(i)

        num_aristas = random.randint(1, k - 1)
        vecinos = random.sample(posibles_vecinos, num_aristas)

        for v in vecinos:
            agregar_arista(grafo, i, v)

    return grafo

# Entradasa para ejecutar creacion de grafo
n = 5
k = 3
grafo = generar_grafo(n, k)

# Imprimir grafo
for i, vecinos in enumerate(grafo):
    print(f"{i}: {sorted(vecinos)}")
