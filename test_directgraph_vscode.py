from typing import no_type_check, Any, Dict
from  source.directgraph import DirectedGraph
import time

def test_graph():
    graph = DirectedGraph()
    graph.add_vertex(1)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 1, 1)
    graph.add_edge(2, 3, 1)

    print("vertice\n", graph.vertices)
    print("len Graph\n", len(graph))
    print("Graph[2]\n", graph[2])
    print("Graph\n", graph)
    print("Vertex\n")
    for vertex in graph:
       print(vertex)
    graph.remove_edge(1, 2)
    print(graph.dijkstra_heap_version(2))


used_graph = DirectedGraph()
used_graph.add_edge(1, 4, 6)
used_graph.add_edge(2, 1, 1)
used_graph.add_edge(2, 4, 2)
used_graph.add_edge(3, 1, 1)
used_graph.add_edge(3, 2, 3)
used_graph.add_edge(4, 3, 1)


def dijkstra_output_comparison() :

    """ Will ensure each dijkstra algorithm give the same dict (Will be overhauled once random directed graph will be implemented)"""

    basic = used_graph.dijkstra_basic_version(1)
    heap = used_graph.dijkstra_heap_version(1)
    for vertex in used_graph.edges.keys() : # Checking values
        assert basic[vertex] == heap[vertex]
    print("\nAll dijkstra algorithm gave same output !")


def dijkstra_opti_tests(number_of_try : int):

    """ Will do some tests to ensure which algorithm is better optimized ! (Will be overhauled once random directed graph will be implemented) """

    chosen_vertex = 2

    # For basic version of dijkstra :
    print("Testing basic dijkstra !")
    start = time.time()
    for i in range(number_of_try):
        used_graph.dijkstra_basic_version(chosen_vertex)
    end = time.time()
    time_dijkstra_basic = end - start

    # For heap version of dijkstra :
    print("Testing heap dijkstra !")
    start = time.time()
    for i in range(number_of_try):
        used_graph.dijkstra_heap_version(chosen_vertex)
    end = time.time()
    time_dijkstra_heap = end - start
    print(f"\nPerformance report on {number_of_try} tests:\n\nBasic dijkstra ran in {time_dijkstra_basic}s.\nHeap dijkstra ran in {time_dijkstra_heap}s.")

# dijkstra_opti_tests(1000)
# test_graph()
# dijkstra_output_comparison()