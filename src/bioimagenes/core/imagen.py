import numpy as np
import matplotlib.pyplot as plt

from .info import Info


class Imagen:

    def __init__(self, data: np.ndarray, info: Info = None):

        # VERIFICAR QUE DATA SEA UN ARRAY DE NUMPY
        if not isinstance(data, np.ndarray):
            raise TypeError("data debe ser un np.ndarray")

        # VERIFICAR QUE SEA UNA IMAGEN 2D O 3D
        if data.ndim not in [2, 3]:
            raise ValueError("la imagen debe ser 2D o 3D")

        # VERIFICAR QUE INFO SEA UN OBJETO INFO
        if info is not None:
            if not isinstance(info, Info):
                raise TypeError("info debe ser un objeto Info")

        # CREAR INFO SI NO SE RECIBE
        if info is None:
            info = Info()

        self.data = data
        self.info = info

        # ACTUALIZAR METADATOS BASICOS DE LA IMAGEN
        self.info.actualizar("dimensiones", self.data.shape)
        self.info.actualizar("brillo", float(np.mean(self.data)))
        self.info.actualizar("tipo", "Imagen")

        if "cortada" not in self.info:
            self.info.actualizar("cortada", False)

    def visualizar(self):

        # VISUALIZAR IMAGEN EN ESCALA DE GRISES
        if self.data.ndim == 2:
            plt.imshow(self.data, cmap="gray")

        # VISUALIZAR IMAGEN RGB
        else:
            plt.imshow(self.data.astype(np.uint8))

        plt.title("Imagen")
        plt.axis("off")
        plt.show()

    def bn(self):

        # SI NO ES RGB, NO SE PUEDE CONVERTIR
        if self.data.ndim != 3:
            raise ValueError("la imagen ya está en escala de grises")

        # PROMEDIAR LOS 3 CANALES RGB
        self.data = np.mean(self.data, axis=2)

        # ACTUALIZAR METADATOS
        self.info.actualizar("dimensiones", self.data.shape)
        self.info.actualizar("brillo", float(np.mean(self.data)))

        # REGISTRAR CAMBIO EN HISTORIAL
        self.info.historial.modificar_historial(
            "Conversión a blanco y negro"
        )

    def aplicar_filtro(self, filtro):

        # APLICAR FILTRO A LA IMAGEN
        self.data = filtro.aplicar(self)

        # ACTUALIZAR METADATOS
        self.info.actualizar("dimensiones", self.data.shape)
        self.info.actualizar("brillo", float(np.mean(self.data)))

        # REGISTRAR CAMBIO EN HISTORIAL
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

        # DEVUELVE CANTIDAD TOTAL DE PIXELES
        return self.data.size

    def __getitem__(self, idx):

        # PERMITE ACCEDER A PIXELES USANDO img[x, y]
        return self.data[idx]