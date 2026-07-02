# Python Program to Illustrate Backpropagation Algorithm
import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(y):
    return y * (1 - y)

# Input, target, weights and bias
x = 0.5
target = 1

# Initial weights and biases
w1 = 0.2
w2 = 0.4
b1 = 0.1
b2 = 0.1

learning_rate = 0.5

# -------- Forward Propagation --------
hidden_input = x * w1 + b1
hidden_output = sigmoid(hidden_input)

final_input = hidden_output * w2 + b2
final_output = sigmoid(final_input)

print("Output before training:", final_output)

# -------- Backpropagation --------
# Calculate output error
output_error = target - final_output
output_delta = output_error * sigmoid_derivative(final_output)

# Calculate hidden layer error
hidden_error = output_delta * w2
hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

# Update weights and biases
w2 += learning_rate * output_delta * hidden_output
b2 += learning_rate * output_delta

w1 += learning_rate * hidden_delta * x
b1 += learning_rate * hidden_delta

# -------- Forward Propagation Again --------
hidden_input = x * w1 + b1
hidden_output = sigmoid(hidden_input)

final_input = hidden_output * w2 + b2
final_output = sigmoid(final_input)

print("Output after training:", final_output)