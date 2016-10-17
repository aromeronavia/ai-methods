function [Ye, Y1, V1] = rednn(W1, W2, Xa)
V1 = W1 * Xa';
Y1 = tanh(V1);
Ye = (W2 * [ones(1, size(Y1, 2));Y1])';