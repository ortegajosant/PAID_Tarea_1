clear; clc; close all;

pkg load image;

source("p2_p1.m");
source("p2_p2.m");
source("p2_p3.m");

# Definir threshold
T = 0.5;

# Abrir imagen
I_color = imread("barbara.jpg");
A = I_color(:,:,1);
A = im2double(A);
[m, n, r] = size(A);

# Generar el mensaje aleatorio.
seed = 3;
rand('seed',seed);
W = uint8(randn(8, 8))*255;
[Wm, Wn] = size(W);


# ---------------------- Encriptar y desencriptar ---------------------------
#{

# Encriptar el mensaje
[O] = embedding_algorithm(A, W, seed, T);

# Extraer el mensaje
[msg] = extracting_algorithm(O, T, seed, Wm, Wn);

subplot(2,2,3);
imshow(W);
title("Mensaje");

subplot(2,2,4);
imshow(msg);
title("Mensaje extraido");

# Obtener el error de la imagen con el mensaje
error = mean(mean(msg == W)) * 100

# Obtener la norma de Frobenius entre las dos imagenes
frobenius = norm(A-O, 'fro')

#}

# ------------------------ Generar graficos --------------------------------

#graph(A, W, seed);

# ------------------------ Obtener mensaje (parte 3) ------------------------


img_encripted = load("barbara_encriptada.mat");
temp = struct2cell(img_encripted);
img_encripted = im2double(temp{1,1});
[m, n, r] = size(A)

T = 0.05;
seed = 3;

[msg] = extracting_algorithm(img_encripted, T, seed, Wm, Wn);
imshow(msg);

