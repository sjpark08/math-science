import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Example inputs and outputs
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
expected_output = np.array([[0], [1], [1], [0]])

# Initialize weights and biases
weights = np.random.uniform(size=(2, 1))
bias = np.random.uniform(size=(1, 1))
learning_rate = 0.1

# Display initial inputs
print("Initial Inputs:")
print(inputs)

# Training process
for iteration in range(10000):
    # Forward propagation
    inputs_layer = inputs
    outputs = sigmoid(np.dot(inputs_layer, weights) + bias)

    # Backward propagation
    error = expected_output - outputs
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(inputs_layer.T, adjustments) * learning_rate
    bias += np.sum(adjustments, axis=0, keepdims=True) * learning_rate

    # Display outputs for each iteration
    if iteration % 100 == 0:  # Adjust this number to control the frequency of output display
        print(f"After iteration {iteration}:")
        print(outputs)

# Final output after training
print("Output after training:")
print(outputs)
