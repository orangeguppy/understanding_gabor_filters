import numpy as np
import matplotlib.pyplot as plt

def gabor_filter(x, y, wavelength, theta, psi, sigma, gamma):
    x_prime = x * np.cos(theta) + y * np.sin(theta)
    cosine = np.cos(theta)
    print(type(cosine), cosine)
    print(type(x_prime), x_prime.shape)
    y_prime = -x * np.sin(theta) + y * np.cos(theta)
    gaussian = np.exp(-0.5 * (x_prime**2 + gamma**2 * y_prime**2) / sigma**2)
    sinusoid = np.cos(2 * np.pi * x_prime / wavelength + psi)
    return gaussian * sinusoid

# Parameters
wavelength = 10
theta = np.pi / 4
psi = 0
sigma = 5
gamma = 1

# Coordinate grid
x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
x, y = np.meshgrid(x, y)
print(x, y)
print("===================")

# Gabor filter
gabor = gabor_filter(x, y, wavelength, theta, psi, sigma, gamma)

# Visualization
plt.imshow(gabor, cmap='gray')
plt.title('Gabor Filter')
plt.colorbar()
plt.show()