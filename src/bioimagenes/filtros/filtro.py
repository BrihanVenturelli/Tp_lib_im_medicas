import numpy as np


class Filtro:

    def __init__(self, tipo: str, kernel: np.ndarray):

        if not isinstance(tipo, str):
            raise TypeError("tipo debe ser un string")

        if not isinstance(kernel, np.ndarray):
            raise TypeError("kernel debe ser un np.ndarray")

        if kernel.ndim != 2:
            raise ValueError("kernel debe ser bidimensional")

        if kernel.shape[0] % 2 == 0 or kernel.shape[1] % 2 == 0:
            raise ValueError("el kernel debe tener dimensiones impares")

        self.tipo = tipo
        self.kernel = kernel
        self.tamaño = kernel.shape

    def convolucion(self, imagen: np.ndarray):

        if not isinstance(imagen, np.ndarray):
            raise TypeError("imagen debe ser un np.ndarray")

        if imagen.ndim != 2:
            raise ValueError("la convolución actual solo acepta imágenes 2D")

        filas_imagen, columnas_imagen = imagen.shape
        filas_kernel, columnas_kernel = self.kernel.shape

        resultado = np.zeros_like(imagen, dtype=float)

        centro_fila = filas_kernel // 2
        centro_columna = columnas_kernel // 2

        for i in range(centro_fila, filas_imagen - centro_fila):
            for j in range(centro_columna, columnas_imagen - centro_columna):

                region = imagen[
                    i - centro_fila:i + centro_fila + 1,
                    j - centro_columna:j + centro_columna + 1
                ]

                resultado[i, j] = np.sum(region * self.kernel)

        return resultado

    def aplicar(self, imagen):
        return self.convolucion(imagen.data)

    def __str__(self):
        return (
            f"Filtro: {self.tipo} | "
            f"Tamaño del kernel: {self.tamaño}"
        )