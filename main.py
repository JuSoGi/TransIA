from conocimiento import reglas, construir_grafo, coordenadas, estaciones
from busqueda import buscar_ruta_a_estrella, obtener_costo_ruta


grafo = construir_grafo(reglas)


def encontrar_estacion(nombre):
    for estacion in grafo:
        if estacion.lower() == nombre.lower():
            return estacion

    return None


def main():
    print("========================================")
    print("              TRANSIA")
    print("     Sistema inteligente de rutas")
    print("========================================")

    print("\nEstaciones disponibles:")

    for estacion in estaciones:
        print("-", estacion)

    print()

    inicio_usuario = input(
        "Ingrese la estación de origen: "
    ).strip()

    destino_usuario = input(
        "Ingrese la estación de destino: "
    ).strip()

    inicio = encontrar_estacion(inicio_usuario)
    destino = encontrar_estacion(destino_usuario)

    if inicio is None:
        print("La estación de origen no existe.")
        return

    if destino is None:
        print("La estación de destino no existe.")
        return

    ruta = buscar_ruta_a_estrella(
        grafo,
        inicio,
        destino,
        coordenadas
    )

    if ruta:
        costo = obtener_costo_ruta(grafo, ruta)

        print("\nRuta encontrada:")
        print(" -> ".join(ruta))
        print("Costo total:", costo)
        print("Número de estaciones:", len(ruta))
    else:
        print("\nNo se encontró una ruta.")


if __name__ == "__main__":
    main()