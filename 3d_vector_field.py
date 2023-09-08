#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:44:55 2023

@author: harald
"""

import matplotlib.pyplot as plt
import numpy as np

N = 4
XMIN = -1
XMAX = 1

ax = plt.figure().add_subplot(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.linspace(XMIN, XMAX, N),
                      np.linspace(XMIN, XMAX, N),
                      np.linspace(XMIN, XMAX, N))

# Make the direction data for the arrows
u = -y
v = x
w = 0

ax.quiver(x, y, z, u, v, w, length=0.6, normalize=False)

plt.show()