from collections import deque
import heapq


def heuristica(estacion_actual, destino, coordenadas):
    x1, y1 = coordenadas[estacion_actual]
    x2, y2 = coordenadas[destino]

    return abs(x1 - x2) + abs(y1 - y2)


def buscar_ruta_bfs(grafo, inicio, destino):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        ruta = cola.popleft()
        estacion_actual = ruta[-1]

        if estacion_actual == destino:
            return ruta

        if estacion_actual in visitados:
            continue

        visitados.add(estacion_actual)

        for vecino, costo in grafo.get(estacion_actual, []):

            if vecino not in visitados:
                nueva_ruta = ruta + [vecino]
                cola.append(nueva_ruta)

    return None


def buscar_ruta_a_estrella(grafo, inicio, destino, coordenadas):

    if inicio not in grafo:
        return None

    if destino not in grafo:
        return None

    cola = []

    heapq.heappush(
        cola,
        (0, 0, inicio, [inicio])
    )

    costos = {
        inicio: 0
    }

    while cola:

        prioridad, costo_actual, estacion_actual, ruta = heapq.heappop(cola)

        if costo_actual > costos.get(estacion_actual, float("inf")):
            continue

        if estacion_actual == destino:
            return ruta

        for vecino, costo in grafo.get(estacion_actual, []):

            nuevo_costo = costo_actual + costo

            if vecino not in costos or nuevo_costo < costos[vecino]:

                costos[vecino] = nuevo_costo

                estimacion = heuristica(
                    vecino,
                    destino,
                    coordenadas
                )

                nueva_prioridad = nuevo_costo + estimacion

                nueva_ruta = ruta + [vecino]

                heapq.heappush(
                    cola,
                    (
                        nueva_prioridad,
                        nuevo_costo,
                        vecino,
                        nueva_ruta
                    )
                )

    return None


def obtener_costo_ruta(grafo, ruta):

    costo_total = 0

    for i in range(len(ruta) - 1):

        origen = ruta[i]
        destino = ruta[i + 1]

        for vecino, costo in grafo[origen]:

            if vecino == destino:
                costo_total += costo
                break

    return costo_total