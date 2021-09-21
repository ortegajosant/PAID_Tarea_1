# Graphics

1;
clc; clear;
pkg load image;
source("p2_p1.m");
source("p2_p2.m");


function graph(A, W, seed)
  
  # Definir variables necesarias
  [m, n] = size(A);
  [Wm, Wn] = size(W);
  calidad_graph = [];
  error_graph = [];
  
  for T = 0.0:0.5:5
    disp(T);
    # Encriptar el mensaje
    [O] = embedding_algorithm(A, W, seed, T);

    # Extraer el mensaje
    [msg] = extracting_algorithm(O, T, seed, Wm, Wn);
    
    # Obtener error y norma de frobenius
    calidad_graph = [calidad_graph; T norm(A-O, 'fro')];
    error_graph = [error_graph; T mean(mean(msg == W))*100];
    disp("\n");

  endfor
  
  figure
  subplot(1, 2, 1);
  plot(error_graph(:, 1), error_graph(:, 2), 'k', 'LineWidth', 2);
  xlabel('Threshold');
  ylabel('Error (%)');
  title('Error extraccion del mensaje');

  subplot(1, 2, 2);
  plot(calidad_graph(:, 1), calidad_graph(:, 2), 'k', 'LineWidth', 2);
  xlabel('Threshold');
  ylabel('Norm');
  title('Error calidad de la imagen');
endfunction
