x1 = -10:0.1:10
x2 = -10:0.1:10
Y = 10 * sin(x1) + 10 * cos(x2);

% Numero de neuronas en capas
nn0 = 2; % numero de entradas
nn1 = 1; % numero de neuronas en capa 1
nn2 = 1; % numero de neuronas en capa 2 o salida

W1 = rand(nn1, nn0 + 1);
W2 = rand(nn2, nn1 + 1);

Xa = [ones(size(x1, 2), 1) x1' x2'] % Datos de entrada

Ye = rednn(W1, W2, Xa); % evaluando red neuronal

wnn1 = (nn0 + 1) * nn1;
wnn2 = (nn1 + 1) * nn2;
Wt = [W1(:);W2(:)];

[J, dJdW] = fun_costo(Wt, [nn0 nn1 nn2], Y', Xa); % calculo de la funcion de costo y gradiente