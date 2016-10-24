%% limpiando todo
close all;
clear all;
clc;
load datos4.mat;

%% Realizando una red neuronal con paqueteria de matlab
X(:, 1) = BMV_1final(:, 5);
X(:, 2) = BMV_2final(:, 5);
X(:, 3) = BMV_3final(:, 5);
X(:, 4) = BMV_4final(:, 5);

Y = IPCfinal(:, 5);

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
plot(1:size(Y, 1), Y', 'b-', 1:size(Y, 1), [Ye_train Ye_test], 'r--');
grid;