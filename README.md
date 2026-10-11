
# TransIA — Sistema inteligente de transporte

## 1. Descripción del proyecto

TransIA es un proyecto académico desarrollado en Python para aplicar conceptos de inteligencia artificial al contexto del transporte masivo.

El proyecto cuenta con dos componentes:

- **Búsqueda de rutas:** utiliza una base de conocimiento con conexiones entre estaciones y el algoritmo A* para encontrar una ruta de costo mínimo dentro de una red simplificada.
- **Agrupamiento de estaciones:** utiliza aprendizaje no supervisado con K-Means para agrupar estaciones según características numéricas simuladas.


## 2. Objetivos

- Representar conexiones entre estaciones mediante una base de conocimiento.
- Aplicar el algoritmo A* para buscar rutas.
- Utilizar K-Means para identificar grupos de estaciones con características similares.
- Validar el funcionamiento mediante pruebas y evidencias.

## 3. Tecnologías utilizadas

- Python 3
- pandas
- scikit-learn
- matplotlib
- Git y GitHub

## 4. Estructura del proyecto

```text
TransIA/
├── main.py
├── conocimiento.py
├── busqueda.py
├── pruebas.py
├── README.md
└── agrupamiento/
    ├── datos_estaciones.csv
    ├── agrupamiento.py
    ├── pruebas.py
    ├── resultados_agrupamiento.csv
```

## 5. Instalación

Instalar las bibliotecas necesarias para el componente de agrupamiento:

```bash
python -m pip install pandas scikit-learn matplotlib
```

## 6. Componente de búsqueda de rutas

Desde la carpeta principal, ejecutar:

```bash
python main.py
```

El programa solicita una estación de origen y una de destino, y muestra la ruta encontrada y su costo dentro del modelo.

## 7. Componente de aprendizaje
Entrar en la carpeta del componente:

```bash
cd agrupamiento
```

Ejecutar el modelo:

```bash
python agrupamiento.py
```

El programa carga `datos_estaciones.csv`, normaliza las variables numéricas, aplica K-Means con tres grupos y genera:

- `grafica_agrupamiento.png`
- `resultados_agrupamiento.csv`

### Variables utilizadas

- `pasajeros_promedio`: valor de pasajeros.
- `numero_conexiones`: cantidad de conexiones.
- `espera_minutos`: tiempo de espera.

El nombre de la estación sirve para identificar cada registro; el modelo agrupa usando las tres variables numéricas.

## 8. Pruebas

### Búsqueda de rutas

Desde la carpeta principal:

```bash
python pruebas.py
```

### Agrupamiento

Desde la carpeta `agrupamiento`:

```bash
python pruebas.py
```

Las pruebas del agrupamiento comprueban la carga de los datos, las columnas requeridas, la ausencia de valores vacíos y la generación de tres grupos.


## 9. Evidencias y entregables

- Dataset: `agrupamiento/datos_estaciones.csv`
- Código del modelo: `agrupamiento/agrupamiento.py`
- Evidencias de ejecución: `agrupamiento/evidencias/`

## 10. Repositorio

Repositorio GitHub: https://github.com/JuSoGi/TransIA