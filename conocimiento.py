reglas = [
    ("Portal Norte", "Calle 100", 1),
    ("Calle 100", "Héroes", 1),
    ("Héroes", "Calle 72", 1),
    ("Héroes", "NQS", 1),
    ("Calle 72", "Calle 57", 1),
    ("Calle 57", "Universidades", 1),
    ("Universidades", "Museo del Oro", 1),
    ("NQS", "Ricaurte", 1),
    ("Ricaurte", "Calle 19", 1),
    ("Calle 19", "Museo del Oro", 1)
]


coordenadas = {
    "Portal Norte": (0, 0),
    "Calle 100": (1, 0),
    "Héroes": (2, 0),
    "Calle 72": (3, 0),
    "Calle 57": (4, 0),
    "Universidades": (5, 0),
    "Museo del Oro": (6, 0),
    "NQS": (2, 1),
    "Ricaurte": (3, 2),
    "Calle 19": (4, 1)
}

estaciones = [
    "Portal Norte",
    "Calle 100",
    "Héroes",
    "Calle 72",
    "Calle 57",
    "Universidades",
    "Museo del Oro",
    "NQS",
    "Ricaurte",
    "Calle 19"
]


def construir_grafo(reglas):
    grafo = {}

    for origen, destino, costo in reglas:
        if origen not in grafo:
            grafo[origen] = []

        if destino not in grafo:
            grafo[destino] = []

        grafo[origen].append((destino, costo))
        grafo[destino].append((origen, costo))

    return grafo