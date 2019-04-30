# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from diafunc import linearfunc

aspart = linearfunc('curve/aspart-in-data.txt')
xs = np.arange(0, 120, 1)
#xs = [0, 15, 30, 55, 75] 
r = []
for x in xs:
    r.append(aspart(x))
    

fig, ax = plt.subplots(figsize=(5, 3))

ax.plot(xs, r)
plt.show()