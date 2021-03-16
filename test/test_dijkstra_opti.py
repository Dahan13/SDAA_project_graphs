from source import graph
import time
import graph_generation
import random as rand


def dijkstra_opti_tests(number_of_try: int) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs."""

    time_dijkstra_basic = 0
    time_dijkstra_heap = 0
    for i in range(number_of_try):
        # Generating a random graph and randomly choosing a vertex for dijkstra
        tested_graph = graph_generation.random_generation(10)
        chosen_vertex = rand.randint(0, len(tested_graph) - 1)

        # For basic version of dijkstra :
        start = time.time()
        tested_graph.dijkstra_basic_version(chosen_vertex)
        end = time.time()
        time_dijkstra_basic += end - start

        # For heap version of dijkstra :
        start = time.time()
        tested_graph.dijkstra_heap_version(chosen_vertex)
        end = time.time()
        time_dijkstra_heap += end - start
    print(f"\nPerformance report on {number_of_try} tests:\n\nBasic dijkstra ran in {time_dijkstra_basic}s.\nHeap dijkstra ran in {time_dijkstra_heap}s.")

