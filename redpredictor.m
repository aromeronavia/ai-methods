%% limpiando todo
close all;
clear all;
clc;
load datos4.mat;

%% Realizando una red neuronal con paqueteria de matlab
data = BMV_1final(:, 5);
nrezago = 3;

for k = 1: nrezago + 1
    temp(:, k) = data(k: end - nrezago + (k - 1), 1)
end

X = temp(:, 1:end-1);
Y = temp(:, end);

ndatatrain = 0.9;
datatrain = round(size(X, 1) * ndatatrain);
Xtrain = X(1: datatrain, :);
Ytrain = Y(1: datatrain, :);

Xtest = X(datatrain+1: end, :);
Ytest = Y(datatrain+1: end, :);

red = feedforwardnet(10);
red.performFcn = 'msereg';
red = train(red, Xtrain', Ytrain');
Ye_train = red(Xtrain');
Ye_test = red(Xtest');

% J = perform(red, Y', [Ye_train Ye_test]);

%% Visualizacion
plot(1:size(Y, 1), Y', 'b-', 1:size(Y, 1), [Ye_train Ye_test], 'r--', [datatrain datatrain], [min(Y) max(Y)], 'g--');
grid;