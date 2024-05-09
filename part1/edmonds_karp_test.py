from graph import read_file
import networkx as nx
import os, time

# run tests in part1 directory with command: `pytest -v -s .`

def run_tests(test_dir):
    for filepath in os.listdir(test_dir):
        if filepath == 'test_rl10.txt' or filepath == 'test_rd07.txt':
            continue
        g, diGraph = read_file(os.path.join(test_dir, filepath))
        start = time.time()
        max_flow = g.edmonds_karp()
        end = time.time()
        print(f"Test {filepath}: {max_flow}, time: {end - start} sec")
        assert max_flow == nx.maximum_flow_value(diGraph, 1, len(diGraph))


def test_basic_edmonds_karp():
    test_dir = os.path.join(os.path.abspath(os.getcwd()), "MaxFlow-tests/basic")
    run_tests(test_dir=test_dir)


def test_d_edmonds_karp():
    test_dir = os.path.join(os.path.abspath(os.getcwd()), "MaxFlow-tests/d")
    run_tests(test_dir=test_dir)


def test_rd_edmonds_karp():
    test_dir = os.path.join(os.path.abspath(os.getcwd()), "MaxFlow-tests/rd")
    run_tests(test_dir=test_dir)


def test_rl_edmonds_karp():
    test_dir = os.path.join(os.path.abspath(os.getcwd()), "MaxFlow-tests/rl")
    run_tests(test_dir=test_dir)
