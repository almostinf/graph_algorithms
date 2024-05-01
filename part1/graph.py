import networkx as nx
from edmonds_karp import bfs, edmonds_karp

class Graph:
    def __init__(self, net: nx.DiGraph, source, sink):
        self.net = net
        self.source = source
        self.sink = sink

    def bfs(self):
        return bfs(self)

    def edmonds_karp(self):
        return edmonds_karp(self)

def read_file(path: str) -> Graph:
    with open(path, 'r') as file:
        data = file.read()
        data = data.split('\n')
        _, num_edges = map(int, data[0].split(' '))
        net = nx.DiGraph()

        for i in range(1, num_edges + 1):
            edge = data[i].split(' ')
            v, u, cap = int(edge[0]), int(edge[1]), float(edge[2])
            net.add_node(v)
            net.add_node(u)
            net.add_edge(v, u, capacity=cap)
        
        return Graph(net, 1, len(net))
