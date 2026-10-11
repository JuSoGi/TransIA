
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def ejecutar_pruebas():
    print("=== PRUEBAS DE TRANSIA SUPERVISADO ===\n")

    # Cargar el dataset
    datos = pd.read_csv("datos_estaciones.csv")

    # Prueba 1: cantidad de registros
    assert len(datos) == 20
    print("Prueba 1: Carga de 20 registros - OK")

    # Prueba 2: columnas necesarias
    columnas = [
        "estacion",
        "pasajeros_promedio",
        "numero_conexiones",
        "espera_minutos",
        "nivel_demanda"
    ]

    assert all(col in datos.columns for col in columnas)
    print("Prueba 2: Columnas requeridas - OK")

    # Prueba 3: comprobar datos completos
    assert not datos[columnas].isnull().any().any()
    print("Prueba 3: Datos completos - OK")

    # Prueba 4: entrenar el modelo
    X = datos[
        [
            "pasajeros_promedio",
            "numero_conexiones",
            "espera_minutos"
        ]
    ]

    y = datos["nivel_demanda"]

    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = (
        train_test_split(
            X,
            y,
            test_size=0.30,
            random_state=42,
            stratify=y
        )
    )

    modelo = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    modelo.fit(X_entrenamiento, y_entrenamiento)
    print("Prueba 4: Entrenamiento del arbol - OK")

    # Prueba 5: prediccion de una categoria valida
    prediccion = modelo.predict(
        pd.DataFrame(
            [[750, 4, 6]],
            columns=X.columns
        )
    )

    assert prediccion[0] in ["Baja", "Media", "Alta"]
    print("Prueba 5: Prediccion de categoria valida - OK")

    print("\nTodas las pruebas finalizaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()