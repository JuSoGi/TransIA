
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# 1. Cargar los datos de las estaciones
datos = pd.read_csv("datos_estaciones.csv")

print("=== TRANSIA: AGRUPAMIENTO DE ESTACIONES ===")
print("\nDatos cargados:")
print(datos)


# 2. Seleccionar las variables numericas
variables = datos[
    [
        "pasajeros_promedio",
        "numero_conexiones",
        "espera_minutos"
    ]
]


# 3. Normalizar los datos
escalador = StandardScaler()
datos_normalizados = escalador.fit_transform(variables)


# 4. Crear y entrenar el modelo K-Means
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

datos["grupo"] = modelo.fit_predict(datos_normalizados)


# 5. Mostrar los resultados
print("\n=== ESTACIONES AGRUPADAS ===")

for grupo in sorted(datos["grupo"].unique()):
    print(f"\nGrupo {grupo + 1}:")

    estaciones = datos[datos["grupo"] == grupo]

    for _, fila in estaciones.iterrows():
        print("-", fila["estacion"])

print("\n=== TABLA FINAL ===")
print(datos.to_string(index=False))


# 6. Crear una grafica de los grupos
plt.figure(figsize=(10, 6))

for grupo in sorted(datos["grupo"].unique()):
    estaciones = datos[datos["grupo"] == grupo]

    plt.scatter(
        estaciones["pasajeros_promedio"],
        estaciones["espera_minutos"],
        label=f"Grupo {grupo + 1}",
        s=100
    )

    for _, fila in estaciones.iterrows():
        plt.annotate(
            fila["estacion"],
            (
                fila["pasajeros_promedio"],
                fila["espera_minutos"]
            ),
            fontsize=8
        )

plt.title("TransIA: Agrupamiento de estaciones con K-Means")
plt.xlabel("Pasajeros promedio (dato simulado)")
plt.ylabel("Tiempo de espera en minutos (dato simulado)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("grafica_agrupamiento.png", dpi=150)
plt.show()

# 7. Guardar los resultados en un archivo CSV
datos.to_csv("resultados_agrupamiento.csv", index=False)

print("\nGrafica guardada en grafica_agrupamiento.png")
print("Resultados guardados en resultados_agrupamiento.csv")