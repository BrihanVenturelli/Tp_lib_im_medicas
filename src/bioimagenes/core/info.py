class Info:
    def __init__(self, datos=None, historial=None):
        self.datos = datos if datos is not None else {}
        self.historial = historial