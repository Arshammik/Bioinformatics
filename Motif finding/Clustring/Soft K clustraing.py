import sys
from math import *
import numpy as np
from copy import deepcopy

class SoftClustering:
    def __init__(self):
        data, k, stiffness = self.readFromFile()
        centers = self.findCenters(data, k, stiffness)
        self.saveResult(centers)

    def readFromFile(self):
        f = open('input.txt', 'r')
        raw = f.read().strip().split()
        f.close()
        k, m, stiffness = int(raw[0]), int(raw[1]), float(raw[2])
        raw = raw[3:]
        data = np.zeros((len(raw)//m, m))
        for i in range(len(raw)//m):
            data[i, ] = [float(d) for d in raw[i*m:(i+1)*m]]
        return data, k, stiffness

    def getDist(self, p1, p2):
        # calculate the distance between two points
        return sqrt(sum((p1-p2)**2))

    def findCenters(self, data, k, stiffness, MAXITER = 100):
        n, m = data.shape
        centers = data[:k, ]
        hiddenMatrix = np.zeros((k, n))
        for _ in range(MAXITER):
            # Centers to Soft Clusters (E-step)
            for i in range(k):
                for j in range(n):
                    hiddenMatrix[i, j] = np.exp(-stiffness*self.getDist(data[j, :], centers[i, :]))
            for j in range(n):
                hiddenMatrix[:, j] /= sum(hiddenMatrix[:, j])
            # Soft Clusters to Centers (M-step)
            centers = np.dot(hiddenMatrix, data)
            for i in range(k):
                centers[i, ] /= sum(hiddenMatrix[i, ])
        return centers

    def saveResult(self, centers):
        k = centers.shape[0]
        f = open('result.txt', 'w')
        for i in range(k):
            print(' '.join([str(p) for p in centers[i, ]]))
            f.write(' '.join([str(p) for p in centers[i, ]]) + '\n')
        f.close()      

if __name__ == '__main__':
    SoftClustering()