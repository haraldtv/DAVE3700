#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:07:34 2023

@author: harald
"""

import numpy as np
import matplotlib.pyplot as plt

N = 500
XMIN = -2*np.pi
XMAX = 2*np.pi

#ax = plt.figure(figsize =(3, 2), dpi=400).add_subplot(projection='3d')
ax = plt.figure().add_subplot(projection='3d')

# Prepare arrays x, y, z
z = np.linspace(XMIN, XMAX, N)

x = z * np.sin(2*z)
y = z * np.cos(2*z)

ax.plot(x, y, z, label="DAVE3700")
ax.legend()

plt.show()