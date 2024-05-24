def FIFOPushRelabel(self) -> int:
    queue = []
    e = [0] * (self.sink + 1)
    h = [0] * (self.sink + 1)
    inQueue = [False] * (self.sink + 1)
    h[self.source] = self.sink
    graph = {v: {u: {'capacity': self.net[v][u]['capacity']} for u in self.net[v]} for v in self.net}
    # graph = {v: copy.deepcopy(self.net[v]) for v in self.net} # медленнее справляется будто
    # graph = self.net.copy() # --> не работает приходится как выше делать
    source = self.source
    sink = self.sink
    for v in graph[source]:
        if graph[source][v]['capacity'] != 0:
            graph[source][v]['capacity'] = 0
            graph[v][source] = {'capacity': self.net[source][v]['capacity']}
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
    if e[u] == 0:
        return
     
    for v in graph[u]:
        if graph[u][v]['capacity'] > 0 and h[v] < h[u]:
            f = min(e[u], graph[u][v]['capacity'])

            graph[u][v]['capacity'] -= f
            if u not in graph[v]:
                graph[v][u] = {'capacity': f}
            else:
                graph[v][u]['capacity'] += f

            e[u] -= f
            e[v] += f

            if not in_queue[v] and v != source and v != sink:
                queue.append(v)
                in_queue[v] = True

    if e[u] != 0:
        queue.append(u)
        in_queue[u] = True
