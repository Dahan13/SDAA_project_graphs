import time
import random as rand
import matplotlib.pyplot as plt
import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import graph_generation


def progressBar(current, total, barLength=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * barLength - 1) + '>'
    spaces = ' ' * (barLength - len(arrow))

    print('Progress: [%s%s] %d %%\n' % (arrow, spaces, percent), end='\r')


def dijkstra_opti_tests(number_of_try: int) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs."""

    time_dijkstra_basic = 0
    time_dijkstra_basic_array = []
    time_dijkstra_heap = 0
    time_dijkstra_heap_array = []
    n_array = []
    for i in range(number_of_try):
        progressBar(i, number_of_try)
        n_array.append(i)
        # Generating a random graph and randomly choosing a vertex for dijkstra
        tested_graph = graph_generation.random_generation(10)
        chosen_vertex = rand.randint(0, len(tested_graph) - 1)

        # For basic version of dijkstra :
        start = time.process_time()
        tested_graph.dijkstra_basic_version(chosen_vertex)
        end = time.process_time()
        time_dijkstra_basic += end - start
        time_dijkstra_basic_array.append(time_dijkstra_basic)

        # For heap version of dijkstra :
        start = time.process_time()
        tested_graph.dijkstra_heap_version(chosen_vertex)
        end = time.process_time()
        time_dijkstra_heap += end - start
        time_dijkstra_heap_array.append(time_dijkstra_heap)

        # ploting
    plt.plot(n_array, time_dijkstra_basic_array, label="basic")
    plt.plot(n_array, time_dijkstra_heap_array, label="heap")
    plt.xlabel('Tries number')
    plt.ylabel('Cumulated time (in seconds)')
    plt.title(f'Testing time with multiple tries')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(f"../log/test_{number_of_try}_tries.png")
    plt.close()


def dijkstra_opti_tests_2(number_of_node: int) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs."""

    time_dijkstra_basic = 0
    time_dijkstra_basic_array = []
    time_dijkstra_heap = 0
    time_dijkstra_heap_array = []
    n_array = []
    alpha = rand.random()
    alpha = round(alpha, 3)
    while 5 > alpha * (5 * 4) // 2:
        alpha = round(rand.random(), 3)
    # Choosing alpha :
    for i in range(number_of_node):
        progressBar(i, number_of_node)

        n_array.append(i)
        tested_graph = graph_generation.generate_random_graph(i, round(alpha * (i * (i - 1) // 2)))
        # Generating a random graph and randomly choosing a vertex for dijkstra
        chosen_vertex = rand.randint(0, len(tested_graph))

        # For basic version of dijkstra :
        start = time.process_time()
        tested_graph.dijkstra_basic_version(chosen_vertex)
        end = time.process_time()
        time_dijkstra_basic = end - start
        time_dijkstra_basic_array.append(time_dijkstra_basic)

        # For heap version of dijkstra :
        start = time.process_time()
        tested_graph.dijkstra_heap_version(chosen_vertex)
        end = time.process_time()
        time_dijkstra_heap = end - start
        time_dijkstra_heap_array.append(time_dijkstra_heap)

        # ploting
    plt.plot(n_array, time_dijkstra_basic_array, label='basic')
    plt.plot(n_array, time_dijkstra_heap_array, label='heap')
    plt.xlabel('Node number')
    plt.ylabel('Cumulated time (in seconds)')
    plt.title(f'For alpha = {alpha}')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(f"../log/test_alpha_{alpha}_nodes_{number_of_node}.png")
    plt.close()


def dijkstra_opti_tests_3(number_of_node: int) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs."""

    time_dijkstra_basic = 0
    time_dijkstra_basic_array = []
    time_dijkstra_heap = 0
    time_dijkstra_heap_array = []
    n_array = []
    # Choosing alpha :
    edges_number = number_of_node - 2
    max_edges = (number_of_node * (number_of_node - 1)) / 2
    while edges_number < max_edges:
        edges_number += 1
        progressBar(edges_number, max_edges)
        n_array.append(edges_number)
        tested_graph = graph_generation.generate_random_graph(number_of_node, edges_number)
        # Generating a random graph and randomly choosing a vertex for dijkstra
        chosen_vertex = rand.randint(0, len(tested_graph))

        # For basic version of dijkstra :
        start = time.process_time()
        tested_graph.dijkstra_basic_version(chosen_vertex)
        end = time.process_time()
        time_dijkstra_basic = end - start
        time_dijkstra_basic_array.append(time_dijkstra_basic)

        # For heap version of dijkstra :
        start = time.process_time()
        tested_graph.dijkstra_heap_version(chosen_vertex)
        end = time.process_time()
        time_dijkstra_heap = end - start
        time_dijkstra_heap_array.append(time_dijkstra_heap)

        # ploting
    plt.plot(n_array, time_dijkstra_basic_array, label='basic')
    plt.plot(n_array, time_dijkstra_heap_array, label='heap')
    plt.xlabel('Edges number')
    plt.ylabel('Cumulated time (in seconds)')
    plt.title(f'Edges testing')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(f"../log/test_{edges_number}_edges.png")
    plt.close()


dijkstra_opti_tests(10000)
dijkstra_opti_tests_2(1000)
dijkstra_opti_tests_3(100)
