# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:05:55 2024

@author: franc
"""

import numpy as np
import math 
from scipy import signal
import matplotlib.pyplot as plt

a = 2/11
b = 5/11
c = 4/11
d = 9/23
e = 5/23

A = np.array([[a, c, d], \
              [b, a, e],\
              [c, b, d]])

#condizione iniziale random

x0 = np.random.rand(3,1)

#non vettore stocastico di principio

x0 = x0/np.sum(x0)
somma = 0
npassi = 99

for i in range(npassi):
    x0 = A@x0


    
print("stato dopo 99 passi:", x0)