from collections import deque

def max_solapamiento(a, b):
    max_olap = 0
    min_len = min(len(a), len(b))
    for i in range(1, min_len + 1):
        if a[-i:] == b[:i]:
            max_olap = i
    return max_olap

def generar_sucesores(used_list, T_U, cadenas, k, visitados):
    sucesores = []
    n = len(cadenas)
    for i in range(n):
        if i in used_list:
            continue  # cadena i ya usada
        s = cadenas[i]
        olap = max_solapamiento(T_U, s)
        nueva_T = T_U + s[olap:]
        nuevo_list = used_list + [i]
        clave_estado = tuple(sorted(nuevo_list))
        if len(nueva_T) <= k:
            if clave_estado not in visitados or len(nueva_T) < visitados[clave_estado]:
                sucesores.append((nuevo_list, nueva_T))
    return sucesores

def problema_decision(cadenas, k):
    visitados = dict()
    cola = deque()
    n = len(cadenas)

    for i in range(n):
        s = cadenas[i]
        used_list = [i]
        cola.append((used_list, s))
        visitados[tuple(sorted(used_list))] = len(s)

    while cola:
        used_list, T_U = cola.popleft()
        if len(used_list) == n and len(T_U) <= k:
            return True

        for nuevo_list, nueva_T in generar_sucesores(used_list, T_U, cadenas, k, visitados):
            clave_estado = tuple(sorted(nuevo_list))
            visitados[clave_estado] = len(nueva_T)
            cola.append((nuevo_list, nueva_T))

    return False

# Poner aqui valores
cadenas = ["abc", "bcd", "cde"]
k = 5

valido = problema_decision(cadenas, k)
print("Existe una cadena menor?: ", str(valido))
