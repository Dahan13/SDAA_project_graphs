from typing import Dict, Any, List
import copy


class DirectedGraph:
    def __init__(self, edges=None) -> None:
        if edges is None:
            edges = {}
        self.edges = edges

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, edges):
        if isinstance(edges, dict):
            for edge in edges:
                for voisin in edge:
                    if edge[voisin] <= 0 and not isinstance(edge, dict):
                        raise ValueError
            self.__edges = edges
        else:
            raise ValueError

    @property
    def vertices(self):
        return [element for element in self.edges.keys()]

    def add_vertex(self, vertex: Any) -> None:
        self.edges[vertex] = {}

    def remove_vertex(self, vertex: Any) -> None:
        del self.edges[vertex]
        for edge in self.edges:
            self.edges[edge].pop(vertex, None)

    def add_edge(self, vertex1: Any, vertex2: Any, weight: int) -> None:
        if vertex1 not in self.edges.keys():
            self.add_vertex(vertex1)
        if vertex2 not in self.edges.keys() :
            self.add_vertex(vertex2)
        self.edges[vertex1][vertex2] = weight

    def remove_edge(self, vertex1: Any, vertex2: Any) -> None:
        del self.edges[vertex1][vertex2]

    def change_weight(self, vertex1: Any, vertex2: Any, weight: int) -> None:
        self.edges[vertex1][vertex2] = weight

    @classmethod
    def reset(cls) -> None:
        cls.edges = {}

    def induced_subgraph(self, vertices_subset: List[int]) -> 'DirectedGraph':
        induced_subgraph = DirectedGraph(self.edges)
        keys = induced_subgraph.edges.keys()
        for key in keys:
            if key not in vertices_subset:
                induced_subgraph.remove_vertex(key)
        return induced_subgraph

    def __len__(self) -> int:
        return len(self.vertices)

    def __getitem__(self, item: Any) -> dict:
        return self.edges[item]

    def __iter__(self) -> 'DirectedGraph':
        self.iterate = 0
        return self

    def __next__(self) -> None:
        if self.iterate < len(self.vertices):
            result = self.vertices[self.iterate]
            self.iterate += 1
            return result
        else:
            raise StopIteration

    def __str__(self) -> str:
        return str(self.edges)



