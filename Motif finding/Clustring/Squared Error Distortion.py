import sys
from math import *
import numpy as np

def readFromFile():
    f = open('input.txt', 'r')
    raw = [d.split() for d in f.read().strip().split('--------')]
    k, m = int(raw[0][0]), int(raw[0][1])
    centers = np.zeros((k, m))
    for i in range(k):
        centers[i, ] = [float(d) for d in raw[0][2+i*m:2+(i+1)*m]]
    n = len(raw[1])//m
    data = np.zeros((n, m))
    for i in range(n):
        data[i, ] = [float(d) for d in raw[1][i*m:(i+1)*m]]
    return data, centers

def getSquaredDist(p1, p2):
    return sum((p1-p2)**2)

def calDistortion(data, centers):
    n, m = data.shape
    k = centers.shape[0]
    distortion = sum([min([getSquaredDist(data[i, ], centers[j, ]) for j in range(k)]) for i in range(n)])/n
    return distortion

def solve():
    data, centers = readFromFile()
    distortion = calDistortion(data, centers)
    print(distortion)

if __name__ == '__main__':
    solve()