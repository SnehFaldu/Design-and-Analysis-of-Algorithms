#write a code on linear regression
import numpy as np
import matplotlib.pyplot as plt
# Generate some sample data
np.random.seed(0)
X = np.random.randn(100, 1)
y = 2 * X + 1 + np.random.randn(100, 1) * 0.1

# Initialize parameters
theta = np.zeros((2, 1))

# Hyperparameters
learning_rate = 0.01
iterations = 1000

# Add bias term to X
X_with_bias = np.c_[np.ones((X.shape[0], 1)), X]

# Gradient descent
for _ in range(iterations):
    # Forward pass
    y_pred = X_with_bias @ theta
    
    # Compute gradients
    gradients = (1 / X.shape[0]) * X_with_bias.T @ (y_pred - y)
    
    # Update parameters
    theta -= learning_rate * gradients

# Print the learned parameters
print("Learned parameters:")
print(f"Intercept: {theta[0][0]}")
print(f"Slope: {theta[1][0]}")

# Plot the results
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, X_with_bias @ theta, color='red', label='Linear regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()