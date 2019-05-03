
# -*- coding: utf-8 -*-
import scipy.integrate as integrate
import numpy as np
from diafunc import linearfunc
from scipy.integrate import quad
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.integrate import quad


def myf(maxmmol, maxgoing,  endgoing, typebranch1, typebranch2):
    pass

norm = st.norm(loc=1, scale=1)
x = np.linspace(norm.ppf(0.01), norm.ppf(0.5), 50)

fig, ax = plt.subplots()



k = norm.pdf(30)
k = 6/k
def myf(x):
    return norm.pdf(x)*k

res, err = quad(myf, 0, 60) 
print(res)

norm2 = st.norm(loc=40, scale=15)
ix = np.linspace(norm2.ppf(0.01), norm2.ppf(0.99), 120)
ik = norm2.pdf(40)
ik = 6.5/ik
def myif(x):
    return norm2.pdf(x)*ik

res, err = quad(myif, 0, 120) 
print(res)

sbx = range(0, 120, 1)
sby = [5]
for i in sbx:
    if i != 0:
        if i > 30:
            res, err = quad(myf, 0, 30)
        else:
            res, err = quad(myf, 0, i)
        res1, err1 = quad(myif, 0, i)
        rk = 5 + (res - res1)/5.714        
        #print("{}: rk {} g {}, i {}, r {} ".format(i, rk, res, res1, res - res1))
        if rk > -1:
            sby.append(rk)
        else:
            sby.append(-1)
    
    

fig, ax = plt.subplots()


ax.plot(x, myf(x))
ax.plot(ix, myif(ix))
ax.plot(sbx, sby)


plt.show()