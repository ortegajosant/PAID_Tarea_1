import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
from tools.rotacion import rotacion
from filtros.mediana import mediana
from filtros.media import media


def rotar(img, grado):
    img_s = None
    if (grado != False and isinstance(grado, int)):
        grado = grado * np.pi/180
        img_rotada = rotacion(img, grado)
    else:
        img_rotada = rotacion(img)

    img_mediana = mediana(img_rotada, True)

    grafico = plt.figure()
    grafico.add_subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Imagen original")

    grafico.add_subplot(1, 3, 2)
    plt.imshow(img_rotada, cmap='gray')
    plt.title("Imagen con rotacion")

    grafico.add_subplot(1, 3, 3)
    plt.imshow(img_mediana, cmap='gray')
    plt.title("Imagen con filtro de mediana")

    plt.show()


def comparar(img, puntos):
    img_media = media(img, puntos)
    img_mediana = mediana(img, puntos)
    
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


def filtrar(tipo, img, puntos):
    img_filtrada = None
    if tipo == 'mediana':
        img_filtrada = mediana(img, puntos)
    else:
        img_filtrada = media(img, puntos)

    # img_s = rt.rotacion(img)  # Rotacion de imagen
    grafico = plt.figure()

    grafico.add_subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Imagen original")

    grafico.add_subplot(1, 2, 2)
    plt.imshow(img_filtrada, cmap='gray')
    plt.title("Imagen con " + tipo)

    plt.show()


if __name__ == "__main__":
    """
    Se realizan las siguientes funciones:
        - Filtro de media:
            Parámetros:
            : media   : indica que se realiza el filtro de la media
            : img     : indica el path de la imagen a utilizar
            : negros  : indica si se realiza el filtro para toda la imagen 
                o sólo los pixeles negros t / f. Si no se especifica, se aplica a
                toda la imagen
            Ejemplo:
                python3 main.py media img/img.jpg t # Se aplica sólo a los negros
                python3 main.py media img/img.jpg   # Se aplica a toda la imagen

        - Filtro de la mediana   :
             Parámetros:
            : mediana : indica que se realiza el filtro de la mediana
            : img     : indica el path de la imagen a utilizar
            : negros  : indica si se realiza el filtro para toda la imagen  
                o sólo los pixeles negros t / f. Si no se especifica, se aplica a
                toda la imagen
            Ejemplo:
                python3 main.py media img/img.jpg t # Se aplica sólo a los negros
                python3 main.py media img/img.jpg   # Se aplica a toda la imagen

        - Compara   :
            Parámetros:
            : compara : compara el filtrado para una imagen aplicando el filtro
                de la media y la mediana
            : img     : indica el path de la imagen a utilizar
            : negros  : indica si se realiza el filtro para toda la imagen 
                o sólo los pixeles negros t / f. Si no se especifica, se aplica a
                toda la imagen
            Ejemplo:
                python3 main.py media img/img.jpg t # Se aplica sólo a los negros
                python3 main.py media img/img.jpg   # Se aplica a toda la imagen

        - Rotacion:
            Parámetros:
            : rotacion : compara el filtrado para una imagen aplicando el filtro
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
        if arg_3 == 't':
            arg_3 = True
        elif arg_3 == 'f':
            arg_3 = False
        else:
            try:
                arg_3 = int(arg_3)
            except:
                print('Invald cast type to int for degrees')

    if function == 'media' or function == 'mediana':
        filtrar(function, img, arg_3)
    elif function == 'comparar':
        comparar(img, arg_3)
    elif function == 'rotacion':
        rotar(img, arg_3)
