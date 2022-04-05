import sys
import numpy as np
from copy import deepcopy

class HierarchicalClustering:
    def __init__(self):
        n, dist = self.readFromFile()
        adj, newClusters = self.clustering(n, dist)
        print('\n'.join([' '.join([str(c) for c in clusters]) for clusters in newClusters]))
        f = open('result.txt', 'w')
        f.write('\n'.join([' '.join([str(c) for c in clusters]) for clusters in newClusters]))
        f.close()
    
    def readFromFile(self):
        f = open('input.txt', 'r')
        data = f.read().strip().split('\n')
        f.close()
        n = int(data[0])
        dist = np.array([[float(v) for v in d.split()] for d in data[1:]])
        np.fill_diagonal(dist, np.inf)
        return n, dist

    def clustering(self, n, dist):
        clusters = [[i, 1] for i in range(n)]
        newClusters = []
        adj = [[] for _ in range(n)]
        while len(dist) > 1:
            node_new = len(adj)
            index = np.argmin(dist)
            i = index // len(dist)
            j = index % len(dist)
            d_new = (dist[i, :] * clusters[i][1] + dist[j, :] * clusters[j][1]) / (clusters[i][1] + clusters[j][1])
            d_new = np.delete(d_new, [i, j], 0)
            dist = np.delete(dist, [i, j], 0)
            dist = np.delete(dist, [i, j], 1)
            dist = np.insert(dist, len(dist), d_new, 0)
            d_new = np.insert(d_new, len(d_new), np.inf, 0)
            dist = np.insert(dist, len(dist)-1, d_new, 1)
            adj.append([clusters[i][0], clusters[j][0]])
            clusters.append([node_new, clusters[i][1] + clusters[j][1]])
            if i < j:
                del clusters[j]
                del clusters[i]
            else:
                del clusters[i]
                del clusters[j]
            newClusters.append(self.findLeafs(adj, node_new))
        return adj, newClusters

    def findLeafs(self, adj, v):
        leafs = []
        visited = [False for _ in range(len(adj))]
        stack = []
        stack.append(v)
        while len(stack) > 0:
            v = stack.pop()
            if 0 == len(adj[v]):
                leafs.append(v + 1)
            if not visited[v]:
                visited[v] = True
                for w in adj[v]:
                    stack.append(w)
        return leafs

if __name__ == "__main__":
    HierarchicalClustering()