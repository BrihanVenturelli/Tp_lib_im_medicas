import numpy as np
import matplotlib.pyplot as plt

from ..core.imagen import Imagen
from ..filtros.filtro import Filtro


class ImagenRadiografia(Imagen):

    def __init__(
        self,
        data: np.ndarray,
        tipo_estudio: str = "Radiografía",
        info=None
    ):

        # INICIALIZAR LA CLASE PADRE IMAGEN
        super().__init__(data=data, info=info)

        # VERIFICAR QUE SEA 2D
        if self.data.ndim != 2:
            raise ValueError("la radiografía debe ser una imagen 2D")

        self.tipo_estudio = tipo_estudio

        self.info.actualizar("tipo", "ImagenRadiografia")
        self.info.actualizar("tipo_estudio", tipo_estudio)

    def mejorar_contraste(self, factor: float = 1.5):

        # AUMENTAR CONTRASTE RESPECTO AL PROMEDIO
        media = np.mean(self.data)
        nueva = media + factor * (self.data - media)

        # LIMITAR VALORES ENTRE 0 Y 255
        self.data = np.clip(nueva, 0, 255)

        self.info.actualizar("brillo", float(np.mean(self.data)))
        self.info.historial.modificar_historial(
            f"Mejora de contraste con factor {factor}"
        )

    def invertir_intensidad(self):

        # INVERTIR ESCALA DE GRISES
        self.data = 255 - self.data

        self.info.actualizar("brillo", float(np.mean(self.data)))
        self.info.historial.modificar_historial(
            "Inversión de intensidades"
        )

    def ecualizar(self):

        # ECUALIZACION SIMPLE DEL HISTOGRAMA
        imagen = self.data.astype(np.uint8)

        hist, bins = np.histogram(
            imagen.flatten(),
            bins=256,
            range=[0, 256]
        )

        cdf = hist.cumsum()
        cdf_normalizada = 255 * cdf / cdf[-1]

        self.data = np.interp(
            imagen.flatten(),
            bins[:-1],
            cdf_normalizada
        ).reshape(imagen.shape)

        self.info.actualizar("brillo", float(np.mean(self.data)))
        self.info.historial.modificar_historial(
            "Ecualización de histograma"
        )

    def detectar_bordes(self):

        # KERNEL SOBEL SIMPLE
        kernel_sobel = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])

        filtro = Filtro(tipo="Sobel", kernel=kernel_sobel)

        self.aplicar_filtro(filtro)

        self.info.historial.modificar_historial(
            "Detección de bordes en radiografía"
        )

    def seleccionar_roi(self, x_inicio, x_fin, y_inicio, y_fin):

        # RECORTAR REGION DE INTERES
        roi = self.data[x_inicio:x_fin, y_inicio:y_fin]

        nueva = ImagenRadiografia(
            data=roi,
            tipo_estudio=self.tipo_estudio
        )

        nueva.info.actualizar("cortada", True)
        nueva.info.historial.modificar_historial(
            "Región de interés seleccionada"
        )

        return nueva

    def visualizar_cluster(self, datos_2d, etiquetas=None):

        # GRAFICAR PUNTOS DE CLUSTER EN 2D
        datos_2d = np.array(datos_2d)

        if datos_2d.ndim != 2 or datos_2d.shape[1] != 2:
            raise ValueError("datos_2d debe tener forma (n, 2)")

        plt.scatter(datos_2d[:, 0], datos_2d[:, 1], c=etiquetas)
        plt.title("Clusters de radiografías")
        plt.xlabel("Característica 1")
        plt.ylabel("Característica 2")
        plt.show()