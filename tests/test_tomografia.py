import numpy as np
import pytest

from bioimagenes import ImagenTomografia


def test_crear_tomografia():
    data = np.random.randint(
        -1000,
        1000,
        (20, 100, 100)
    )

    img = ImagenTomografia(data)

    assert img.data.shape == (20, 100, 100)
    assert img.info["tipo"] == "ImagenTomografia"


def test_obtener_slice():
    data = np.random.randint(
        -1000,
        1000,
        (20, 100, 100)
    )

    img = ImagenTomografia(data)

    corte = img.obtener_slice(10)

    assert corte.shape == (100, 100)


def test_normalizar_intensidades():
    data = np.random.randint(
        -1000,
        1000,
        (20, 100, 100)
    )

    img = ImagenTomografia(data)

    img.normalizar_intensidades()

    assert np.min(img.data) >= 0
    assert np.max(img.data) <= 1


def test_aplicar_ventana():
    data = np.random.randint(
        -1000,
        1000,
        (20, 100, 100)
    )

    img = ImagenTomografia(data)

    ventana = img.aplicar_ventana(
        centro=40,
        ancho=80
    )

    assert ventana.shape == data.shape


def test_ventana_tejido():
    data = np.random.randint(
        -1000,
        1000,
        (20, 100, 100)
    )

    img = ImagenTomografia(data)

    ventana = img.ventana_tejido("hueso")

    assert ventana.shape == data.shape


def test_error_slice_fuera_de_rango():
    data = np.random.randint(
        -1000,
        1000,
        (20, 100, 100)
    )

    img = ImagenTomografia(data)

    with pytest.raises(IndexError):
        img.obtener_slice(100)


def test_error_tomografia_no_3d():
    data = np.random.randint(
        0,
        255,
        (100, 100)
    )

    with pytest.raises(ValueError):
        ImagenTomografia(data)


def test_error_tejido_invalido():
    data = np.random.randint(
        -1000,
        1000,
        (20, 100, 100)
    )

    img = ImagenTomografia(data)

    with pytest.raises(ValueError):
        img.ventana_tejido("piel")