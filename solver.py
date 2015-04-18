# A program to solve the Schrodinger equation and display probability density graphs

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

if False: # make this a cmd line option
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

######### 2D option ##########
else:
    Lx = input("Enter the length of the well in the x direction: ")
    Ly = input("Enter the length of the well in the y direction: ")
    nx = input("Enter the x energy level: ")
    ny = input("Enter the y energy level: ")

    x = np.arange(0, Lx, Lx/100.0)
    y = np.arange(0, Ly, Ly/100.0)
    Ax = np.sqrt(2.0/Lx)
    Ay = np.sqrt(2.0/Ly)
    psi_x = Ax*np.sin(nx*np.pi*x/Lx)
    psi_y = Ay*np.sin(ny*np.pi*y/Ly)
    
    PDx = psi_x**2
    PDy = psi_y**2

    X,Y = np.meshgrid(PDx, PDy)
    Z = X+Y

    fig, ax = plt.subplots()
    p = ax.pcolor(X, Y, Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
    cb = fig.colorbar(p, ax=ax)

    plt.show()
