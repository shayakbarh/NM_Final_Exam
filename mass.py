import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the density function
def density(r):
    
    return (3 * (1 + r**2)**(-5/2))/(4 * np.pi) # in kg/m^3

#Define the integrand to get enclosed mass
def integrand(r):
    return 4 * np.pi * r**2 * density(r)

# Calculate mass using numerical integration
def mass_enclosed(r):
    result, _ = quad(integrand, 0, r)
    return 0.5 * result

# Compute enclosed mass for various radii
radii = np.linspace(0, 10, 1000)
masses = [mass_enclosed(r) for r in radii]

# Plotting the results

plt.plot(radii, masses, label='Enclosed Mass')
plt.xlabel('Radius (r) in meter')
plt.ylabel('Enclosed Mass (M) in Kg/m^3')
plt.title("Q1. Enclosed Mass as a function of distance from centre")
plt.legend()
plt.grid()
plt.show()
