import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
import tools.rotacion as rotar
from filtros.mediana import mediana
from filtros.media import media


def rotacion(img, ang=np.pi/4):
    img_rotada = rotar.rotacion(img, ang)

    img_mediana = mediana(img_rotada, True)
    img_media = media(img_rotada, True)

    grafico = plt.figure()
    grafico.add_subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Imagen original")

    grafico.add_subplot(2, 2, 2)
    plt.imshow(img_rotada, cmap='gray')
    plt.title("Imagen con rotacion")

    grafico.add_subplot(2, 2, 3)
    plt.imshow(img_mediana, cmap='gray')
    plt.title("Imagen con filtro de mediana")

    grafico.add_subplot(2, 2, 4)
    plt.imshow(img_media, cmap='gray')
    plt.title("Imagen con filtro de media")

    plt.show()
