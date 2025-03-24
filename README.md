# Sistema Inteligente de Rutas 🚆

Este proyecto implementa un **sistema basado en reglas** utilizando la librería `experta` en Python. Permite encontrar la mejor ruta entre dos estaciones en un sistema de transporte masivo, optimizando el tiempo o el costo del viaje según la preferencia del usuario.

## 📌 Características
- Utiliza un **motor de inferencia** basado en reglas para explorar rutas.
- Optimiza la ruta según el **menor tiempo de viaje** o el **menor costo**.
- Expande rutas dinámicamente hasta encontrar la mejor opción.
- Muestra la mejor ruta encontrada en la terminal.

## 📂 Estructura del Código

- **Ruta**: Representa una conexión entre estaciones con tiempo y costo.
- **Exploracion**: Almacena estaciones exploradas con tiempo y costo acumulado.
- **DestinoUsuario**: Define el destino final.
- **MejorRuta**: Guarda la mejor ruta encontrada.
- **SistemaRutas**: Motor de reglas que procesa la información y encuentra la mejor opción.

## 📦 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Sherna0303/ReglasLogicas.git
   cd sistema_rutas
   ```

2. **Instalar dependencias**
   ```bash
   pip install experta
   ```

## 🚀 Uso

1. Ejecuta el script:
   ```bash
   python sistema_rutas.py
   ```
2. Ingresa los datos cuando se soliciten en la terminal:
   ```
   Ingrese la estación de origen: A
   Ingrese la estación de destino: F
   Desea considerar el costo de transporte (y/n): Y
   ```
3. El sistema mostrará la mejor ruta:
   ```
   ✅ Mejor ruta encontrada: A → C → F con tiempo 22 min. y precio 4000 COP.
   ```

## 📖 Ejemplo de Rutas Definidas

El sistema tiene un conjunto de rutas predefinidas:
```python
rutas = [
    ("A", "B", 5, 5000),
    ("A", "C", 10, 2000),
    ("B", "D", 7, 3000),
    ("B", "E", 3, 7000),
    ("C", "F", 12, 2000),
    ("E", "F", 4, 5000),
    ("D", "F", 6, 7000),
]
```

## 🛠 Personalización
Puedes agregar más rutas editando la lista `rutas` en `sistema_rutas.py`.

