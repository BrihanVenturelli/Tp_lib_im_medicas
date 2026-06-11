import numpy as np

from bioimagenes.core.imagen import Imagen
from bioimagenes.filtros.filtro import Filtro


def test_aplicar_filtro_promedio():
    data = np.random.randint(0, 255, (100, 100))

    img = Imagen(data)

    kernel = np.ones((3, 3)) / 9
    filtro = Filtro("Promedio", kernel)

    img.aplicar_filtro(filtro)

    assert img.data.shape == (100, 100)
    assert len(img.info.historial) == 1
    assert img.info.historial.ultimo_cambio == "Filtro aplicado: Promedio"