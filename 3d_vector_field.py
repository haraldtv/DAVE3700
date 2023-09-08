#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:44:55 2023

@author: harald
"""

import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.linspace(-1, 1, 8),
                      np.linspace(-1, 1, 8),
                      np.linspace(-1, 1, 8))

# Make the direction data for the arrows
u = x**2
v = y+z
w = z**3

ax.quiver(x, y, z, u, v, w, length=0.2, normalize=False)

plt.show()