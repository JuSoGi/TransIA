import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def ejecutar_pruebas():
    print("=== PRUEBAS DE TRANSIA ===\n")

    # Prueba 1: cargar los datos
    datos = pd.read_csv("datos_estaciones.csv")

    assert len(datos) == 10
    print("Prueba 1: Carga de 10 estaciones - OK")

    # Prueba 2: verificar las columnas necesarias
    columnas = [
        "estacion",
        "pasajeros_promedio",
        "numero_conexiones",
        "espera_minutos"
    ]

    assert all(columna in datos.columns for columna in columnas)
    print("Prueba 2: Columnas requeridas - OK")

    # Prueba 3: comprobar que no existan datos vacios
    assert not datos[columnas].isnull().any().any()
    print("Prueba 3: Datos completos - OK")

    # Prueba 4: entrenar K-Means
    variables = datos[
        [
            "pasajeros_promedio",
            "numero_conexiones",
            "espera_minutos"
        ]
    ]

    escalador = StandardScaler()
    datos_normalizados = escalador.fit_transform(variables)

    modelo = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    grupos = modelo.fit_predict(datos_normalizados)

    assert len(grupos) == len(datos)
    print("Prueba 4: Agrupamiento de estaciones - OK")

    # Prueba 5: comprobar que se generen tres grupos
    assert len(set(grupos)) == 3
    print("Prueba 5: Generacion de tres grupos - OK")

    print("\nTodas las pruebas finalizaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()