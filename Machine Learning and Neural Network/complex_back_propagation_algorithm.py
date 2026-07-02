# Write a python program to illustrate working of backpropagation algorithm 

import numpy as np

# 1. Activation function and its derivative
def sigmoid(x):
    """Compute the sigmoid activation function."""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Compute the derivative of the sigmoid function (for backpropagation)."""
    return x * (1 - x)

# 2. Define the training dataset (XOR logic gate)
# Input features (4 samples, 2 features each)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Target outputs (4 samples, 1 output each)
y = np.array([[0], 
              [1], 
              [1], 
              [0]])

# Seed the random number generator for reproducibility
np.random.seed(42)

# 3. Network Architecture Configurations
input_neurons = 2    # Two input features
hidden_neurons = 3   # Three neurons in the hidden layer
output_neurons = 1   # One final prediction output
learning_rate = 0.5  # Step size for gradient descent
epochs = 10000       # Number of training iterations

# 4. Initialize weights and biases randomly
# Weights connecting Input layer to Hidden layer
W1 = np.random.uniform(size=(input_neurons, hidden_neurons))
b1 = np.zeros((1, hidden_neurons))

# Weights connecting Hidden layer to Output layer
W2 = np.random.uniform(size=(hidden_neurons, output_neurons))
b2 = np.zeros((1, output_neurons))

print("--- Training Started ---")

# 5. Training Loop
for epoch in range(epochs):
    
    # === PHASE 1: Forward Propagation ===
    # Calculate hidden layer activations
    hidden_layer_input = np.dot(X, W1) + b1
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    # Calculate final output layer activations
    output_layer_input = np.dot(hidden_layer_output, W2) + b2
    predicted_output = sigmoid(output_layer_input)
    
    # === PHASE 2: Backpropagation (Error Calculation) ===
    # Compute error at the output layer (Loss derivative)
    error_output = y - predicted_output
    
    # Compute gradient (delta) at the output layer
    # Delta = error * derivative of activation function
    slope_output = sigmoid_derivative(predicted_output)
    delta_output = error_output * slope_output
    
    # Compute error contributed by the hidden layer
    error_hidden = delta_output.dot(W2.T)
    
    # Compute gradient (delta) at the hidden layer
    slope_hidden = sigmoid_derivative(hidden_layer_output)
    delta_hidden = error_hidden * slope_hidden
    
    # === PHASE 3: Weight and Bias Updates (Gradient Descent) ===
    # Update weights and biases using the calculated gradients
    W2 += hidden_layer_output.T.dot(delta_output) * learning_rate
    b2 += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
    
    W1 += X.T.dot(delta_hidden) * learning_rate
    b1 += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate
    
    # Print Mean Squared Error metrics every 2000 epochs
    if epoch % 2000 == 0:
        loss = np.mean(np.square(error_output))
        print(f"Epoch {epoch:5d} | Mean Squared Error (Loss): {loss:.6f}")

print("\n--- Training Complete ---")

# 6. Evaluate Final Model Predictions
print("\nFinal Predicted Outputs vs Target Outputs:")
for i in range(len(X)):
    print(f"Input: {X[i]} -> Target: {y[i][0]} -> Predicted: {predicted_output[i][0]:.4f}")
