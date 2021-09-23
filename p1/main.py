import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
import filtros.mediana as f_mediana
import filtros.media as f_media
from parte1_p1 import media
from parte1_p2 import mediana
from parte1_p3 import rotacion


def rotar(img, grado):
    img_rotada = None
    if (grado != False and isinstance(grado, int)):
        grado = grado * np.pi/180
        rotacion(img, grado)
    else:
        rotacion(img)


def comparar(img):
    img_media = f_media.media(img, False)
    img_mediana = f_mediana.mediana(img, False)
    
    grafico = plt.figure()
    
    grafico.add_subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Imagen original")

    grafico.add_subplot(1, 3, 2)
    plt.imshow(img_media, cmap='gray')
    plt.title("Imagen con media")

    grafico.add_subplot(1, 3, 3)
    plt.imshow(img_mediana, cmap='gray')
    plt.title("Imagen con mediana")

    plt.show()


def filtrar(tipo, img):
    img_filtrada = None
    if tipo == 'mediana':
        mediana(img)
    else:
        media(img)


if __name__ == "__main__":
    """
    Se realizan las siguientes funciones:
        - Filtro de media:
            Parámetros:
            : media   : indica que se realiza el filtro de la media
            : img     : indica el path de la imagen a utilizar
            Ejemplo:
                python3 main.py media img/img.jpg t # Se aplica sólo a los negros
                python3 main.py media img/img.jpg   # Se aplica a toda la imagen

        - Filtro de la mediana   :
             Parámetros:
            : mediana : indica que se realiza el filtro de la mediana
            : img     : indica el path de la imagen a utilizar
            Ejemplo:
                python3 main.py media img/img.jpg t # Se aplica sólo a los negros
                python3 main.py media img/img.jpg   # Se aplica a toda la imagen

        - Compara   :
            Parámetros:
            : compara : compara el filtrado para una imagen aplicando el filtro
                de la media y la mediana
            : img     : indica el path de la imagen a utilizar
            Ejemplo:
                python3 main.py media img/img.jpg t # Se aplica sólo a los negros
                python3 main.py media img/img.jpg   # Se aplica a toda la imagen

        - Rotacion:
            Parámetros:
            : rotacion : rota una imagen y compara el filtrado aplicando el filtro
                de la media y la mediana
            : img     : indica el path de la imagen a utilizar
            : grados  : indica el angulo de giro a utilizar para realizar la rotación
                Si no se especifica, el giro es de 45 grados ('pi/4')
            Ejemplo:
                python3 main.py rotacion img/img.jpg 90 # Se aplica un giro de pi/2 
                python3 main.py rotacion img/img.jpg    # Se aplica un giro de pi/4
    """

    args = sys.argv

    len_args = len(args)

    if len(args) < 3 or len(args) > 4:
        print("Invalid number of arguments, must be between 2 or 3")
        exit()

    function = args[1]
    img_path = args[2]
    arg_3 = False
    if (len_args == 4):
        arg_3 = args[3]

    img = Image.open(img_path, 'r')
    if (arg_3 != False):
        try:
            arg_3 = int(arg_3)
        except:
            print('Invald cast type to int for degrees')

    if function == 'media' or function == 'mediana':
        filtrar(function, img)
    elif function == 'comparar':
        comparar(img)
    elif function == 'rotacion':
        rotar(img, arg_3)
