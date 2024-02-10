import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1


weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[1], [0], [0], [1]])

for epoch in range(20000):
    # Feedforward
    input_layer = X
    hidden_layer_input = np.dot(input_layer, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    output_layer_output = sigmoid(output_layer_input)

    # Backpropagation
    error = y - output_layer_output
    d_output = error * sigmoid_derivative(output_layer_output)
    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer_output)

    # weight change
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
    weights_input_hidden += input_layer.T.dot(d_hidden) * learning_rate

predicted = (output_layer_output > 0.5).astype(int)

print("pish bini:")
print(predicted)