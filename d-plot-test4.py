# -*- coding: utf-8 -*-
import scipy.integrate as integrate
import numpy as np
from diafunc import linearfunc
from scipy.integrate import quad
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import gamma


class myf(object):
    
    def __init__(self, maxmmol, maxgoing,  endgoing, typebranch1, typebranch2):
        self.xs = range(0, endgoing, 1)
        self.ys = []
        
        if typebranch1 == typebranch2:
            if typebranch1 == "line":
                for x in range(0, endgoing, 1):
                    if x <= maxgoing:
                        self.ys.append(x * maxmmol / maxgoing) 
                    else:
                        self.ys.append(maxmmol - (x - maxgoing) * maxmmol / (endgoing - maxgoing))
            elif typebranch1 == "elrong":
                a = 2
                mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
                xr = np.linspace(0,1, maxgoing)
                xr2 = np.linspace(1.001, 6, endgoing-maxgoing)
                xr = xr + xr2                
                ky = maxmmol / gamma.pdf(1, a)
                kx1 = maxgoing 
                kx2 = (endgoing - maxgoing) / 5
                for x in xr:
                        self.ys.append(gamma.pdf(x, a) * ky)
        else:
            if typebranch1 == "line":
                for x in range(0, maxgoing, 1):
                    self.ys.append(x * maxmmol / maxgoing) 
                
            if typebranch2 == "line":
                for x in range(maxgoing+1, endgoing, 1):
                    self.ys.append(maxmmol - (x - maxgoing) * maxmmol / (endgoing - maxgoing))
            elif typebranch2 == "norm":   
                norm = st.norm(loc=1, scale=0.25)
                xr = np.linspace(norm.ppf(0.5), norm.ppf(0.9999), endgoing-maxgoing)
                k = maxmmol / norm.pdf(1)
                for x in xr:
                    self.ys.append( norm.pdf(x) * k)
                
                
                
                  
    
    def f(x):
        pass

y1 = myf(10.24, 35, 50, "line", "norm")
y2 = myf(10.24, 40, 240, "elrong", "elrong")


fig, ax = plt.subplots()

ax.plot(y1.xs, y1.ys)

plt.show()