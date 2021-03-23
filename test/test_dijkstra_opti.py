import time
import random as rand
import matplotlib.pyplot as plt
from statistics import mean
import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import graph_generation


def progressBar(current, total, barLength=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * barLength - 1) + '>'
    spaces = ' ' * (barLength - len(arrow))
    print(f"Progress: [{arrow + spaces}]  {percent}%", end="\r")


def dijkstra_time(tested_graph, chosen_vertex):
    # For basic version of dijkstra :
    start = time.process_time()
    tested_graph.dijkstra_basic_version(chosen_vertex)
    end = time.process_time()
    time_dijkstra_basic = end - start

    # For heap version of dijkstra :
    start = time.process_time()
    tested_graph.dijkstra_heap_version(chosen_vertex)
    end = time.process_time()
    time_dijkstra_heap = end - start
    return time_dijkstra_basic, time_dijkstra_heap


def dijkstra_opti_tests_mean(number_of_nodes: int) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs with max edges."""

    time_dijkstra_basic_array = []
    time_dijkstra_heap_array = []
    n_array = []
    nb_of_try = 100
    for i in range(1, number_of_nodes):
        progressBar(i, number_of_nodes)
        n_array.append(i)
        # Generating a random graph and randomly choosing a vertex for dijkstra

        basic_values = []
        heap_values = []
        for j in range(nb_of_try):
            tested_graph = graph_generation.random_generation(i)
            chosen_vertex = rand.randint(0, i)
            result = dijkstra_time(tested_graph, chosen_vertex)
            basic_values.append(result[0])
            heap_values.append(result[1])
        time_dijkstra_basic_array.append(mean(basic_values))
        time_dijkstra_heap_array.append(mean(heap_values))

        # ploting
    plt.plot(n_array, time_dijkstra_basic_array, label="basic")
    plt.plot(n_array, time_dijkstra_heap_array, label="heap")
    plt.xlabel('Number of nodes')
    plt.ylabel(f'Mean time over {nb_of_try} essay(in seconds)')
    plt.title(f'Comparing for x nodes and max edges')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(f"../log/test_nodes_{number_of_nodes}_mean_{nb_of_try}.png")
    plt.close()


def dijkstra_opti_tests_2(number_of_node: int) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs."""

    time_dijkstra_basic_array = []
    time_dijkstra_heap_array = []
    n_array = []
    nb_of_try = 100
    alpha = rand.random()
    alpha = round(alpha, 3)
    while 5 > alpha * (5 * 4) // 2:
        alpha = round(rand.random(), 3)
    # Choosing alpha :
    for i in range(1, number_of_node):
        progressBar(i, number_of_node)
        n_array.append(i)
        # Generating a random graph and randomly choosing a vertex for dijkstra

        basic_values = []
        heap_values = []
        for j in range(nb_of_try):
            tested_graph = graph_generation.generate_random_graph(i, round(alpha * (i * (i - 1) // 2)))
            chosen_vertex = rand.randint(0, i)
            result = dijkstra_time(tested_graph, chosen_vertex)
            basic_values.append(result[0])
            heap_values.append(result[1])
        time_dijkstra_basic_array.append(mean(basic_values))
        time_dijkstra_heap_array.append(mean(heap_values))

        # ploting
    plt.plot(n_array, time_dijkstra_basic_array, label='basic')
    plt.plot(n_array, time_dijkstra_heap_array, label='heap')
    plt.xlabel('Number of nodes')
    plt.ylabel(f'Mean time over {nb_of_try} essay(in seconds)')
    plt.title(f'For alpha = {alpha}')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(f"../log/test_alpha_{alpha}_nodes_{number_of_node}_mean_{nb_of_try}.png")
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
    plt.savefig(f"../log/test_edges_{edges_number}.png")
    plt.close()


start = time.time()
print(start)
# dijkstra_opti_tests_mean(500)
dijkstra_opti_tests_2(500)
# dijkstra_opti_tests_3(100)
end = time.time()
print(end)
print(end - start)
