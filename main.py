from modelos import Neurona
from modelos import Conexion

def crear_capa(n):
    capa = []
    for i in range(n):
        capa.append(Neurona())
    return capa

capa_inicial = crear_capa(10)
