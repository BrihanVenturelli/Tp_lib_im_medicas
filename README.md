# Tp_lib_im_medicas
Trabajo Integrador : Librería para el  procesamiento y análisis  de imágenes médicas
# Estructura de carpetas
# Diagrama UML


# Tp_lib_im_medicas

Trabajo Integrador de Programación Orientada a Objetos.

Librería desarrollada en Python para el procesamiento y análisis básico de imágenes médicas, implementando conceptos de encapsulamiento, herencia, modularización y pruebas unitarias.

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

## Estructura de carpetas

```text
Tp_lib_im_medicas/
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
│
├── README.md
└── pyproject.toml
```

## Clases implementadas

### Historial

Permite registrar los cambios realizados sobre una imagen.

### Info

Almacena metadatos asociados a una imagen:

* dimensiones
* brillo
* tipo
* estado de recorte

### Imagen

Clase base para representar imágenes bidimensionales o tridimensionales.

Funciones principales:

* visualización
* conversión a blanco y negro
* aplicación de filtros
* acceso a píxeles

### Filtro

Representa filtros basados en kernels y permite realizar convoluciones.

### ImagenTermografica

Clase especializada para imágenes térmicas.

Funciones:

* conversión a temperatura
* detección de puntos calientes
* normalización
* mapa de calor

### ImagenRadiografia

Clase especializada para radiografías.

Funciones:

* mejora de contraste
* ecualización
* inversión de intensidades
* selección de regiones de interés (ROI)

### ImagenTomografia

Clase especializada para tomografías.

Funciones:

* obtención de cortes (slices)
* normalización de intensidades
* aplicación de ventanas
* visualización por tejidos

## Instalación

Instalar el proyecto en modo editable:

```bash
pip install -e .
```

## Dependencias

* numpy
* matplotlib
* pytest

## Ejecución de pruebas

Ejecutar todos los tests:

```bash
pytest
```

Ejecutar un archivo específico:

```bash
pytest tests/test_tomografia.py
```

## Diagrama UML

(Insertar aquí la imagen UML o el enlace al diagrama actualizado).

## Autor

Brihan Venturelli

Ingeniería Biomédica
