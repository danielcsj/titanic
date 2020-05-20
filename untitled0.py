# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:22:21 2020

@author: upbt
"""

import numpy as np
import matplotlib.pyplot as plt

s = np.random.uniform(0,1,10000)

#plt.hist(s)


size_mean = 50
n_means = 1000

mean_list = []
for i in range(n_means):
    # Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
    mean = np.random.rand(1,size_mean).mean()
    mean_list.append(mean)
    
    
plt.hist(mean_list)

