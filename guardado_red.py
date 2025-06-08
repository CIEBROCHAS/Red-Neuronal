import numpy as np

# Guarda el diccionario de pesos al archivo en 'ruta', ejemplo: pesos.npz
# ADVERTENCIA, lo que sea que se guarde sobreescribe lo que ya había ahí
def guardar_pesos(dict_pesos, ruta) -> None:
    dict_pesos_str = {str(k): v for k, v in dict_pesos.items()}  # Las llaves tienen que ser str
    np.savez_compressed(ruta, **dict_pesos_str)

# Retorna un dict que contiene las matrices de pesos del archivo en 'ruta', ej: pesos.npz
def cargar_pesos(ruta) -> dict:
    np_data = np.load(ruta)
    dict_pesos = {eval(k): np_data[k] for k in np_data}
    return dict_pesos