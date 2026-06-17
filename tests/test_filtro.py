import numpy as np
import pytest

from bioimagenes.filtros.filtro import Filtro


def test_crear_filtro():
    kernel = np.ones((3, 3)) / 9

    filtro = Filtro("Promedio", kernel)

    assert filtro.tipo == "Promedio"
    assert filtro.tamaño == (3, 3)


def test_kernel_invalido_no_ndarray():
    with pytest.raises(TypeError):
        Filtro("Promedio", [[1, 1], [1, 1]])


def test_tipo_invalido():
    kernel = np.ones((3, 3))

    with pytest.raises(TypeError):
        Filtro(123, kernel)


def test_kernel_dimension_par():
    kernel = np.ones((2, 2))

    with pytest.raises(ValueError):
        Filtro("Promedio", kernel)


def test_kernel_3d_invalido():
    kernel = np.ones((3, 3, 3))

    with pytest.raises(ValueError):
        Filtro("Promedio", kernel)


def test_convolucion_2d():
    kernel = np.ones((3, 3)) / 9
    filtro = Filtro("Promedio", kernel)

    imagen = np.ones((5, 5))

    resultado = filtro.convolucion(imagen)

    assert resultado.shape == imagen.shape


def test_convolucion_imagen_no_ndarray():
    kernel = np.ones((3, 3)) / 9
    filtro = Filtro("Promedio", kernel)

    with pytest.raises(TypeError):
        filtro.convolucion([[1, 2], [3, 4]])


def test_convolucion_imagen_3d_invalida():
    kernel = np.ones((3, 3)) / 9
    filtro = Filtro("Promedio", kernel)

    imagen = np.ones((5, 5, 3))

    with pytest.raises(ValueError):
        filtro.convolucion(imagen)