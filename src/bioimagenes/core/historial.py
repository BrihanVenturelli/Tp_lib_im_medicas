class Historial:

    def __init__(self, lista_cambios: list = None):
        if lista_cambios is None:
            self.lista_cambios = []
        else:
            self.lista_cambios = lista_cambios

    def modificar_historial(self, cambio):
        self.lista_cambios.append(cambio)

    @property
    def ultimo_cambio(self):
        if len(self.lista_cambios) == 0:
            return None
        return self.lista_cambios[-1]

    def ver_historial(self):
        return self.lista_cambios

    def __len__(self):
        return len(self.lista_cambios)

    def __iter__(self):
        return iter(self.lista_cambios)

    def __str__(self):
        if not self.lista_cambios:
            return "Historial vacío"

        texto = "Historial de cambios:\n"

        for i, cambio in enumerate(self.lista_cambios, 1):
            texto += f"{i}. {cambio}\n"

        texto += f"Último cambio: {self.ultimo_cambio}"

        return texto




        