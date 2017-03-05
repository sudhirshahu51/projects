function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples
n = length(theta);
% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
tmp = 0;
for i=1:m
    tmp = tmp + (-y(i)*log(sigmoid(X(i,:)*theta)) - (1 - y(i))*log(1 - sigmoid(X(i,:)*theta)));
end

tmp2 = 0;

for j=2:n
    tmp2 = tmp2 + theta(j).^2;
end

tmp2 = (tmp2*lambda)/(2*m);
J = tmp/m + tmp2;

% Note: grad should have the same dimensions as theta
%

for j=1:length(theta)
    tmp = 0;
    for i=1:m
      tmp = tmp + (sigmoid(X(i,:)*theta) - y(i))*X(i,j);
    end
    if j != 1
      grad(j) = (tmp + theta(j).*lambda)/m;
    else
      grad(j) = tmp/m;
end





% =============================================================

end
