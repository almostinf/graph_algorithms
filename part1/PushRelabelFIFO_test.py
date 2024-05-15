from graph import read_file
import networkx as nx
import os, time
import PushRelabelFIFO

# run tests in part1 directory with command: `pytest -v -s .`

def run_tests(test_dir):
    for filepath in os.listdir(test_dir):
        if filepath == 'test_rl10.txt' or filepath == 'test_rd07.txt':
            continue
        g, lib_graph = read_file(os.path.join(test_dir, filepath))
        start = time.time()
        max_flow = g.FIFOPushRelabel()
        end = time.time()
        print(f"Test {filepath}: {max_flow}, time: {end - start} sec")
        assert max_flow == nx.maximum_flow_value(lib_graph, 1, len(lib_graph))

def test_basic_push_relabel():
    test_dir = os.path.join(os.path.abspath(os.getcwd()), "MaxFlow-tests/basic")
    run_tests(test_dir=test_dir)


def test_d_push_relabel():
    test_dir = os.path.join(os.path.abspath(os.getcwd()), "MaxFlow-tests/d")
    run_tests(test_dir=test_dir)


def test_rd_push_relabel():
    test_dir = os.path.join(os.path.abspath(os.getcwd()), "MaxFlow-tests/rd")
    run_tests(test_dir=test_dir)


def test_rl_push_relabel():
    test_dir = os.path.join(os.path.abspath(os.getcwd()), "MaxFlow-tests/rl")
    run_tests(test_dir=test_dir)