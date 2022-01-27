import sys
from math import *
import numpy as np

k = 2
center ="""
6 2
7.9 7.4
2.4 8.0
4.4 2.7
8.8 8.3
0.8 6.9
6.2 1.9
""".split('\n')

print(center)

centers = {tuple(edge.split(' ')) for edge in center if edge}

print(centers)

data = """
3.42 6.03
6.23 8.25
4.76 1.64
4.47 4.33
3.95 7.61
8.93 2.97
9.74 4.03
1.73 1.28
9.72 5.01
7.27 3.77
""".split('\n')

print(data)

Data = [tuple(edge.split(' ')) for edge in data if edge]

print(Data)

def pointDist(a,b):
    return sum([(float(a[i])-float(b[i]))**2 for i in range(len(a))])

def dist(a,centers):
    d = {b:pointDist(a,b) for b in centers}
    dm = min(d.items(),key = lambda x:x[1])
    return dm[1]

def distortion(Data,k,centers):
    n = len(Data)
    dm =[dist(a,centers) for a in Data]
    return sum(dm)/n

print (distortion(Data, k, centers))