clear all;
load datos2.mat;
neurons = 6;
X = datos2;
inputs = size(X, 1);
eta = 0.1;

W = rand(inputs, neurons); % Pesos iniciales
iterations = 10;
for i = 1: iterations
    X = X(:, randperm(size(X, 2)));
    for k = 1: size(X, 2)
        for j = 1: neurons
            D = X(:, k) - W(:, j);
            V(:, j) = D' * D;
        end

        [val, ind] = min(V); % Determinando qué neurona es la mas cercana
        Y = zeros(neurons, 1);
        Y(ind, :) = 1;
        W(:, ind) = W(:, ind) + eta * (X(:, k) - W(:, ind));
    end
end

% Simulacion de resultados
X = datos2;
Y = zeros(neurons, size(X, 2));
for k = 1: size(X, 2);
    for j = 1: neurons
        D = X(:, k) - W(:, j);
        V(:, j) = D' * D;
    end
    
    [val, ind] = min(V); % Determinando qué neurona es la mas cercana
    Y(ind, k) = 1;
end

Y = vec2ind(Y);
plot3(X(1, :), X(2, :), X(3, :), 'b.', W(1, :), W(2, :), W(3, :), 'rx', 'LineWidth', 2);
