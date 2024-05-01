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
