from collections import deque

def bfs(self) -> int:
    parents = {}
    parents[self.source] = None
    q = deque([self.source])
    min_cap = {self.source: float('inf')}
    flow = 0

    while q:
        cur = q.popleft()
        cur_cap = min_cap[cur]
        for neighbor, neighbor_cap in self.net[cur].items():
            if neighbor_cap['capacity'] > 0 and neighbor not in parents:
                min_cap[neighbor] = min(cur_cap, neighbor_cap['capacity'])
                parents[neighbor] = cur
                if neighbor == self.sink:
                    flow = min(cur_cap, neighbor_cap['capacity'])
                    break
                q.append(neighbor)

    if flow > 0:
        cur = self.sink
        while cur != self.source:
            if cur in parents:
                parent = parents[cur]
                if parent in self.net and cur in self.net[parent]:
                    self.net[parent][cur]['capacity'] -= flow
                else:
                    if parent not in self.net:
                        self.net[parent] = {}
                    self.net[parent][cur] = {'capacity': -flow}
                
                if cur in self.net and parent in self.net[cur]:
                    self.net[cur][parent]['capacity'] += flow
                else:
                    if cur not in self.net:
                        self.net[cur] = {}
                    self.net[cur][parent] = {'capacity': flow}
                
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
