# import copy
def FIFOPushRelabel(self) -> int:
    queue = []
    e = [0] * (len(self.net) + 1)
    h = [0] * (len(self.net) + 1)
    inQueue = [False] * (len(self.net) + 1)
    h[self.source] = len(self.net)
    graph = {v: {u: {'capacity': self.net[v][u]['capacity']} for u in self.net[v]} for v in self.net}
    # graph = {v: copy.deepcopy(self.net[v]) for v in self.net} # медленнее справляется будто
    # graph = self.net.copy() # --> не работает приходится как выше делать
    init_graph(graph)
    source = self.source
    sink = self.sink
    for v in graph[source]:
        if graph[source][v]['capacity'] != 0:
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

def relabel(graph, u, h):
    minHeight = float("inf")
    for v in graph[u]:
        if graph[u][v]['capacity'] > 0:
            minHeight = min(minHeight, h[v])
            h[u] = minHeight + 1

def push(graph, u, e, h, queue, in_queue, source, sink):
    for v in graph[u]:
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

def init_graph(graph):
    for v in graph:
        for u in graph[v]:
            if u not in graph or v not in graph[u]:
                graph[u][v] = {'capacity': 0}