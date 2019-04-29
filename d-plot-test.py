# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

xs = np.arange(0, 120, 1)
#xs = [0, 15, 30, 55, 75] 
r = []
r2 = []

a =-3.06282216833E-002
b =2.23132472411E-001
c =-4.34107514124E-003
d =2.07206130565E-005
for i in xs:
    r.append(a + b*i + c*i*i + d*i*i*i)
    

fig, ax = plt.subplots(figsize=(5, 3))

ax.plot(xs, r)
plt.show()