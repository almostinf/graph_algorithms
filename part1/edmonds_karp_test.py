from graph import Graph
import networkx as nx

def test_edmonds_karp():
    # Test case 1: Basic flow network
    net1 = nx.DiGraph()
    net1.add_edge(1, 2, capacity=40)
    net1.add_edge(1, 4, capacity=20)
    net1.add_edge(2, 3, capacity=30)
    net1.add_edge(2, 4, capacity=20)
    net1.add_edge(3, 4, capacity=10)

    net_copy = net1.copy()
    g1 = Graph(net1, 1, 4)
    assert g1.edmonds_karp() == nx.maximum_flow_value(net_copy, 1, 4)

    # Test case 2: Source and sink are the same
    net2 = nx.DiGraph()
    net2.add_edge(1, 1, capacity=100)  # Self-loop
    g2 = Graph(net2, 1, 1)
    assert g2.edmonds_karp() == 0  # Maximum flow should be 0

    # Test case 3: Disconnected graph
    net3 = nx.DiGraph()
    net3.add_edge(1, 2, capacity=10)
    net3.add_edge(3, 4, capacity=20)
    g3 = Graph(net3, 1, 4)
    assert g3.edmonds_karp() == 0  # Maximum flow should be 0

    # Test case 4: No path from source to sink
    net4 = nx.DiGraph()
    net4.add_edge(1, 2, capacity=10)
    net4.add_edge(3, 4, capacity=20)
    g4 = Graph(net4, 1, 5)  # Sink node does not exist in the graph
    assert g4.edmonds_karp() == 0  # Maximum flow should be 0
