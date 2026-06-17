
import numpy as np
import pytest

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


def test_bn_imagen_rgb():
    data = np.ones((10, 10, 3))

    img = Imagen(data)

    img.bn()

    assert img.data.shape == (10, 10)
    assert img.info["dimensiones"] == (10, 10)
    assert img.info.historial.ultimo_cambio == "Conversión a blanco y negro"


def test_bn_error_imagen_2d():
    data = np.ones((10, 10))

    img = Imagen(data)

    with pytest.raises(ValueError):
        img.bn()


def test_aplicar_filtro():
    data = np.random.randint(0, 255, (10, 10))

    img = Imagen(data)

    kernel = np.ones((3, 3)) / 9
    filtro = Filtro("Promedio", kernel)

    img.aplicar_filtro(filtro)

    assert img.data.shape == (10, 10)
    assert len(img.info.historial) == 1
    assert img.info.historial.ultimo_cambio == "Filtro aplicado: Promedio"


def test_error_data_no_ndarray():

    with pytest.raises(TypeError):
        Imagen([[1, 2], [3, 4]])


def test_error_dimension_invalida():

    data = np.ones((5,))

    with pytest.raises(ValueError):
        Imagen(data)


def test_str_imagen():

    data = np.ones((10, 10))

    img = Imagen(data)

    texto = str(img)

    assert "Imagen" in texto
    assert "shape=(10, 10)" in texto