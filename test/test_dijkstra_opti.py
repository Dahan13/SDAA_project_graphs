from graph import *
import time

used_graph = DirectedGraph()
used_graph.add_edge(1, 4, 6)
used_graph.add_edge(2, 1, 1)
used_graph.add_edge(2, 4, 2)
used_graph.add_edge(3, 1, 1)
used_graph.add_edge(3, 2, 3)
used_graph.add_edge(4, 3, 1)


def dijkstra_opti_tests(number_of_try: int):
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


dijkstra_opti_tests(100000)
