import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def media(img, black_p=False):
    """
       Aplicación del filtro de la media para las imágenes
       Parametros:
       : img : Imagen
       : black_p : Indica si sólo se deben considerar pixeles negros
    """

    m, n = img.size

    A = np.array(img, dtype=np.uint8)

    # Se verifica si es para todos, o solo para los negros
    if black_p:
        for x in range(m):
            for y in range(n):
                if A[x, y] == np.uint8(0):
                    # Se obtiene la matriz de 3x3 que rodea el punto
                    kernel_array = np.squeeze(np.asarray(A[x-1:x+2, y-1:y+2]))
                    # Se calcula la media
                    average = np.mean(kernel_array)
                    #Se agrega en filtrado para el píxel específico
                    A[x, y] = np.uint8(average)

    else:
        for x in range(m):
            for y in range(n):
                # Se obtiene la matriz de 3x3 que rodea el punto
                kernel_array = np.squeeze(np.asarray(A[x-1:x+2, y-1:y+2]))
                # Se calcula la media
                average = np.mean(kernel_array)
                #Se agrega en filtrado para el píxel específico
                A[x, y] = np.uint8(average)

    # imagen de salida
    img_salida = Image.fromarray(A, 'L')

    return img_salida.convert('L')
