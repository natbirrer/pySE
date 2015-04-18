# A program to solve the Schrodinger equation and display probability density graphs

import numpy as np
import matplotlib.pyplot as plt

# get L and n
L = input("Enter the length of the well: ")
n = input("Enter the energy level: ")

# compute A and psi
x = np.arange(0, L, L/100.0)
A = np.sqrt(2.0/L)
psi = A*np.sin(n*np.pi*x/L)

# find PD
PD = psi**2

# plot
plt.plot(x,PD)
plt.show()
