import numpy as np

from bioimagenes.core.imagen import Imagen
from bioimagenes.filtros.filtro import Filtro


data = np.random.randint(0, 255, (10, 10))

img = Imagen(data)

print("Imagen creada:")
print(img)

kernel = np.ones((3, 3)) / 9

filtro = Filtro(
    tipo="Promedio",
    kernel=kernel
)

print("\nFiltro:")
print(filtro)

img.aplicar_filtro(filtro)

print("\nImagen filtrada:")
print(img)

print("\nHistorial:")
print(img.info.historial)

print("\nInfo:")
print(img.info)