import queue

def bfs(self) -> int:
    parents = {}
    parents[self.source] = None
    q = queue.Queue()
    q.put(self.source)
    min_cap = queue.Queue()
    min_cap.put(float('inf'))
    flow = 0

    while not q.empty():
        cur = q.get()
        cur_cap = min_cap.get()

        for neighbor in list(self.net[cur].keys()):
            neighbor_cap = self.net[cur][neighbor]['capacity']
            if neighbor_cap > 0 and neighbor not in parents:
                q.put(neighbor)
                min_cap.put(min(cur_cap, neighbor_cap))
                parents[neighbor] = cur
                if neighbor == self.sink:
                    flow = min(cur_cap, neighbor_cap)
                    break

    if flow > 0:
        cur = self.sink
        while cur != self.source:
            if cur in parents:
                parent = parents[cur]
                if self.net.has_edge(parent, cur):
                    self.net[parent][cur]['capacity'] -= flow
                else:
                    self.net.add_edge(parent, cur, capacity=-flow)
                
                if self.net.has_edge(cur, parent):
                    self.net[cur][parent]['capacity'] += flow
                else:
                    self.net.add_edge(cur, parent, capacity=-flow)
                
                cur = parent

    return flow


def edmonds_karp(self) -> int:
    max_flow = 0
    while True:
        cur_flow = self.bfs()
        if cur_flow == 0:
            break
        max_flow += cur_flow
    return max_flow
