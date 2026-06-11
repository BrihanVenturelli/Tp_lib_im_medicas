import numpy as np
import matplotlib.pyplot as plt

from .info import Info


class Imagen:

    def __init__(self, data: np.ndarray, info: Info = None):

        if not isinstance(data, np.ndarray):
            raise TypeError("data debe ser un np.ndarray")

        if data.ndim not in [2, 3]:
            raise ValueError("la imagen debe ser 2D o 3D")

        if info is not None:
            if not isinstance(info, Info):
                raise TypeError("info debe ser un objeto Info")

        if info is None:
            info = Info(
                datos={
                    "dimensiones": data.shape,
                    "brillo": float(np.mean(data)),
                    "tipo": "Imagen",
                    "cortada": False
                }
            )

        self.data = data
        self.info = info

    def visualizar(self):
        if self.data.ndim == 2:
            plt.imshow(self.data, cmap="gray")
        else:
            plt.imshow(self.data.astype(np.uint8))

        plt.title("Imagen")
        plt.axis("off")
        plt.show()

    def bn(self):
        if self.data.ndim != 3:
            raise ValueError("la imagen ya está en escala de grises")

        self.data = np.mean(self.data, axis=2)

        self.info.datos["dimensiones"] = self.data.shape
        self.info.datos["brillo"] = float(np.mean(self.data))

        self.info.historial.modificar_historial(
            "Conversión a blanco y negro"
        )

    def aplicar_filtro(self, filtro):
        self.data = filtro.aplicar(self)

        self.info.datos["dimensiones"] = self.data.shape
        self.info.datos["brillo"] = float(np.mean(self.data))

        self.info.historial.modificar_historial(
            f"Filtro aplicado: {filtro.tipo}"
        )

    def __str__(self):
        return (
            f"Imagen("
            f"shape={self.data.shape}, "
            f"brillo={self.info.datos['brillo']:.2f}, "
            f"cambios={len(self.info.historial)}"
            f")"
        )

    def __len__(self):
        return self.data.size

    def __getitem__(self, idx):
        return self.data[idx]