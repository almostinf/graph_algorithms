from graph_algorithms.part1.graph import Graph
import networkx as nx

def FIFOPushRelabel(self: Graph) -> int:
    queue = []
    e = [0] * (self.net.number_of_nodes() + 1)
    h = [0] * (self.net.number_of_nodes() + 1)
    inQueue = [False] * (self.net.number_of_nodes() + 1)
    h[self.source] = self.net.number_of_nodes()
    graph = self.net.copy()
    init_graph(graph)
    source = self.source
    sink = self.sink
    for v in list(graph[source].keys()):
        if(graph[source][v]['capacity'] != 0):
            graph[source][v]['capacity'] = 0
            graph[v][source]['capacity'] = self.net[source][v]['capacity']
            e[v] = graph[v][source]['capacity']
            if v != self.sink:
                queue.append(v)
                inQueue[v] = True
    while queue:
        u = queue.pop(0)
        inQueue[u] = False
        relabel(graph, u, h)
        push(graph, u, e, h, queue, inQueue, source, sink)
    return e[self.sink]

def relabel(graph: nx.DiGraph , u, h):
    minHeight = float("inf")
    for v in list(graph[u].keys()):
        if graph[u][v]['capacity']> 0:
            minHeight = min(minHeight, h[v])
            h[u] = minHeight + 1

def push(graph: nx.DiGraph, u, e, h, queue, in_queue, source, sink):
    for v in list(graph[u].keys()):
        if e[u] == 0:
            break

        if graph[u][v]['capacity'] > 0 and h[v] < h[u]:
            f = min(e[u], graph[u][v]['capacity'])

            graph[u][v]['capacity'] -= f
            graph[v][u]['capacity'] += f

            e[u] -= f
            e[v] += f

            if not in_queue[v] and v != source and v != sink:
                queue.append(v)
                in_queue[v] = True

    if e[u] != 0:
        queue.append(u)
        in_queue[u] = True

def init_graph(graph: nx.DiGraph):
    for edge in graph.edges:
        if not graph.has_edge(edge[1],edge[0]):
            graph.add_edge(edge[1],edge[0], capacity=0)