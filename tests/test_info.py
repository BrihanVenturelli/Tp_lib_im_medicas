import pytest

from bioimagenes.core.info import Info
from bioimagenes.core.historial import Historial


def test_crear_info_por_defecto():
    info = Info()

    assert "dimensiones" in info
    assert "brillo" in info
    assert "cortada" in info
    assert isinstance(info.historial, Historial)


def test_acceder_a_dato():
    info = Info(datos={"brillo": 120})

    assert info["brillo"] == 120


def test_get_info():
    info = Info(datos={"tipo": "Imagen"})

    assert info.get("tipo") == "Imagen"
    assert info.get("no_existe", "default") == "default"


def test_actualizar_info():
    info = Info()

    info.actualizar("tipo", "Imagen")

    assert info["tipo"] == "Imagen"


def test_error_datos_no_diccionario():

    with pytest.raises(TypeError):
        Info(datos="no soy diccionario")


def test_error_historial_no_valido():

    with pytest.raises(TypeError):
        Info(historial="no soy historial")