
# n_pre y n_pos se refieren a las neuronas de la capa previa y posterior con las que está conectada
# c_pre y c_pos se refieren a las conexiones de la capa previa y posterior que tienen
class Neurona:
    def __init__(self, n_pre, n_pos, c_pre, c_pos):
        self.__n_pre = n_pre
        self.__n_pos = n_pos
        self.__c_pre = c_pre
        self.__c_pos = c_pos

class Conexion:
    def __init__(self, pre, pos):
        self.__pre = pre
        self.__pos = pos

