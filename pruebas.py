from conocimiento import reglas, construir_grafo, coordenadas
from busqueda import buscar_ruta_a_estrella


grafo = construir_grafo(reglas)

def prueba_ruta_existente():
    inicio = "Portal Norte"
    destino = "Museo del Oro"

    ruta = buscar_ruta_a_estrella(
        grafo,
        inicio,
        destino,
        coordenadas
    )

    assert ruta is not None

    print("PRUEBA 1: Ruta existente")
    print("Resultado:", " -> ".join(ruta))
    print("Estado: OK\n")

def prueba_mismo_origen_destino():
    inicio = "Héroes"
    destino = "Héroes"

    ruta = buscar_ruta_a_estrella(
        grafo,
        inicio,
        destino,
        coordenadas
    )

    assert ruta == ["Héroes"]

    print("PRUEBA 2: Mismo origen y destino")
    print("Resultado:", " -> ".join(ruta))
    print("Estado: OK\n")

def prueba_destino_inexistente():
    inicio = "Portal Norte"
    destino = "EstacionInventada"

    ruta = buscar_ruta_a_estrella(
        grafo,
        inicio,
        destino,
        coordenadas
    )

    assert ruta is None

    print("PRUEBA 3: Destino inexistente")
    print("Resultado: No se encontró una ruta.")
    print("Estado: OK\n")

def prueba_origen_inexistente():
    inicio = "EstacionInventada"
    destino = "Museo del Oro"

    ruta = buscar_ruta_a_estrella(
        grafo,
        inicio,
        destino,
        coordenadas
    )

    assert ruta is None

    print("PRUEBA 4: Origen inexistente")
    print("Resultado: No se encontró una ruta.")
    print("Estado: OK\n")

def prueba_ruta_alternativa():
    inicio = "Héroes"
    destino = "Museo del Oro"

    ruta = buscar_ruta_a_estrella(
        grafo,
        inicio,
        destino,
        coordenadas
    )

    assert ruta is not None

    print("PRUEBA 5: Ruta alternativa")
    print("Resultado:", " -> ".join(ruta))
    print("Estado: OK\n")    

def ejecutar_pruebas():
    prueba_ruta_existente()
    prueba_mismo_origen_destino()
    prueba_destino_inexistente()
    prueba_origen_inexistente()
    prueba_ruta_alternativa()


if __name__ == "__main__":
    ejecutar_pruebas()            