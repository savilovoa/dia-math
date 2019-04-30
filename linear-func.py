# -*- coding: utf-8 -*-
from numpy import loadtxt
from io import StringIO 

class linearfunc():
    xs = []
    ys = []
    def __init__(self, filename):
        self.xs, self.ys = loadtxt(filename, delimiter=chr(9),unpack=True)   
    def f(self, x):
        res = 0
        for i in range(0,len(self.xs)-1):
            if self.xs[i] == x:
                res = self.ys[i]
                break
            elif self.xs[i] >= x:
                x_end = i
                res = self.ys[x_end-1] + (x-self.xs[i-1])*(self.ys[x_end] - self.ys[x_end-1]) / (self.xs[i] - self.xs[i-1])
                if self.ys[x_end] < self.ys[x_end-1]:
                    res = res * -1
                break
        return res
                    
                
        
    
#print(linearfunc('curve/aspart-in-data.txt').f(29))
