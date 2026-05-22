class Historial:

    def __init__(
        self,
        lista_cambios: list = None # Si no se manda algo, el valor por defecto sera: None!
        # Osea lo define como un parametro opcional
    ):

        if lista_cambios is None:
            self.lista_cambios = [] # Crea una lista del hsitorial en el caso de no existir

        else: # Cubre el caso de que ya exista un historial!
            self.lista_cambios = lista_cambios


    # metodo para modificar la lista previamente creada
    def modificar_historial(self, cambio):
        self.lista_cambios.append(cambio)
    # Metodo para agregar un unico elemento nuevo a la clase!   
    @property
    def ultimo_cambio(self):
        if len(self.lista_cambios) == 0:
            return None
        return self.lista_cambios[-1]
    # METODO PARA SABER CUANTOS ELEMENTOS CONTIENE EL HSITORIAL
    def __len__(self):
        return len(self.lista_cambios)

    # METODO PARA VER EL HISTORIAL COMPLETO:
    def ver_historial(self):
        return self.lista_cambios
    
    # METODO STR PARA VER SI HAY O NO DATOS
    # SI HAY DATOS ENUMERARLOS, ORDENARLOS Y MOSTRAR EL ULTIMO
    def __str__(self):
        if not self.lista_cambios:
            return "Historial vacío"

        texto = "Historial de cambios:\n"

        for i, cambio in enumerate(self.lista_cambios, 1):
            texto += f"{i}. {cambio}\n"

        texto += f"Último cambio: {self.ultimo_cambio}"

        return texto




        