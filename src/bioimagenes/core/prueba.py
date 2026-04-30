
import numpy as np
import matplotlib.pyplot as plt

from bioimagenes.core.info import Info
from bioimagenes.core.historial import Historial
from bioimagenes.filtros.filtros import Filtro


class Imagen:
    """
    Clase base para el manejo y procesamiento de imágenes digitales.

    Representa una imagen como una matriz de datos y proporciona
    herramientas para su manipulación, visualización y análisis.

    Integra metadatos (Info) y trazabilidad (Historial).
    """

    def __init__(self, data: np.ndarray, info: Info = None):
        """
        Inicializa una instancia de Imagen.

        Parameters
        ----------
        data : np.ndarray
            Matriz de píxeles (2D o 3D).

        info : Info
            Metadatos de la imagen.
        """

        # 🔴 Validaciones importantes
        if not isinstance(data, np.ndarray):
            raise TypeError("data debe ser un np.ndarray")

        if data.ndim not in [2, 3]:
            raise ValueError("La imagen debe ser 2D (grises) o 3D (RGB)")

        self.data = data

        # 🔵 Info + Historial
        if info is None:
            historial = Historial()
            info_dict = {
                "dimensiones": data.shape,
                "brillo": float(np.mean(data)),
                "cortada": False
            }
            self.info = Info(datos=info_dict, historial=historial)
        else:
            self.info = info



    # =========================================================
    # MÉTODOS PRINCIPALES
    # =========================================================

    def aplicar_filtro(self, filtro: Filtro):
        if not isinstance(filtro, Filtro):
            raise TypeError("Debe ser un objeto Filtro")

        self.data = filtro.aplicar(self)

        self.info.historial.modificar_historial({
            "operacion": "filtro",
            "tipo": filtro.tipo
        })

        return self

    def bn(self):
        if self.data.ndim == 2:
            return self

        if self.data.shape[2] != 3:
            raise ValueError("La imagen no es RGB válida")

        r = self.data[:, :, 0]
        g = self.data[:, :, 1]
        b = self.data[:, :, 2]

        self.data = 0.2989 * r + 0.5870 * g + 0.1140 * b

        self.info.datos["dimensiones"] = self.data.shape
        self.info.datos["brillo"] = float(np.mean(self.data))

        self.info.historial.modificar_historial({
            "operacion": "bn"
        })

        return self

    def visualizar(self):
        plt.figure()

        if self.data.ndim == 2:
            plt.imshow(self.data, cmap="gray")
        else:
            plt.imshow(self.data.astype(np.uint8))

        plt.title("Imagen")
        plt.axis("off")
        plt.show()

    # =========================================================
    # MÉTODOS ESPECIALES
    # =========================================================

    def __str__(self):
        return (
            f"Imagen:\n"
            f"Dimensiones: {self.data.shape}\n"
            f"Tipo: {'RGB' if self.data.ndim == 3 else 'Grises'}\n"
            f"Brillo: {np.mean(self.data):.2f}"
        )

    def __len__(self):
        return self.data.size

    def __getitem__(self, idx):
        return self.data[idx]