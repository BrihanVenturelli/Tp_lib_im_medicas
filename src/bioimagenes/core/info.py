from .historial import Historial


class Info:

    def __init__(
        self,
        datos: dict = None,
        historial: Historial = None
    ):

        # VERIFICAR QUE DATOS SEA UN DICCIONARIO
        if datos is not None:
            if not isinstance(datos, dict):
                raise TypeError("datos debe ser un diccionario")

        # VERIFICAR QUE HISTORIAL SEA UN OBJETO HISTORIAL
        if historial is not None:
            if not isinstance(historial, Historial):
                raise TypeError(
                    "historial debe ser un objeto Historial"
                )

        # CREAR DICCIONARIO VACIO SI NO SE RECIBEN DATOS
        if datos is None:
            datos = {}

        # AGREGAR CLAVES POR DEFECTO
        if "dimensiones" not in datos:
            datos["dimensiones"] = None

        if "brillo" not in datos:
            datos["brillo"] = None

        if "cortada" not in datos:
            datos["cortada"] = False

        # CREAR HISTORIAL VACIO SI NO EXISTE
        if historial is None:
            historial = Historial()

        self.datos = datos
        self.historial = historial

    # ACCEDER A LOS DATOS COMO SI FUERA UN DICCIONARIO
    def __getitem__(self, clave):
        return self.datos[clave]

    # VERIFICAR SI EXISTE UNA CLAVE
    def __contains__(self, clave):
        return clave in self.datos

    # OBTENER UN VALOR CON OPCION POR DEFECTO
    def get(self, clave, valor_por_defecto=None):
        return self.datos.get(clave, valor_por_defecto)

    # MODIFICAR O AGREGAR UN DATO
    def actualizar(self, clave, valor):
        self.datos[clave] = valor

    # MOSTRAR RESUMEN DE LOS METADATOS
    def __str__(self):
        return (
            f"Info(datos={self.datos}, "
            f"cambios={len(self.historial)})"
        )