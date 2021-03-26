from typing import Dict, Any, List
import math
import heapq

class DirectedGraph:
    """oriented graph coded as a dict of dict"""

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
                for voisin in edges[edge]:
                    if edges[edge][voisin] <= 0 and not isinstance(edges[edge], dict):
                        raise ValueError
            self.__edges = edges
        else:
            raise ValueError

    @property
    def vertices(self) -> List:
        return [element for element in self.edges.keys()]

    def add_vertex(self, vertex: Any) -> None:
        self.edges[vertex] = {}

    def remove_vertex(self, vertex: Any) -> None:
        del self.edges[vertex]
        for edge in self.edges:
            self.edges[edge].pop(vertex, None)

    def add_edge(self, vertex1: Any, vertex2: Any, weight: int = 1, checker: bool = False) -> bool:
        if vertex1 not in self.edges.keys():
            self.add_vertex(vertex1)
        if vertex2 not in self.edges.keys():
            self.add_vertex(vertex2)
        if checker:
            if vertex2 in self.edges[vertex1]:
                return False
            else:
                self.edges[vertex1][vertex2] = weight
                return True
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

    def __ne__(self, other: 'DirectedGraph') -> bool:
        return self.edges != other.edges

    def __eq__(self, other) -> bool:
        return self.edges == other.edges

    def dijkstra_basic_version(self, chosen_vertex: Any) -> dict:
        # Initializing values
        dist = {}
        pred = {}
        vertices_fighting = []
        for vertex in self.vertices:
            vertices_fighting.append(vertex)
            dist[vertex] = math.inf
            pred[vertex] = None
        dist[chosen_vertex] = 0

        # Beginning study
        while len(vertices_fighting):  # While studied graph is not empty

            # Return key with lowest value
            better_dist = math.inf
            nearest_vertex = vertices_fighting[0]  # Failsafe, in case the graph is made of one node only without edges.
            for vertex in vertices_fighting:
                if dist[vertex] < better_dist:
                    better_dist = dist[vertex]
                    nearest_vertex = vertex
            vertices_fighting.remove(nearest_vertex)
            # Actually we can't use min method because it may return the key of an already deleted vertex

            # Make a copy of edges related to nearest_vertex to avoid repetition
            nearest_vertex_infos = self.edges[nearest_vertex]
            for vertex in nearest_vertex_infos:
                new_dist = dist[nearest_vertex] + nearest_vertex_infos[vertex]
                if dist[vertex] > new_dist:
                    
                    dist[vertex] = new_dist
                    pred[vertex] = nearest_vertex
        return dist

    def dijkstra_heap_version(self, chosen_vertex: Any, target_vertex: Any) -> dict:
        # Initializing values
        dist = {vertex: math.inf for vertex in self.vertices}
        pred = {vertex: None for vertex in self.vertices}
        vertices_fighting = {vertex: True for vertex in self.vertices}
        dist[chosen_vertex] = 0
        vertices_heap = []
        heapq.heappush(vertices_heap, (0, chosen_vertex))
        # Beginning study
        while len(vertices_heap):  # While studied graph is not empty

            # Return key with lowest value
            nearest_dist, nearest_vertex = heapq.heappop(vertices_heap)
            if vertices_fighting[nearest_vertex]:
                vertices_fighting[nearest_vertex] = False

                # Stop the function in case we found the targeted vertex
                if nearest_vertex == target_vertex:
                    return dist[nearest_vertex]

                # Make a copy of edges related to nearest_vertex to avoid repetition
                nearest_vertex_infos = self.edges[nearest_vertex]
                for vertex in nearest_vertex_infos:
                    new_dist = nearest_dist + nearest_vertex_infos[vertex]
                    if vertices_fighting[vertex] and dist[vertex] > new_dist:
                        dist[vertex] = new_dist
                        pred[vertex] = nearest_vertex
                        heapq.heappush(vertices_heap, (new_dist, vertex))
        return dist
class UndirectedGraph(DirectedGraph):
    """non oriented graph coded as a dict of dict"""

    def __init__(self, edges=None) -> None:
        super().__init__(edges)
        for vertice in self.vertices:
            for target in self.edges[vertice].keys():
                if vertice not in self.edges[target].keys():
                    raise ValueError
                if self.edges[target][vertice] != self.edges[vertice][target]:
                    raise ValueError

    def add_edge(self, vertex1: Any, vertex2: Any, weight: int = 1, checker: bool = False) -> bool:
        if vertex1 not in self.edges.keys():
            self.add_vertex(vertex1)
        if vertex2 not in self.edges.keys():
            self.add_vertex(vertex2)
        if checker:
            if vertex2 in self.edges[vertex1] and vertex1 in self.edges[vertex2]:
                return False
            else:
                self.edges[vertex1][vertex2] = weight
                self.edges[vertex2][vertex1] = weight
                return True
        self.edges[vertex1][vertex2] = weight
        self.edges[vertex2][vertex1] = weight

    def remove_edge(self, vertex1: Any, vertex2: Any) -> None:
        del self.edges[vertex1][vertex2]
        del self.edges[vertex2][vertex1]
