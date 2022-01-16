### constructing distance matrix and philogenic tree utilizing neighbor joining algorithm
import sys
import numpy as np


class NeighborJoining:
    def __init__(self):
        n, disMatrix = self.readFromFile()
        adj = self.runNeighborJoining(disMatrix, n)
        self.printGraph(adj)
        self.saveResult(adj)

    def _input(self):
        data = sys.stdin.read().strip().split('\n')
        n = int(data[0])
        distanceMatrix = [[0] * n for _ in range(n)]
        for i in range(n):
            d = data[i + 1].split()
            for k in range(n):
                distanceMatrix[i][k] = int(d[k])
        return n, distanceMatrix

    def readFromFile(self):
        f = open('dataset_10333_7-2.txt', 'r')
        data = []
        for line in f:
            data.append(line.strip())
        n = int(data[0])
        distMatrix = [[0] * n for _ in range(n)]
        for i in range(n):
            d = data[i + 1].split()
            for k in range(n):
                distMatrix[i][k] = int(d[k])
        return n, distMatrix

    def saveResult(self, adj):
        f = open('result.txt', 'w')
        for i, nodes in enumerate(adj):
            for d, w in nodes:
                f.write(str(i) + '->' + str(d) + ':' + '%0.3f' % w + '\n')

    def printDistMatrix(self, distanceMatrix):
        for d in distanceMatrix:
            print(' '.join([str(i) for i in d]))

    def printGraph(self, adj):
        for i, nodes in enumerate(adj):
            for d, w in nodes:
                print(str(i) + '->' + str(d) + ':' + '%0.3f' % w)

    def runNeighborJoining(self, distanceMatrix, n):
        D = np.array(distanceMatrix, dtype=float)
        clusters = [i for i in range(n)]
        adj = [[] for i in range(n)]
        if len(D) <= 1:
            return adj
        while True:
            if 2 == n:
                adj[len(adj) - 1].append((len(adj) - 2, D[0][1]))
                adj[len(adj) - 2].append((len(adj) - 1, D[0][1]))
                break
            totalDist = np.sum(D, axis=0)
            D1 = (n - 2) * D
            D1 = D1 - totalDist
            D1 = D1 - totalDist.reshape((n, 1))
            np.fill_diagonal(D1, 0.)
            # print(D1)
            index = np.argmin(D1)
            i = index // n
            j = index % n
            delta = (totalDist[i] - totalDist[j]) / (n - 2)
            li = (D[i, j] + delta) / 2
            lj = (D[i, j] - delta) / 2
            d_new = (D[i, :] + D[j, :] - D[i, j]) / 2
            D = np.insert(D, n, d_new, axis=0)
            d_new = np.insert(d_new, n, 0., axis=0)
            D = np.insert(D, n, d_new, axis=1)
            D = np.delete(D, [i, j], 0)
            D = np.delete(D, [i, j], 1)
            # print(D)

            m = len(adj)
            adj.append([])
            adj[m].append((clusters[i], li))
            adj[clusters[i]].append((m, li))
            adj[m].append((clusters[j], lj))
            adj[clusters[j]].append((m, lj))
            if i < j:
                del clusters[j]
                del clusters[i]
            else:
                del clusters[i]
                del clusters[j]
            clusters.append(m)

            n -= 1

        return adj


if __name__ == "__main__":
    NeighborJoining()