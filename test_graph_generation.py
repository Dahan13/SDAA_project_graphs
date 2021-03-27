import unittest
from graph_generation import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.graph_0 = grp.UndirectedGraph()
        self.graph_1 = grp.UndirectedGraph({0: {}})
        self.graph_2 = grp.UndirectedGraph({0: {1: 1}, 1: {0: 1}})

    def test_minimal_case(self):
        graph = generate_random_graph(0, 0)
        assert graph == self.graph_0

    def test_minimal_case_2(self):
        graph = generate_random_graph(1, 0)
        assert graph == self.graph_1

    def test_minimal_case_3(self):
        graph = generate_random_graph(2, 1)
        assert graph == self.graph_2

    def test_node_number(self):
        graph = generate_random_graph(5, 8)
        assert len(graph.edges) == 5
        assert len(self.graph_0.edges) == 0
        assert len(self.graph_1.edges) == 1
        assert len(self.graph_2.edges) == 2

    def test_edge_number_undirected(self):
        graph = generate_random_graph(5, 8)
        done = []
        for node in graph.edges:
            for edge in graph.edges[node]:
                if (node, edge) not in done and (edge, node) not in done:
                    done.append((node, edge))
        assert len(done) == 8

    def test_edge_number_directed(self):
        print("here")
        graph = generate_random_graph(5, 8, directed=True)
        print(graph)
        sum = 0
        for node in graph.edges:
            sum += len(graph.edges[node])
        assert sum == 8


if __name__ == '__main__':
    unittest.main()
