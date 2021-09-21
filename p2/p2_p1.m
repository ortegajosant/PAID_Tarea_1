# embedding_algorithm

1;
clc; clear;
pkg load image;

# Función para la generación de coordenadas aleatorias
  % Entradas:
  %   used_coord = registro de coordenadas utilizadas.
  %   m, n = dimensiones del mensaje.
  % Salidas:
  %   i, j = nuevas coordenadas libres.
function [i, j] = rand_coord(used_coord, m, n);
    free = 1;
    while (free)
        i = round(rand(1) * (m-1)) + 1;
        j = round(rand(1) * (n-1)) + 1;
        free = 0;
        for k=1:size(used_coord, 1)
            if (isequal(used_coord(k,:), [i j]))
              free = 1;
              break;
            endif
        endfor
    endwhile
endfunction

# Función para la encriptación en un mensaje
  % Entradas:
  %   A = imagen a encriptar mensaje.
  %   W = mensaje binario a encriptar.
  %   seed = semilla para la generación de números aleatorios.
  %   T = threshold
  % Salidas:
  % image_o = imagen con mensaje encriptado.
function [image_o] = embedding_algorithm(A, W, seed, T)
 
  # Establecer semilla para rand
  rand('seed', seed);
  
  # Definición de variables necesarias.
  [m, n, r] = size(A);
  used_coord = [];
  [Wn, Wm] = size(W);
  cont = 0;
  
  # Generar los bloques 4x4 de la imagen y para almacenar la salida.
  Y = mat2cell(A, 4*ones(1, m/4), 4*ones(1, n/4), 1);
  O = mat2cell(zeros(m, n, 1), 4*ones(1, m/4), 4*ones(1, n/4));
  
  # Inicio del algoritmo
  disp("Inicio de encriptacion...");
  for iCell = 1:m/4
    for jCell = 1:n/4
      Bk = Y{iCell, jCell};
      
      [Uk, Sk, Vk] = svd(Bk);
      Sk = diag(Sk);
      
      if cont < Wn * Wm
        
        [i_rand, j_rand] = rand_coord(used_coord, Wn, Wm);
        used_coord = [used_coord; i_rand j_rand];
        cont += 1;
        
        if W(i_rand, j_rand) == 255
          if (Sk(3) > Sk(2) - Sk(3))
            Sk(4) = Sk(2) - Sk(3);
          else
            Sk(4) = 0;
          endif
          Sk(2) = Sk(2) + T;
        endif
        
     endif
     
     if Sk(3) < Sk(4)
      Sk(3) = Sk(4);
     endif
      
      Sk = diag(Sk);

      O(iCell, jCell) = Uk * Sk * Vk';
    endfor
  endfor
  
  disp("Encripcion finalizada.")
  
  # Convertir imagen con mensaje a matriz.
  image_o = cell2mat(O);
  image_o = im2double(image_o);
  
  # Alamcenar imagen
  imwrite(image_o, "out.jpg");
  
  # Mostrar imagen original
  subplot(2,2,1);
  imshow(A);
  title("Imagen original");

  # Mostrar mensaje original
  subplot(2,2,2);
  imshow(image_o);
  title("Imagen con mensaje");
  
endfunction


% ----------------- Para probar -------------------------

#{
I_color = imread("barbara.jpg");
A = I_color(:,:,1);

A = im2double(A);

# Generar el mensaje aleatorio.
W = randn(8,8);
W = uint8(W) * 255;

subplot(2,2,3);
imshow(W);
title("Mensaje original");

[O] = embedding_algorithm(A, W, 3, 0.5);

# Obtener la norma de Frobenius entre las dos imagenes
frobenius = norm(A-O, 'fro')

#}

