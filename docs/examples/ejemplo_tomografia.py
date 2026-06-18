import nibabel as nib
import numpy as np

from bioimagenes import ImagenTomografia


# RUTA DEL ARCHIVO DE TOMOGRAFIA REAL
ruta = "data/tomografias/AC421363f.nii"

# CARGAR ARCHIVO NIFTI
archivo = nib.load(ruta)

# OBTENER DATOS COMO ARRAY DE NUMPY
data = archivo.get_fdata()

# REORDENAR EJES PARA QUE QUEDE COMO:
# (cantidad_de_cortes, filas, columnas)
data = np.moveaxis(data, -1, 0)

# CREAR OBJETO TOMOGRAFIA
ct = ImagenTomografia(data)

print("=== TOMOGRAFIA REAL ===")
print(ct)

# MOSTRAR DIMENSIONES DEL VOLUMEN
print("Dimensiones del volumen:", ct.data.shape)

# ELEGIR UN CORTE CENTRAL
indice = ct.data.shape[0] // 2

# MOSTRAR CORTE EN ESCALA DE GRISES
ct.mostrar_slice(indice)

# APLICAR VENTANA DE TEJIDO
ventana_hueso = ct.ventana_tejido("hueso")
print("Ventana hueso:", ventana_hueso.shape)

# VISUALIZAR CORTE COLOREADO SEGUN TEJIDOS
ct.visualizar_corte(indice)

# NORMALIZAR INTENSIDADES
ct.normalizar_intensidades()

print("=== TOMOGRAFIA NORMALIZADA ===")
print(ct)

# REPRESENTACION 3D SIMPLIFICADA
ct.representar_3d()

# MOSTRAR HISTORIAL
print("=== HISTORIAL ===")
print(ct.info.historial)