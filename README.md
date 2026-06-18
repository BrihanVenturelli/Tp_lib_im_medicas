# Tp_lib_im_medicas

Trabajo Integrador de Programación Orientada a Objetos.

Librería desarrollada en Python para el procesamiento y análisis de imágenes médicas, implementando conceptos de encapsulamiento, herencia, modularización y pruebas unitarias.

---

## Objetivos

* Representar imágenes médicas mediante clases.
* Gestionar información y metadatos asociados.
* Mantener un historial de modificaciones realizadas sobre las imágenes.
* Aplicar filtros de procesamiento digital.
* Implementar clases específicas para distintos tipos de imágenes médicas:

  * Radiografía
  * Termografía
  * Tomografía
* Verificar el correcto funcionamiento mediante pruebas unitarias.

---

## Estructura de carpetas

```text
Tp_lib_im_medicas/
│
├── data/
│   ├── radiografias/
│   ├── termografias/
│   └── tomografias/
│
├── docs/
│   ├── examples/
│   │   ├── ejemplo_radiografia.py
│   │   ├── ejemplo_termografica.py
│   │   └── ejemplo_tomografia.py
│   │
│   └── uml/
│       └── uml.jpg
│
├── src/
│   └── bioimagenes/
│       ├── core/
│       │   ├── historial.py
│       │   ├── info.py
│       │   └── imagen.py
│       │
│       ├── filtros/
│       │   └── filtro.py
│       │
│       ├── medicas/
│       │   ├── imagen_termografica.py
│       │   ├── imagen_radiografia.py
│       │   └── imagen_tomografia.py
│       │
│       ├── __init__.py
│       └── __version__.py
│
├── tests/
│   ├── test_historial.py
│   ├── test_info.py
│   ├── test_imagen.py
│   ├── test_filtro.py
│   ├── test_radiografia.py
│   ├── test_termografica.py
│   └── test_tomografia.py
│
├── README.md
├── pyproject.toml
└── .gitignore
```

---

## Clases implementadas

### Historial

Permite registrar los cambios realizados sobre una imagen.

Funciones principales:

* Registrar cambios.
* Consultar el último cambio realizado.
* Obtener la cantidad de cambios registrados.
* Visualizar el historial completo.

---

### Info

Almacena metadatos asociados a una imagen.

Información almacenada:

* Dimensiones.
* Brillo promedio.
* Tipo de imagen.
* Estado de recorte.
* Parámetros específicos según el estudio.

---

### Imagen

Clase base para representar imágenes bidimensionales o tridimensionales.

Funciones principales:

* Visualización.
* Conversión a blanco y negro.
* Aplicación de filtros.
* Acceso a píxeles.
* Gestión de metadatos.
* Gestión de historial.

---

### Filtro

Representa filtros basados en kernels y permite realizar convoluciones.

Funciones principales:

* Validación de kernels.
* Aplicación de convoluciones.
* Procesamiento mediante filtros personalizados.

---

### ImagenRadiografia

Clase especializada para radiografías.

Funciones implementadas:

* Mejora de contraste.
* Inversión de intensidades.
* Ecualización de histograma.
* Detección de bordes.
* Selección de regiones de interés (ROI).
* Visualización de clusters.

---

### ImagenTermografica

Clase especializada para imágenes térmicas.

Funciones implementadas:

* Conversión de intensidad a temperatura.
* Generación de mapas de calor.
* Detección de puntos calientes.
* Segmentación por umbral.
* Normalización de imágenes.

---

### ImagenTomografia

Clase especializada para tomografías tridimensionales.

Funciones implementadas:

* Obtención de slices.
* Visualización de cortes.
* Normalización de intensidades.
* Aplicación de ventanas.
* Ventanas específicas por tejido.
* Visualización coloreada de tejidos.
* Representación simplificada de volúmenes 3D.

---

## Instalación

Instalar el proyecto en modo editable:

```bash
pip install -e .
```

---

## Dependencias

El proyecto utiliza las siguientes librerías:

* numpy
* matplotlib
* pytest
* opencv-python
* nibabel

Instalación manual de dependencias:

```bash
pip install numpy matplotlib pytest opencv-python nibabel
```

O bien instalar el proyecto completo en modo editable:

```bash
pip install -e .
```

---

## Ejecución de pruebas

Ejecutar todos los tests unitarios:

```bash
pytest
```

Ejecutar una prueba específica:

```bash
pytest tests/test_tomografia.py
```

---

## Ejemplos de uso con imágenes reales

Durante el desarrollo se validó la librería utilizando imágenes médicas reales proporcionadas por la cátedra y almacenadas en la carpeta `data`.

### Radiografía

Ejecutar:

```bash
python docs/examples/ejemplo_radiografia.py
```

Permite:

* Cargar una radiografía real.
* Mejorar contraste.
* Ecualizar histograma.
* Detectar bordes.
* Seleccionar regiones de interés (ROI).
* Consultar historial de cambios.

---

### Termografía

Ejecutar:

```bash
python docs/examples/ejemplo_termografica.py
```

Permite:

* Cargar una termografía real.
* Generar mapas de calor.
* Detectar puntos calientes.
* Segmentar regiones según temperatura.
* Normalizar intensidades.
* Consultar historial de procesamiento.

---

### Tomografía

Ejecutar:

```bash
python docs/examples/ejemplo_tomografia.py
```

Permite:

* Cargar un volumen médico real en formato NIfTI (.nii).
* Obtener cortes (slices) del volumen.
* Visualizar cortes tomográficos.
* Aplicar ventanas de visualización.
* Visualizar tejidos mediante colores.
* Representar información del volumen 3D.
* Consultar historial de procesamiento.

---

## Resultados de validación

La librería fue validada mediante:

* Pruebas unitarias automatizadas.
* Imágenes sintéticas generadas con NumPy.
* Radiografías reales (.png).
* Termografías reales (.jpg).
* Tomografías reales (.nii).

Resultados obtenidos:


✔ Validación funcional con imágenes médicas reales proporcionadas por la cátedra.

✔ Procesamiento exitoso de radiografías, termografías y tomografías.

---

## Diagrama UML

El diagrama UML del proyecto se encuentra en:

```text
docs/uml/uml.jpg
```

---

## Autor

Brihan Venturelli

Ingeniería Biomédica

