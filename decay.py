import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Given parameters
lambda_val = 2.5  # decay constant in s^-1
n_0 = 40  # initial number density in particles/m^3
t_max = 10  # maximum time in seconds

# Define the differential equation
def decay_equation(t):
    return -lambda_val

# Function to integrate the differential equation using scipy's quad
def integrate_decay_equation(t):
    result, _ = quad(decay_equation, 0, t)
    return n_0 * np.exp(result)

# Time values for plotting
t_values = np.linspace(0, t_max, 1000)

# Numerical solution using scipy's quad
n_values = np.vectorize(integrate_decay_equation)(t_values)

# Plot the evolution of n
plt.plot(t_values, n_values, label = r'$n(t)$', color = 'green')
plt.title('Q 6: Evolution of Number Density(n) with time')
plt.xlabel('Time (s)')
plt.ylabel('n (particles/m^3)')
plt.legend()
plt.grid(True)
plt.show()
