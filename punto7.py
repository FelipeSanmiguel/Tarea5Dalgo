from collections import deque

def max_solapamiento(a, b):
    max_olap = 0
    min_len = min(len(a), len(b))
    for i in range(1, min_len + 1):
        if a[-i:] == b[:i]:
            max_olap = i
    return max_olap

def generar_sucesores(used_mask, T_U, cadenas, k, visitados):
    sucesores = []
    n = len(cadenas)
    for i in range(n):
        if (used_mask & (1 << i)) != 0:
            continue 
        s = cadenas[i]
        olap = max_solapamiento(T_U, s)
        nueva_T = T_U + s[olap:]
        nuevo_mask = used_mask | (1 << i)
        if len(nueva_T) <= k:
            if nuevo_mask not in visitados or len(nueva_T) < visitados[nuevo_mask]:
                sucesores.append((nuevo_mask, nueva_T))
    return sucesores

def problema_decision(cadenas, k):
    visitados = dict()
    cola = deque()
    n = len(cadenas)

    for i in range(n):
        s = cadenas[i]
        mask = 1 << i
        cola.append((mask, s))
        visitados[mask] = len(s)

    while cola:
        used_mask, T_U = cola.popleft()
        if used_mask == (1 << n) - 1 and len(T_U) <= k:
            return True

        for nuevo_mask, nueva_T in generar_sucesores(used_mask, T_U, cadenas, k, visitados):
            visitados[nuevo_mask] = len(nueva_T)
            cola.append((nuevo_mask, nueva_T))

    return False

# Introducir aqui valores
cadenas = ["abc", "bcd", "cde"]
k = 5

valido = problema_decision(cadenas, k)
print("¿Existe una supercadena de longitud menor?"+ str(valido))
