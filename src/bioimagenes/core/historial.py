class Historial:
    def __init__(self):
        self.registros = []

    def modificar_historial(self, cambio):
        self.registros.append(cambio)