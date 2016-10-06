clear all;
close all;
clc;

load datos4.mat;

X = [];
for k = 1:35
    % text = sprintf('X(:, k) = BMV_%0.0ffinal(:, 5);', k);
    text = sprintf('X(:, k) = BMV_%0.0ffinal(:, 5)/max(BMV_%0.0ffinal(:, 5));', k, k);
    eval(text);
end

net = competlayer(20);
net = train(net, X);
Y = net(X);
Y = vec2ind(Y);
grupos = unique(Y);
%%
for k = 1: size(grupos, 2)
   text = sprintf('grupo%0.0f = X(:, Y == grupos(1, k))', grupos(1, k));
   eval(text);
   figure(k);
   text = sprintf('plot(grupo%0.0f)', grupos(1, k));
   eval(text);
end
