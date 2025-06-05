
# n_pre y n_pos se refieren a las neuronas de la capa previa y posterior con las que está conectada (lista)
# c_pre y c_pos se refieren a las conexiones de la capa previa y posterior que tienen (lista)
# Esta clase debe ser instanciada sin argumentos: Neurona()
class Neurona:
    def __init__(self, n_pre=None, n_pos=None, c_pre=None, c_pos=None):
        self.__n_pre = n_pre if n_pre is not None else []
        self.__n_pos = n_pos if n_pos is not None else []
        self.__c_pre = c_pre if c_pre is not None else []
        self.__c_pos = c_pos if c_pos is not None else []
    def __str__(self):
        return "N"

class Conexion:
    def __init__(self, pre, pos):
        self.__pre = pre
        self.__pos = pos

