import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def traslacion(img, delta_x=50, delta_y=50):
    """
    La traslación mueve los píxeles de una imagen en los ejes 'x' y 'y'
    mediante un delta_x y un delta_y
    """

    m, n = img.size
    img = img.resize((int(m * 0.5), int(n * 0.5)))
    m, n = img.size
    img = img.convert('L')  # Convierte la imagen a escala de grises

    A = np.array(img)  # Conversion de imagen a array
    B = np.zeros((m, n), dtype=np.uint8)

    # Traslación

    for x in range(m):
        for y in range(n):
            x_t = x + delta_x
            y_t = y + delta_y

            if x_t < m and y_t < n:
                B[x_t][y_t] = np.uint8(A[x, y])

    # Conversion del array de salida en un imagen en
    # escala de grises.
    B = Image.fromarray(B, 'L')

    return B


def rotacion(img, theta=np.pi/4):
    """
    Rota una imagen en torno a las manecillas del reloj, considerando 
    un ángulo ingresado, thetha
    """

    img = img.convert('L')

    A = np.array(img, dtype=np.uint8)
    m, n = img.size
    B = np.zeros((m, n), dtype=np.uint8)

    # Centro de rotacion
    x_c = m // 2
    y_c = n // 2

    for x in range(m):
        for y in range(n):
            # Posición para el eje X
            a0 = np.cos(theta)
            a1 = np.sin(theta)
            a2 = x_c - a0*x_c - a1*y_c
            x_t = np.round(a0*x + a1*y + a2)

            # Posición para el eje Y
            b0 = -np.sin(theta)
            b1 = np.cos(theta)
            b2 = y_c - b0*y_c - b1*y_c
            y_t = np.round(b0*x + b1*y + b2)

            # Verifica que los pixeles no exceda la pocisión 
            # de la imagen original
            if x_t >= 0 and y_t >= 0 and x_t < m and y_t < n:
                B[np.int64(x_t), np.int64(y_t)] = np.uint8(A[x, y])

    # Imagen de salida a escala de grises
    B = Image.fromarray(B, 'L')

    return B
