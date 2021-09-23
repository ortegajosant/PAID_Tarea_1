import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import filtros.media as filtro_media


def media(img):
    img_filtrada = filtro_media.media(img, False)

    grafico = plt.figure()

    grafico.add_subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Imagen original")

    grafico.add_subplot(1, 2, 2)
    plt.imshow(img_filtrada, cmap='gray')
    plt.title("Imagen con media")

    plt.show()