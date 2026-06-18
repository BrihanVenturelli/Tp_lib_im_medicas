import cv2
import matplotlib.pyplot as plt

from bioimagenes import ImagenTermografica


# RUTA DE LA TERMOGRAFIA REAL
ruta = "data/termografias/N11108.jpg"

# CARGAR IMAGEN EN ESCALA DE GRISES
data = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

# VERIFICAR QUE LA IMAGEN SE CARGO BIEN
if data is None:
    raise ValueError("No se pudo cargar la termografía. Verificar la ruta.")

# CREAR OBJETO TERMOGRAFICO
# Como la imagen viene en escala de grises y no trae temperatura real,
# proponemos un rango aproximado de temperatura.
term = ImagenTermografica(
    data=data,
    temp_min=30.0,
    temp_max=36.5
)

print("=== TERMOGRAFIA ORIGINAL ===")
print(term)
term.visualizar()

# CONVERTIR A MAPA DE TEMPERATURA
temp_map = term.convertir_a_temperatura()

print("=== MAPA DE TEMPERATURA ===")
print("Temperatura mínima:", temp_map.min())
print("Temperatura máxima:", temp_map.max())

# MOSTRAR MAPA DE CALOR
term.mapa_calor()

# DETECTAR PUNTOS CALIENTES
zonas_calientes = term.detectar_puntos_calientes(
    umbral=35.0
)

plt.imshow(zonas_calientes, cmap="gray")
plt.title("Zonas calientes >= 35 °C")
plt.axis("off")
plt.show()

# NORMALIZAR IMAGEN
term.normalizar()

print("=== TERMOGRAFIA NORMALIZADA ===")
print(term)
term.visualizar()

# MOSTRAR HISTORIAL
print("=== HISTORIAL ===")
print(term.info.historial)