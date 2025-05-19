from collections import deque

def max_solapamiento(cadena_a, cadena_b):
    max_solap = 0
    longitud_min = min(len(cadena_a), len(cadena_b))
    for i in range(1, longitud_min + 1):
        if cadena_a[-i:] == cadena_b[:i]:
            max_solap = i
    return max_solap

def generar_sucesores(lista_usados, cadena_actual, cadenas, k, visitados):
    sucesores = []
    n = len(cadenas)
    for i in range(n):
        if i in lista_usados:
            continue  
        cadena_siguiente = cadenas[i]
        solapamiento = max_solapamiento(cadena_actual, cadena_siguiente)
        nueva_cadena = cadena_actual + cadena_siguiente[solapamiento:]
        nueva_lista_usados = lista_usados + [i]
        clave_estado = tuple(sorted(nueva_lista_usados))
        if len(nueva_cadena) <= k:
            if clave_estado not in visitados or len(nueva_cadena) < visitados[clave_estado]:
                sucesores.append((nueva_lista_usados, nueva_cadena))
    return sucesores

def problema_decision(cadenas, k):
    visitados = dict()
    cola = deque()
    n = len(cadenas)

    for i in range(n):
        cadena_inicial = cadenas[i]
        lista_usados = [i]
        cola.append((lista_usados, cadena_inicial))
        visitados[tuple(sorted(lista_usados))] = len(cadena_inicial)

    while cola:
        lista_usados, cadena_actual = cola.popleft()
        if len(lista_usados) == n and len(cadena_actual) <= k:
            return True

        for nueva_lista_usados, nueva_cadena in generar_sucesores(lista_usados, cadena_actual, cadenas, k, visitados):
            clave_estado = tuple(sorted(nueva_lista_usados))
            visitados[clave_estado] = len(nueva_cadena)
            cola.append((nueva_lista_usados, nueva_cadena))

    return False

# Poner aqui valores
cadenas = ["abc", "bcd", "cde"]
k = 5

valido = problema_decision(cadenas, k)
print("Existe una cadena menor?: ", str(valido))
