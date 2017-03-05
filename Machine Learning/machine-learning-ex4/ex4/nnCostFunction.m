function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));
% Size(Theta1) = hidden_layer_size*(input_layer_size+1)

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));
% Size(Theta2) = num_labels*(hidden_layer_size+1)
                 
% Setup some useful variables
m = size(X, 1);
% m = no. of examples

% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
% 


% Making the output layer using given classes for ex [0 0 0 1 0 0 0 0 0 0]
Y = zeros(m,num_labels);
for i=1:m,
    Y(i,y(i)) = 1;
end

% For backpropagation intializing error terms
si3 = zeros(num_labels, 1);                       %size(si3) = num_labels*1
si2 = zeros(1 + hidden_layer_size, 1);            %size(si2) = (1+hidden_layer_size)*1
si1 = zeros(1 + input_layer_size, 1);             %size(si1) = (1+input_layer_size)*1
delta1 = zeros(hidden_layer_size,size(X,2)+1);                      %size(delta1) = (no. of features)*1
delta2 = zeros(num_labels,hidden_layer_size+1);              %size(delta2) = hidden_layer_size*1
% cost function without regularization

X = [ones(m,1) X];
tmp1 = 0;
for i=1:m,
    tmp = 0;
    a1 = X(i,:)';           %size(a1) = (no. of features)*1
    z2 = Theta1*a1;                              
    %size(z2) = (hidden_layer_size*1) = [(hidden_layer_size*(input_layer_size+1)) * ((no. of features)*1)]
    a2 = sigmoid(z2);       %size(a2) = hidden_layer_size*1
    a2 = [1; a2];           %size(a2) = (hidden_layer_size+1)*1
    z3 = Theta2*a2;
    %size(z2) = (num_labels*1) = [(num_labels*(hidden_layer_size+1)) * ((hidden_layer_size+1)*1)]
    a3 = sigmoid(z3);       %size(a3) = num_labels*1
    for k=1:num_labels,
        tmp = tmp + (-Y(i,k).*log(a3(k)) - (1 - Y(i,k)).*log(1 - a3(k)));
    end
    si3 = a3 - Y(i,:)';     %size(si3) = num_labes*1
    si2 = Theta2(:, 2:end)'*si3.*sigmoidGradient(z2);
    %size(si2) = hidden_layer_size*1 = [(hidden_layer_size*num_labels) * (num_labels*1)]
    delta2 = delta2 + si3*a2';
    %size(delta2) = [(num_labels*1) * (1*(hidden_layer_size))]
    delta1 = delta1 + si2*a1';
    %size(delta1) = [(hidden_layer_size*1) * (1*(no. of features))]    
    tmp1 = tmp1 + tmp;
end
J = tmp1/m;

Theta1_grad = (1/m)*(delta1 + [zeros(size(delta1,1),1), lambda*Theta1(:,2:end)]);
Theta2_grad = (1/m)*(delta2 + [zeros(size(delta2,1),1), lambda*Theta2(:,2:end)]);

% Regularization term of cost function
% Do not add the first col of theta since it is for the biased terms.
reg_term = lambda*(sum([Theta1(:,2:end).^2](:)) + ...
            sum([Theta2(:,2:end).^2](:)))/(2*m);
J = reg_term + J;




% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];

end