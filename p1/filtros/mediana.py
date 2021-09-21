import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def mediana(img, black_p=False):
    """
       Aplicación del filtro de la mediana para las imágenes que se ven
       con ruido tras la aplicación de una rotación
    """
    m, n = img.size

    A = np.array(img, dtype=np.uint8)

    if black_p:
        for x in range(m):
            for y in range(n):
                if A[x, y] == np.uint8(0):
                    kernel_array = np.squeeze(np.asarray(A[x-1:x+2, y-1:y+2]))
                    A[x, y] = np.uint8(np.median(kernel_array))

    else:
        for x in range(m):
            for y in range(n):
                kernel_array = np.squeeze(np.asarray(A[x-1:x+2, y-1:y+2]))
                A[x, y] = np.uint8(np.median(kernel_array))

    # imagen de salida
    img_salida = Image.fromarray(A, 'L')

    return img_salida.convert('L')
