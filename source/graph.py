from typing import Dict, Any, List
import copy
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
        for vertex in self:
            dist[vertex] = math.inf
            pred[vertex] = None
        dist[chosen_vertex] = 0

        # Beginning study
        studied_graph = copy.deepcopy(self)
        while len(studied_graph.edges) != 0:  # While studied graph is not empty

            # Return key with lowest value
            better_dist = math.inf
            nearest_vertex = studied_graph.vertices[0]  # Failsafe, in case the graph is made of one node only without edges.
            for vertex in studied_graph:
                if dist[vertex] < better_dist:
                    better_dist = dist[vertex]
                    nearest_vertex = vertex
            # Actually we can't use min method because it may return the key of an already deleted vertex

            # Make a copy of nearest_vertex related infos since we will delete it right away
            nearest_vertex_infos = [(value, key) for key, value in studied_graph[nearest_vertex].items()]
            studied_graph.remove_vertex(nearest_vertex)
            for vertex in nearest_vertex_infos:
                if dist[vertex[1]] > dist[nearest_vertex] + vertex[0]:
                    dist[vertex[1]] = dist[nearest_vertex] + vertex[0]
                    pred[vertex[1]] = nearest_vertex
        return dist

    def dijkstra_heap_version(self, chosen_vertex: Any) -> dict:
        # Initializing values
        dist = {}  # Only used for final output
        queue = []  # Items in queue will have following structure : [distance, predecessor, vertex key]
        for vertex in self:
            if vertex == chosen_vertex:
                heapq.heappush(queue, [0, None, vertex])
            else:
                heapq.heappush(queue, [math.inf, None, vertex])

        # Beginning study
        while queue != []:  # While main queue is not empty

            # Return info of vertex with lowest distancen heap type use allowed for great complexity reduction
            nearest_vertex = heapq.heappop(queue)
            dist[nearest_vertex[2]] = nearest_vertex[0]
            # nearest_vertex is not explicitely deleted, but we won't push it into the queue so it's the same

            # Handling datas
            queue2 = []  # queue2 is for temp storage
            for i in range(len(queue)):
                current_item = heapq.heappop(queue)
                # Check conditions
                if current_item[2] in self.edges[nearest_vertex[2]].keys() and current_item[0] > nearest_vertex[0] + self.edges[nearest_vertex[2]][current_item[2]]:
                    current_item[0] = nearest_vertex[0] + self.edges[nearest_vertex[2]][current_item[2]]
                    current_item[1] = nearest_vertex[2]
                # Pushing new vertex infos on temp queue
                heapq.heappush(queue2, current_item)
            # Pouring everything into my main queue, note that nearest_vertex infos are no longer in it !
            queue = queue2  # No need to use deepcopy here, it will make the function globally 2 times faster.
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
