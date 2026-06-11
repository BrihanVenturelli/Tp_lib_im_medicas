
import numpy as np

from bioimagenes.core.imagen import Imagen
from bioimagenes.filtros.filtro import Filtro


def test_crear_imagen():
    data = np.ones((10, 10))

    img = Imagen(data)

    assert img.data.shape == (10, 10)
    assert img.info["dimensiones"] == (10, 10)


def test_len_imagen():
    data = np.ones((10, 10))

    img = Imagen(data)

    assert len(img) == 100


def test_getitem_imagen():
    data = np.ones((10, 10))

    img = Imagen(data)

    assert img[0, 0] == 1


def test_aplicar_filtro():
    data = np.random.randint(0, 255, (10, 10))

    img = Imagen(data)

    kernel = np.ones((3, 3)) / 9
    filtro = Filtro("Promedio", kernel)

    img.aplicar_filtro(filtro)

    assert img.data.shape == (10, 10)
    assert len(img.info.historial) == 1
    assert img.info.historial.ultimo_cambio == "Filtro aplicado: Promedio"