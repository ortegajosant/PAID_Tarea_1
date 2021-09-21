import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
import tools.tras_rota as rt
import filtros.filtro_mediana as mediana
import filtros.filtro_media as media

if __name__ == "__main__":
    """
    Realiza una traslación o una rotación dependiendo de la entrada
    Entradas:
        - traslacion
        - rotacion
    """
    args = sys.argv
    img = Image.open('img/imagen1.jpg', 'r')
    img_s = rt.rotacion(img)  # Rotacion de imagen
    img_s_f = media.filtro_media(img_s)
    img_m = mediana.filtro_mediana(img_s)
    grafico = plt.figure()
    grafico.add_subplot(1, 3, 1)
    plt.imshow(img_s, cmap='gray')
    plt.title("Imagen original")

    grafico.add_subplot(1, 3, 2)
    plt.imshow(img_s_f, cmap='gray')
    plt.title("Imagen con traslacion")

    grafico.add_subplot(1, 3, 3)
    plt.imshow(img_m, cmap='gray')
    plt.title("Imagen con traslacion")

    plt.show()
