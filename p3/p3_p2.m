close all
clear all
clc
pkg load image


function L = list_files(path)
L = dir ( path );
L = L (3: length (L));
L = struct2cell (L);
L = L (1 ,:) ;
end

function face_recognition(path, test_image, epsilon_0);
  
  %Cantidad de personas
  persons = 40;
  %Cantidad de fotos por persona
  photos = 9;
  % Cantidad de imágenes de rostros
  N = persons * photos; 
  % Tamaño original mxn redimensionado
  [m, n] = size(test_image);
  M  = m*n;
  % Se crea la matriz S de tamaño MxN (mn x N)
  S = zeros(M, N); 
  
  
  %Se carga la base de datos en S
  BaseData = list_files(path); 
  for i =1:N;    
    f = im2double(imread(strcat(path, BaseData{1,i})));
    S(:, i) = f(:);
  endfor 

  %Calcular el promedio
  f_prom = zeros(M, 1);
  for i =1: N;
    f_prom = f_prom + S(:, i);
  endfor 
  f_prom = f_prom * (1/N);


  % A = f_i - f_prom
  A = S - repmat(f_prom, 1, N);

  %Calcular matriz U_r
  [U, s, v] = svd(A, 0);
  r = N; 
  U_r = U(:, 1:r);
  
  %Calcular matriz de x_i
  X = U_r' * A;
  
  %Calcular w
  dif = test_image(:) - f_prom; 
  w = U_r' * dif; 
  
  % Calcular epsilon para cada imagen 
  epsilons = zeros(N, 1);
  for i = 1:N
      epsilons(i, 1) = norm((w - X(:, i)));
  end
  %Obtener el mínimo
  [x_j j] = min(epsilons(:, 1));
  
  %Si x_j < e0, detectar el rostro
  if norm(w - x_j) < epsilon_0
      disp(sprintf('El rostro es de la persona de la imagen %s', BaseData{1,j}));
  else
      disp('El rostro es desconocido');
  end
end


path = 'C:\Users\kimbe\Desktop\Problema3\Database\';
epsilon_0 = 500;

test_image = im2double(imread('C:\Users\kimbe\Desktop\Problema3\Comparar\13_10.png'));
tic;
face_recognition(path, test_image, epsilon_0);
tiempo_total = toc

