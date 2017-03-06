# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:31:29 2017

@author: Alek
"""

import numpy as np
import matplotlib.pyplot as plt

# Input data
alphad = 2             # angle of attack [deg]
k = 10                  # semi-axis ratio for ellipse
R = 1.0                 # cylinder radius 

alpha = alphad*np.pi/180    #
c2 = R**2*(k-1)/(k+1)   # c**2
c = np.sqrt(c2)         # transformation constant
major_str = str(R+c2/R) 
minor_str = str(R-c2/R)
theta_str = str(alphad)

# Mesh grid
N = 100                             # no. of points in each direction
x_start, x_end = -5.0, 5.0          # boundaries for x-dir.
y_start, y_end = -5.0, 5.0          # boundaries for y-dir.
x_ar = np.linspace(x_start, x_end, N) #
y_ar = np.linspace(y_start, y_end, N)
x, y = np.meshgrid(x_ar,y_ar)       # meshes grid
z = x+1j*y                          # Complex mesh plane

# Exclusion of points inside circle
for i in range(N):
    for j in range(N):
        if abs(z[i,j])<= (R-5e-3):
            z[i,j] = complex(float('nan'),float('nan'))


# Aerodynamic potential
f = np.exp(-1j*alpha)*z + (np.exp(1j*alpha)*R**2)/z

# Joukowski transformation
J = z+c2/z

plt.figure()
plt.contour(x,y,f.imag)