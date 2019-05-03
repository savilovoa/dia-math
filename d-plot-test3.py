
# -*- coding: utf-8 -*-
import scipy.integrate as integrate
import numpy as np
from diafunc import linearfunc
from scipy.integrate import quad
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import gamma


def myf(maxmmol, maxgoing,  endgoing, typebranch1, typebranch2):
    pass

norm = st.norm(loc=1, scale=0.25)
x = np.linspace(norm.ppf(0.0001), norm.ppf(0.9999), 50)

a = 2
#erl = st.erlang.stats(a)
mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
print (mean, var, skew, kurt)
x2 = np.linspace(0,6, 100)
#x2 = np.linspace(erl.ppf(0.0001, a), erl.ppf(0.9999, a), 50)
res, err = quad(gamma.pdf, 0, 6, args=(a)) 
print(res)
print(x2)

fig, ax = plt.subplots()

ax.plot(x, norm.pdf(x))
ax.plot(x2, gamma.pdf(x2, a))

plt.show()