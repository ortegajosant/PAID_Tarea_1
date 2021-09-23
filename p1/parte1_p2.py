import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import filtros.mediana as filtro_mediana


def mediana(img):
    img_filtrada = filtro_mediana.mediana(img, False)

    # img_s = rt.rotacion(img)  # Rotacion de imagen
    grafico = plt.figure()

    grafico.add_subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Imagen original")

    grafico.add_subplot(1, 2, 2)
    plt.imshow(img_filtrada, cmap='gray')
    plt.title("Imagen con mediana")

    plt.show()