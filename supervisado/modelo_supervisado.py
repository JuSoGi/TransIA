
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report


# 1. Cargar los datos
datos = pd.read_csv("datos_estaciones.csv")

print("=== TRANSIA: APRENDIZAJE SUPERVISADO ===")
print("\nDatos cargados:")
print(datos)


# 2. Separar variables de entrada y categoria objetivo
X = datos[
    [
        "pasajeros_promedio",
        "numero_conexiones",
        "espera_minutos"
    ]
]

y = datos["nivel_demanda"]


# 3. Separar datos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = (
    train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y
    )
)


# 4. Crear y entrenar el arbol de decision
modelo = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

modelo.fit(X_entrenamiento, y_entrenamiento)


# 5. Predecir las categorias
predicciones = modelo.predict(X_prueba)


# 6. Mostrar resultados
precision = accuracy_score(y_prueba, predicciones)

print("\n=== RESULTADOS ===")
print("Categorias reales:", list(y_prueba))
print("Categorias predichas:", list(predicciones))
print(f"Exactitud del modelo: {precision:.2%}")

print("\nReporte de clasificacion:")
print(classification_report(
    y_prueba,
    predicciones,
    zero_division=0
))


# 7. Probar una nueva estacion
nueva_estacion = pd.DataFrame(
    [[750, 4, 6]],
    columns=X.columns
)

prediccion = modelo.predict(nueva_estacion)

print("=== PREDICCION DE EJEMPLO ===")
print("Pasajeros: 750")
print("Conexiones: 4")
print("Espera: 6 minutos")
print("Nivel de demanda estimado:", prediccion[0])


# 8. Dibujar el arbol de decision
plt.figure(figsize=(14, 8))

plot_tree(
    modelo,
    feature_names=X.columns,
    class_names=modelo.classes_,
    filled=True,
    rounded=True
)

plt.title("TransIA: Arbol de decision para clasificar la demanda")
plt.tight_layout()
plt.savefig("arbol_decision.png", dpi=150)
plt.show()


# 9. Guardar resultados de prueba
resultados = X_prueba.copy()
resultados["categoria_real"] = y_prueba
resultados["categoria_predicha"] = predicciones

resultados.to_csv("resultados_supervisado.csv", index=False)

print("\nArchivos generados:")
print("- arbol_decision.png")
print("- resultados_supervisado.csv")