# Tarea 1 - Procesamiento y análsisi de imágenes digitales

## Parte 1

### Contenido

Esta sección es la parte 1, la cual contiene la aplicación de los siquientes componentes:
    - Filtro de la mediana para una imagen
    - Filtro de la media para una imagen
    - Rotación para una imagen

### Uso

Cada una de las funciones pueden ser utilizadas la importación específica en el código deseado, 
sin embargo, se ha elaborado un main que contiene el acceso a todas las funcionalidades. Para utilizar
este main, seguir las siguientes instrucciones.

- **Filtro de la media**:
    
    Parámetros:
    
    `: media   :` indica que se realiza el filtro de la media
    
    `: img     :` indica el path de la imagen a utilizar
    
    `: negros  :` indica si se realiza el filtro para toda la imagen 
        o sólo los pixeles negros t / f. Si no se especifica, se aplica a
        toda la imagen
    
    Ejemplo:
    
    `python3 main.py media img/img.jpg t` # Se aplica sólo a los negros

    `python3 main.py media img/img.jpg`   # Se aplica a toda la imagen

- **Filtro de la mediana**:
    
    Parámetros:
    
    `: mediana :` indica que se realiza el filtro de la mediana
    
    `: img     :` indica el path de la imagen a utilizar  
    
    `: negros  :` indica si se realiza el filtro para toda la imagen  
        o sólo los pixeles negros t / f. Si no se especifica, se aplica a
        toda la imagen
    
    Ejemplo:
    
    `python3 main.py media img/img.jpg t` # Se aplica sólo a los negros

    `python3 main.py media img/img.jpg  ` # Se aplica a toda la imagen

- **Comparar:**
    
    Parámetros:
    
    `: compara :` compara el filtrado para una imagen aplicando el filtro
        de la media y la mediana
    
    `: img     :` indica el path de la imagen a utilizar
    
    `: negros  :` indica si se realiza el filtro para toda la imagen 
        o sólo los pixeles negros t / f. Si no se especifica, se aplica a
        toda la imagen
    
    Ejemplo:
    
    `python3 main.py media img/img.jpg t` # Se aplica sólo a los negros
    
    `python3 main.py media img/img.jpg  ` # Se aplica a toda la imagen

- **Rotacion:**

    Parámetros:
    
    `: rotacion :` compara el filtrado para una imagen aplicando el filtro
        de la media y la mediana
    
    `: img     :` indica el path de la imagen a utilizar
    
    `: grados  :` indica el angulo de giro a utilizar para realizar la rotación
        Si no se especifica, el giro es de 45 grados ('pi/4')
    
    Ejemplo:

    `python3 main.py rotacion img/img.jpg 90` # Se aplica un giro de pi/2 
    
    `python3 main.py rotacion img/img.jpg   ` # Se aplica un giro de pi/4