import numpy as np
import matplotlib.pyplot as plt


class Imagen:
    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            raise TypeError("data debe ser un np.ndarray")

        self.data = data

    def visualizar(self):
        plt.imshow(self.data, cmap="gray")
        plt.title("Imagen")
        plt.axis("off")
        plt.show()

    def __str__(self):
        return f"Imagen de forma {self.data.shape}"

    def __len__(self):
        return self.data.size

    def __getitem__(self, idx):
        return self.data[idx]