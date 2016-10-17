function[J, dJdW] = fun_costo(Wt, nn, Y, Xa)
% Recuperar los pesos
nnw1 = (nn(1) + 1) * nn(2); % calculando el numero de elementos de W1
nnw2 = (nn(2) + 1) * nn(3);
W1 = reshape(Wt(1: nnw1, 1), nn(2), nn(1) + 1);
W2 = reshape(Wt(nnw2+1: end, 1), nn(3), nn(2) + 1);

Ye = rednn(W1, W2, Xa);

E = Y - Ye;
Avgs = sum(E.^2, 2) / size(Y, 2);
J = sum(Avgs) / (2 * size(Y, 1));

m = size(Y, 1);
dJdY = -E / m;
dJdW1 = zeros(nn(2), nn(1) + 1);
dJdW2 = zeros(nn(3), nn(2) + 1);
[Ye, Y1, V1] = rednn(W1, W2, Xa);

for k = 1: m
    V2 = W2 * [1;Y1(:, k)];
    d2 = (dJdY(k, :)');
    d1 = (W2(:, 2:end)' * d2).*(1 - tanh(V1(:, k).^2));
    dJdW2 = dJdW2 + d2 * [1; Y1(:, k)]';
    dJdW1 = dJdW1 + d1 * Xa(k, :)\';
end

dJdW2 = dJdW2 / m;
dJdW1 = dJdW1 / m;
dJdW = [dJdW1(:);dJdW2(:)];