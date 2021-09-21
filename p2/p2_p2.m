# extracting_algorithm

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

# Función para la desencriptación de un mensaje.
  % Entradas:
  %   A = imagen con mensaje.
  %   Wm , Wn = dimensiones del mensaje binario a desencriptar.
  %   seed = semilla para la generación de números aleatorios.
  %   T = threshold
  % Salidas:
  % msg = mensaje encriptado en la imagen.
function [msg] = extracting_algorithm(A, T, seed, Wm, Wn)
  
  # Establecer semilla para rand
  rand('seed',seed);
  
  # Definición de variables necesarias.
  [m, n, r] = size(A);
  used_coord = [];
  cont = 0;
  msg = zeros(Wm, Wn);
  msg = uint8(msg);
  [Wm, Wn] = size(msg);
  
  # Generar los bloques Wm x Wn del mensaje a desencriptar.
  Y = mat2cell(A, 4*ones(1, m/4), 4*ones(1, n/4), 1);

  # Inicio del algoritmo
  disp("Inicio de desencriptacion...");
  for iCell = 1:m/4
    for jCell = 1:n/4
      
      Bk = Y{iCell, jCell};
      [Uk, Sk, Vk] = svd(Bk);
      diag_s = diag(Sk);
      
      s1 = diag_s(1);
      s2 = diag_s(2);
      s3 = diag_s(3);
      s4 = diag_s(4);
      
      if cont < Wm * Wn
        [i_rand, j_rand] = rand_coord(used_coord, Wm, Wn);
        
        cont += 1;
        used_coord = [used_coord; i_rand j_rand];
        
        if (s2 - s3) > T/2
          msg(i_rand, j_rand, 1) = 1;
        else
          msg(i_rand, j_rand, 1) = 0;
        endif
      endif
    endfor
  endfor
  disp("Desencriptacion finalizada.")
  msg = msg * 255;
endfunction

% ----------------- Para probar -------------------------

#{
I_color = imread("out.jpg");
A = I_color(:,:,1);

A = im2double(A);

[salida] = extracting_algorithm(A, 0.5, 3, 8, 8);
imshow(salida);
title("Mensaje obtenido");
#}

