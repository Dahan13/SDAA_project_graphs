import unittest
from source import graph as grp
import graph_generation as randgraph


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = grp.DirectedGraph()
        self.graph2 = grp.UndirectedGraph()
        self.graph_0 = grp.UndirectedGraph()
        self.graph_1 = grp.UndirectedGraph({0: {}})
        self.graph_2 = grp.UndirectedGraph({0: {1: 1}, 1: {0: 1}})

    def test_add_vertex_dir(self):
        self.graph.add_vertex("banane")
        assert len(self.graph) == 1

    def test_add_edge_dir(self):
        self.graph.add_edge("banane", 2, 3)
        assert len(self.graph) == 2
        self.graph.add_edge(2, "banane", 1)
        assert self.graph.edges[2] == {"banane": 1}
        self.graph.add_edge(2, 3, 1)
        assert len(self.graph) == 3
        assert self.graph.edges[2] == {"banane": 1, 3: 1}

    def test_remove_edge_dir(self):
        self.graph.add_edge(2, "banane", 1)
        self.graph.add_edge(2, 3, 1)
        self.graph.remove_edge(2, 3)
        assert self.graph.edges[2] == {"banane": 1}

    def test_indent_dir(self):
        self.graph.add_edge(2, "banane", 1)
        self.graph.add_edge(2, 3, 1)
        i = 0
        for vertex in self.graph:
            assert vertex == self.graph.vertices[i]
            i += 1

    def test_remove_vertex_dir(self):
        self.graph.add_edge(2, "banane", 1)
        self.graph.add_edge(2, 3, 1)
        self.graph.remove_vertex("banane")
        assert len(self.graph) == 2
        assert self.graph.edges[2] == {3: 1}

    def test_add_edge_undir(self):
        self.graph2.add_edge("banane", 2, 3)
        assert len(self.graph2) == 2
        self.graph2.add_edge(2, "banane", 1)
        assert self.graph2.edges[2] == {"banane": 1}
        assert self.graph2.edges["banane"] == {2: 1}
        self.graph2.add_edge(2, 3, 1)
        assert len(self.graph2) == 3
        assert self.graph2.edges[2] == {"banane": 1, 3: 1}
        assert self.graph2.edges[3] == {2: 1}

    def test_remove_edge_undir(self):
        self.graph2.add_edge(2, "banane", 1)
        self.graph2.add_edge(2, 3, 1)
        self.graph2.remove_edge(2, 3)
        assert self.graph2.edges[2] == {"banane": 1}
        assert self.graph2.edges[3] == {}

    def test_eq(self):
        assert self.graph == self.graph_0

    def test_eq2(self):
        graph1 = grp.DirectedGraph({0: {}})
        assert graph1 == self.graph_1

    def test_gen_and_eq(self):
        graph = grp.DirectedGraph({0: {1: 1}, 1: {0: 1}})
        assert graph == self.graph_2

    def test_dijckstra(self):
        for i in range(10):
            used_graph = randgraph.random_generation(10)
            basic = used_graph.dijkstra_basic_version(1)
            heap = used_graph.dijkstra_heap_version(1)
            for vertex in used_graph.edges.keys():  # Checking values
                assert basic[vertex] == heap[vertex]


if __name__ == '__main__':
    unittest.main()
