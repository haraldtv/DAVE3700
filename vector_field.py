#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:17:48 2023

@author: harald
"""

import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-2, 2, 10),
				np.linspace(-2, 2, 10))

#Vectors
u = 1+x**2
v = x + y**3

plt.quiver(x, y, u, v, color="lightblue")
plt.title('F = (1+x**2, x+y**3)')

#Up the resolution
 #plt.figure(figsize=(8, 5), dpi=800)   

plt.grid() 
plt.show()
