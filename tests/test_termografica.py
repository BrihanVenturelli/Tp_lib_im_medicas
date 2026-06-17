import numpy as np
import pytest

from bioimagenes import ImagenTermografica


def test_crear_imagen_termografica():
    data = np.random.randint(0, 255, (100, 100))

    img = ImagenTermografica(data, temp_min=30, temp_max=36.5)

    assert img.data.shape == (100, 100)
    assert img.temp_min == 30
    assert img.temp_max == 36.5
    assert img.info["tipo"] == "ImagenTermografica"


def test_convertir_a_temperatura():
    data = np.random.randint(1, 255, (100, 100))

    img = ImagenTermografica(data, temp_min=30, temp_max=36.5)

    temp = img.convertir_a_temperatura()

    assert temp.shape == data.shape
    assert np.min(temp) >= 30
    assert np.max(temp) <= 36.5


def test_detectar_puntos_calientes():
    data = np.random.randint(1, 255, (100, 100))

    img = ImagenTermografica(data, temp_min=30, temp_max=36.5)

    zonas = img.detectar_puntos_calientes(35)

    assert zonas.shape == data.shape
    assert zonas.dtype == bool


def test_normalizar_termografica():
    data = np.random.randint(1, 255, (100, 100))

    img = ImagenTermografica(data)

    img.normalizar()

    assert np.min(img.data) >= 0
    assert np.max(img.data) <= 1


def test_error_imagen_termografica_3d():
    data = np.random.randint(0, 255, (100, 100, 3))

    with pytest.raises(ValueError):
        ImagenTermografica(data)


def test_error_rango_temperatura_invalido():
    data = np.random.randint(0, 255, (100, 100))

    with pytest.raises(ValueError):
        ImagenTermografica(data, temp_min=40, temp_max=30)