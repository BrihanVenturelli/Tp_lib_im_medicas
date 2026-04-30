
# Primeras pruebas de testeo de la primera clase imagen.py y Principal del proyecto

import numpy as np
from bioimagenes.core.imagen import Imagen


def test_basico():
    print("\n--- TEST BÁSICO ---")

    data = np.random.randint(0, 255, (50, 50))
    img = Imagen(data)

    print(img)
    print("Cantidad de pixeles:", len(img))
    print("Pixel [0,0]:", img[0, 0])

    img.visualizar()

    print("--- FIN ---\n")


if __name__ == "__main__":
    test_basico()


# Para pobre el primer test se debe de correr con : python tests/test_imagen.py
# Dicho testeo nos mostrara una ventana con una imagen pixelada
# cabe aclarar que como interprete de python estamos usando minconda. 