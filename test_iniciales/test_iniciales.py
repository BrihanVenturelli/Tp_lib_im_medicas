from bioimagenes.core import Historial # Importa la clase historial de /core/bioimagenes

# # hist = Historial() # Creamos un objeto de tipo historial

# # print("Lista de cambios:") # Imprimimos un texto  de Prueba para lista de cambios
# # print(hist.lista_cambios) # Imprimimos el atributo lista_cambios de el objeto hist creado!


# # TEST 1 - agregar cambios
# historial = Historial()

# historial.modificar_historial("aplicó filtro blur")
# historial.modificar_historial("cambió brillo")

# print(historial.lista_cambios)


# # TEST 2 - ultimo cambio
# h = Historial()

# h.modificar_historial("A")
# h.modificar_historial("B")

# print(h.ultimo_cambio)


# # TEST 3 - len
# h = Historial()

# h.modificar_historial("A")
# h.modificar_historial("B")
# h.modificar_historial("C")

# print(len(h))

# # TEST 4 PARA VER EL HISTORIAL COMPLETO

# h = Historial()

# h.modificar_historial("A")
# h.modificar_historial("B")
# h.modificar_historial("C")

# print(h.ver_historial())

# # TEST 5 : ME DEBERIA DE GENERAR UNA RUTA

# print(h)

# TEST 6

# TEST 6 - __str__
h = Historial()
h.modificar_historial("A")
h.modificar_historial("B")

print(h)