# -*- coding: utf-8 -*-
from numpy import loadtxt
from io import StringIO 
import scipy.stats as st
import scipy.integrate as integrate
from scipy.integrate import quad
import numpy as np


class linearfunc(object):
    xs = []
    ys = []
    xmax = 0
    k_norm = 1.0
    #xplot = []
    #yplot = []
    def __init__(self, filename, kf = 12):
        super(linearfunc, self).__init__()
        self.xs, self.ys = loadtxt(filename, delimiter=chr(9),unpack=True)   
        for i in self.xs:
            if self.xmax < i:
                self.xmax = i
        print("Max time going {}. Start calc S on {}:".format(self.xmax, kf))
        if kf != -1:
            self.kf_calc(kf)
        
        # подготовим массивы для графиков
        self.xplot = np.arange(0, self.xmax, 5)
        self.yplot = []
        for x in self.xplot:
            self.yplot.append(self.f(x))    
            
    def kf_calc(self, kf):
        res = kf + 2
        k = 2
        n = True
        while abs(res - kf) > 1:
            res, err = quad(self.f, 0, self.xmax) 
            if res - kf > 1:
                if not n:
                    k = k + 0.25
                    n = True
                self.k_norm = self.k_norm / k
            elif res - kf < -1:
                if n:
                    k = k -0.25
                    n = False
                self.k_norm = self.k_norm * k    
            print("... step find kf: {} {}".format(self.k_norm, res))
            
        
            
    def f(self, x):
        res = 0
        for i in range(0,len(self.xs)-1):
            if self.xs[i] == x:
                res = self.k_norm * self.ys[i]
                break
            elif self.xs[i] >= x:
                x_end = i
                #dy = self.ys[x_end] - self.ys[x_end-1]
                #dx = self.xs[x_end] - self.xs[x_end-1]
                #res = dy/dx
                #res = x * dy/dx
                res = self.k_norm * (self.ys[x_end-1] +((x-self.xs[x_end-1])*(self.ys[x_end] - self.ys[x_end-1]) / (self.xs[x_end] - self.xs[x_end-1])))
                
                break
        
        return res
                    
                
        
    
#print(linearfunc('curve/aspart-in-data.txt').f(43))
