import numpy as np
import pytest

from bioimagenes import ImagenRadiografia


def test_crear_radiografia():
    data = np.random.randint(0, 255, (100, 100))

    img = ImagenRadiografia(data)

    assert img.data.shape == (100, 100)
    assert img.info["tipo"] == "ImagenRadiografia"


def test_mejorar_contraste():
    data = np.random.randint(0, 255, (100, 100))

    img = ImagenRadiografia(data)

    img.mejorar_contraste()

    assert img.data.shape == (100, 100)


def test_invertir_intensidad():
    data = np.ones((10, 10)) * 100

    img = ImagenRadiografia(data)

    img.invertir_intensidad()

    assert img.data[0, 0] == 155


def test_ecualizar():
    data = np.random.randint(0, 255, (100, 100))

    img = ImagenRadiografia(data)

    img.ecualizar()

    assert img.data.shape == (100, 100)


def test_roi():
    data = np.random.randint(0, 255, (100, 100))

    img = ImagenRadiografia(data)

    roi = img.seleccionar_roi(
        10, 50,
        10, 50
    )

    assert roi.data.shape == (40, 40)


def test_error_radiografia_3d():
    data = np.random.randint(
        0, 255,
        (100, 100, 3)
    )

    with pytest.raises(ValueError):
        ImagenRadiografia(data)