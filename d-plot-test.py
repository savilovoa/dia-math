# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from diafunc import linearfunc



aspart = linearfunc('curve/aspart-in-data.txt', -1 )
gluk = linearfunc('curve/glukoza-in-data.txt', -1)
med = linearfunc('curve/55-69-in-data.txt', -1)
far = linearfunc('curve/30-55-in-data.txt', -1)

xs = np.arange(0, 120, 5)
r = []
for i in xs:
    r.append(5+gluk.f(i)+far.f(i)-aspart.f(i))

gridsize = (2, 1)
fig = plt.figure(figsize=(10, 6))
ax1 = plt.subplot2grid(gridsize, (0, 0))
ax2 = plt.subplot2grid(gridsize, (1, 0))

ax1.plot(aspart.xplot, aspart.yplot, label='Новорапид')
ax1.plot(gluk.xplot, gluk.yplot, label='Глюкоза')
ax1.plot(med.xplot, med.yplot, label='55-69 (средний)')
ax1.plot(far.xplot, far.yplot, label='30-55 (долгий)')

ax1.legend()

#ax2.plot(xs, r)
plt.show()