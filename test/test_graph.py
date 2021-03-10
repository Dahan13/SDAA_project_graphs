import unittest
from graph import DirectedGraph, UndirectGraph


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = DirectedGraph()
        self.graph2 = UndirectGraph()

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


if __name__ == '__main__':
    unittest.main()
