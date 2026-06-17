import numpy as np
import matplotlib.pyplot as plt

from ..core.imagen import Imagen


class ImagenTomografia(Imagen):

    def __init__(
        self,
        data: np.ndarray,
        voxel_size: tuple = (1.0, 1.0, 1.0),
        unidad: str = "HU",
        info=None
    ):

        # INICIALIZAR LA CLASE PADRE IMAGEN
        super().__init__(data=data, info=info)

        # VERIFICAR QUE SEA VOLUMEN 3D
        if self.data.ndim != 3:
            raise ValueError("la tomografía debe ser una imagen 3D")

        self.voxel_size = voxel_size
        self.unidad = unidad

        self.info.actualizar("tipo", "ImagenTomografia")
        self.info.actualizar("voxel_size", voxel_size)
        self.info.actualizar("unidad", unidad)

    def obtener_slice(self, indice: int):

        # VERIFICAR INDICE DEL CORTE
        if indice < 0 or indice >= self.data.shape[0]:
            raise IndexError("índice de slice fuera de rango")

        return self.data[indice]

    def mostrar_slice(self, indice: int):

        # OBTENER CORTE ESPECIFICO
        corte = self.obtener_slice(indice)

        # MOSTRAR CORTE EN ESCALA DE GRISES
        plt.imshow(corte, cmap="gray")
        plt.title(f"Slice {indice}")
        plt.axis("off")
        plt.show()

        self.info.historial.modificar_historial(
            f"Visualización del slice {indice}"
        )

    def normalizar_intensidades(self):

        minimo = np.min(self.data)
        maximo = np.max(self.data)

        if maximo == minimo:
            raise ValueError("no se puede normalizar un volumen constante")

        self.data = (self.data - minimo) / (maximo - minimo)

        self.info.actualizar("brillo", float(np.mean(self.data)))
        self.info.historial.modificar_historial(
            "Normalización de intensidades tomográficas"
        )

    def aplicar_ventana(self, centro: float, ancho: float):

        if ancho <= 0:
            raise ValueError("el ancho de ventana debe ser mayor a cero")

        minimo = centro - ancho / 2
        maximo = centro + ancho / 2

        ventana = np.clip(self.data, minimo, maximo)
        ventana = (ventana - minimo) / (maximo - minimo)

        self.info.historial.modificar_historial(
            f"Ventana aplicada: centro={centro}, ancho={ancho}"
        )

        return ventana

    def ventana_tejido(self, tejido: str):

        tejido = tejido.lower()

        ventanas = {
            "pulmon": (-600, 1500),
            "hueso": (400, 1800),
            "cerebro": (40, 80),
            "tejido_blando": (50, 400)
        }

        if tejido not in ventanas:
            raise ValueError(
                "tejido no válido. Opciones: pulmon, hueso, cerebro, tejido_blando"
            )

        centro, ancho = ventanas[tejido]

        return self.aplicar_ventana(centro, ancho)

    def visualizar_corte(self, indice: int):

        # OBTENER CORTE
        corte = self.obtener_slice(indice)

        # CREAR IMAGEN RGB VACIA
        rgb = np.zeros((corte.shape[0], corte.shape[1], 3), dtype=np.uint8)

        # CLASIFICAR TEJIDOS SEGUN VALORES HU APROXIMADOS
        aire = corte < -500
        tejido_blando = (corte >= -500) & (corte < 300)
        hueso = corte >= 300

        # ASIGNAR COLORES
        rgb[aire] = [0, 0, 255]
        rgb[tejido_blando] = [255, 100, 100]
        rgb[hueso] = [255, 255, 255]

        plt.imshow(rgb)
        plt.title(f"Corte coloreado {indice}")
        plt.axis("off")
        plt.show()

        self.info.historial.modificar_historial(
            f"Visualización coloreada del corte {indice}"
        )

        return rgb

    def representar_3d(self):

        # REPRESENTACION SIMPLE DEL VOLUMEN
        print(f"Volumen 3D con dimensiones: {self.data.shape}")
        print(f"Tamaño de voxel: {self.voxel_size}")
        print(f"Unidad de intensidad: {self.unidad}")

        self.info.historial.modificar_historial(
            "Representación 3D simplificada"
        )