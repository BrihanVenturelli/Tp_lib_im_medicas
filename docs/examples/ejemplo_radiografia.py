import cv2

from bioimagenes import ImagenRadiografia


# RUTA DE LA RADIOGRAFIA REAL
ruta = "data/radiografias/216840111366964014008416513202014153161516671_01-196-149.png"

# CARGAR IMAGEN EN ESCALA DE GRISES
data = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

# VERIFICAR QUE LA IMAGEN SE CARGO BIEN
if data is None:
    raise ValueError("No se pudo cargar la radiografía. Verificar la ruta.")

# CREAR OBJETO RADIOGRAFIA
rx = ImagenRadiografia(data)

print("=== RADIOGRAFIA ORIGINAL ===")
print(rx)
rx.visualizar()

# MEJORAR CONTRASTE
rx.mejorar_contraste(factor=1.5)

print("=== RADIOGRAFIA CON CONTRASTE MEJORADO ===")
print(rx)
rx.visualizar()

# ECUALIZAR HISTOGRAMA
rx.ecualizar()

print("=== RADIOGRAFIA ECUALIZADA ===")
print(rx)
rx.visualizar()

# DETECTAR BORDES
rx.detectar_bordes()

print("=== RADIOGRAFIA CON BORDES DETECTADOS ===")
print(rx)
rx.visualizar()

# SELECCIONAR REGION DE INTERES
roi = rx.seleccionar_roi(
    100, 400,
    100, 400
)

print("=== REGION DE INTERES ===")
print(roi)
roi.visualizar()

# MOSTRAR HISTORIAL
print("=== HISTORIAL ===")
print(rx.info.historial)