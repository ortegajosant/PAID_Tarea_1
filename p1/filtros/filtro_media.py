import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def filtro_media(img):
    """
       Aplicación del filtro de la mediana para las imágenes que se ven
       con ruido tras la aplicación de una rotación
    """

    # img = img.resize(50, 50)
    m, n = img.size

    A = np.array(img, dtype=np.uint8)

    mask = np.full((3, 3), 1/9)

    print(mask)

    for x in range(m):
        for y in range(n):
            if A[x, y] == np.uint8(0):
                kernel_array = np.squeeze(np.asarray(A[x-1:x+2, y-1:y+2]))

                average = np.mean(kernel_array)
                # print(new_value)
                A[x, y] = np.uint8(average)

    # imagen de salida
    img_salida = Image.fromarray(A, 'L')

    return img_salida.convert('L')
