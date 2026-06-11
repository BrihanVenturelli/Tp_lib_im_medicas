from .historial import Historial


class Info:

    def __init__(self, datos: dict = None, historial: Historial = None):

        if datos is not None:
            if not isinstance(datos, dict):
                raise TypeError("datos debe ser un diccionario")

        if historial is not None:
            if not isinstance(historial, Historial):
                raise TypeError("historial debe ser un objeto Historial")

        if datos is None:
            datos = {}

        if "dimensiones" not in datos:
            datos["dimensiones"] = None

        if "brillo" not in datos:
            datos["brillo"] = None

        if "cortada" not in datos:
            datos["cortada"] = False

        if historial is None:
            historial = Historial()

        self.datos = datos
        self.historial = historial

    def __getitem__(self, clave):
        return self.datos[clave]

    def __contains__(self, clave):
        return clave in self.datos

    def get(self, clave, valor_por_defecto=None):
        return self.datos.get(clave, valor_por_defecto)

    def __str__(self):
        return (
            f"Info(datos={self.datos}, "
            f"cambios={len(self.historial)})"
        )