import numpy as np
import matplotlib.pyplot as plt

from ..core.imagen import Imagen


class ImagenTermografica(Imagen):

    def __init__(
        self,
        data: np.ndarray,
        temp_min: float = 30.0,
        temp_max: float = 36.5,
        info=None
    ):

        # INICIALIZAR LA CLASE PADRE IMAGEN
        super().__init__(data=data, info=info)

        # VERIFICAR QUE SEA UNA IMAGEN 2D
        if self.data.ndim != 2:
            raise ValueError("la imagen termográfica debe ser 2D")

        # VERIFICAR RANGO DE TEMPERATURA
        if temp_min >= temp_max:
            raise ValueError("temp_min debe ser menor que temp_max")

        self.temp_min = temp_min
        self.temp_max = temp_max

        self.info.actualizar("tipo", "ImagenTermografica")
        self.info.actualizar("temp_min", temp_min)
        self.info.actualizar("temp_max", temp_max)

    def convertir_a_temperatura(self):

        # NORMALIZAR VALORES ENTRE 0 Y 1
        data_norm = self.data.astype(float) / np.max(self.data)

        # CONVERTIR A RANGO REAL DE TEMPERATURA
        temp_map = self.temp_min + data_norm * (self.temp_max - self.temp_min)

        self.info.historial.modificar_historial(
            "Conversión a mapa de temperatura"
        )

        return temp_map

    def mapa_calor(self):

        # OBTENER MATRIZ DE TEMPERATURA
        temp_map = self.convertir_a_temperatura()

        # MOSTRAR MAPA DE CALOR
        plt.imshow(temp_map, cmap="hot")
        plt.colorbar(label="Temperatura °C")
        plt.title("Mapa de calor termográfico")
        plt.axis("off")
        plt.show()

    def detectar_puntos_calientes(self, umbral: float):

        # CONVERTIR IMAGEN A TEMPERATURA
        temp_map = self.convertir_a_temperatura()

        # BUSCAR PIXELES MAYORES AL UMBRAL
        zonas = temp_map >= umbral

        self.info.historial.modificar_historial(
            f"Detección de puntos calientes con umbral {umbral} °C"
        )

        return zonas

    def segmentar_por_umbral(self, umbral: float):

        # CREAR MASCARA BINARIA SEGUN TEMPERATURA
        return self.detectar_puntos_calientes(umbral)

    def normalizar(self):

        minimo = np.min(self.data)
        maximo = np.max(self.data)

        if maximo == minimo:
            raise ValueError("no se puede normalizar una imagen constante")

        self.data = (self.data - minimo) / (maximo - minimo)

        self.info.actualizar("brillo", float(np.mean(self.data)))
        self.info.historial.modificar_historial(
            "Normalización de imagen termográfica"
        )