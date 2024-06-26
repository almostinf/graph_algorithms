import networkx as nx
from edmonds_karp import bfs, edmonds_karp
from PushRelabelFIFO import FIFOPushRelabel

class Graph:
    def __init__(self, net: dict, source, sink):
        self.net = net
        self.source = source
        self.sink = sink

    def bfs(self):
        return bfs(self)

    def edmonds_karp(self):
        return edmonds_karp(self)
    
    def FIFOPushRelabel(self):
        return FIFOPushRelabel(self)


def read_file(path: str):
    with open(path, 'r') as file:
        data = file.read()
        data = data.split('\n')
        _, num_edges = map(int, data[0].split(' '))
        net = {}
        diGraph = nx.DiGraph()

        for i in range(1, num_edges + 1):
            edge = data[i].split(' ')
            v, u, cap = int(edge[0]), int(edge[1]), float(edge[2])
            if v not in net:
                net[v] = {}
            if u not in net:
                net[u] = {}
            net[v][u] = {'capacity': cap}

            diGraph.add_node(v)
            diGraph.add_node(u)
            diGraph.add_edge(v, u, capacity=cap)
        
        return Graph(net, 1, len(net)), diGraph