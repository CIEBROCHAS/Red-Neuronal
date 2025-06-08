import numpy as np

# Crea una matriz con n filas y m columnas llena de 1.0
# Implementada con arrays de numpy
def crear_matriz_pesos(n, m) -> np.ndarray:
    matriz_base = [[float(1)] * m] * n
    matriz_pesos = np.array(matriz_base, dtype=np.float32)
    return matriz_pesos

# Crear un diccionario de matrices de pesos para una red neuronal donde long_inp es la cantidad de
# neuronas de la capa de input, long_out de la capa de output, long_media de las capas intermedias
# u ocultas y cantidad_medias la cantidad de capas medias que habrán.
#
# La entrada (0, 1) son los pesos entre la primera capa y la segunda, la
# (cantidad_medias, cantidad_medias + 1) los pesos entre la penúltima y la última
def crear_dict_matrices(long_inp, long_out, long_media, cantidad_medias) -> dict:
    if not all(isinstance(x, int) for x in [long_inp, long_out, long_media, cantidad_medias]):
        raise TypeError("Todos los parámetros deben ser enteros")
    if long_inp < 0 or long_out < 0 or long_media < 0 or cantidad_medias < 0:
        raise ValueError("No se permiten números negativos")

    dict_matrices = {}
    for i in range(cantidad_medias + 1):
        if i == 0:  # capa de la izq es la de inp
            if cantidad_medias == 0:  # capa de la der es la de out
                dict_matrices[(i, i + 1)] = crear_matriz_pesos(long_inp, long_out)
            else:  # capa de la der es una media
                dict_matrices[(i, i + 1)] = crear_matriz_pesos(long_inp, long_media)
        else:  # capa de la izq es una media
            if i < cantidad_medias:  # capa de la der es otra media
                dict_matrices[(i, i + 1)] = crear_matriz_pesos(long_media, long_media)
            else:  # capa de la der es la de out
                dict_matrices[(i, i + 1)] = crear_matriz_pesos(long_media, long_out)
    return dict_matrices