from bioimagenes.core.historial import Historial


def test_crear_historial_vacio():
    historial = Historial()

    assert len(historial) == 0
    assert historial.ultimo_cambio is None


def test_modificar_historial():
    historial = Historial()

    historial.modificar_historial("Filtro aplicado")

    assert len(historial) == 1
    assert historial.ultimo_cambio == "Filtro aplicado"


def test_iterar_historial():
    historial = Historial()

    historial.modificar_historial("Cambio 1")
    historial.modificar_historial("Cambio 2")

    cambios = list(historial)

    assert cambios == ["Cambio 1", "Cambio 2"]