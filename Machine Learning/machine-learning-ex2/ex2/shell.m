u = linspace(-1, 1.5, 50);
v = linspace(-1, 1.5, 50);
    z = zeros(length(u), length(v));
    % Evaluate z = theta*x over the grid
    for i = 1:length(u)
        for j = 1:length(v)
        mapFeature(u(i), v(j))
            z(i,j) = mapFeature(u(i), v(j))*[2;2];
        end
    end