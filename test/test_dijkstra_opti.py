import inspect
import os
import random as rand
import sys
import time
from statistics import mean, median

import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import graph_generation


def progressbar(current, total, barlength=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * barlength - 1) + '>'
    spaces = ' ' * (barlength - len(arrow))
    print(f"Progress: [{arrow + spaces}]  {percent}%", end="\r")
    if current == total:
        print("\n")


def dijkstra_time_both(tested_graph, chosen_vertex):
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


def dijkstra_time_best(tested_graph, chosen_vertex1, chosen_vertex2):
    # For heap version of dijkstra :
    start = time.process_time()
    result = tested_graph.dijkstra_one_node(chosen_vertex1,chosen_vertex2)
    end = time.process_time()
    time_dijkstra_heap = end - start
    return time_dijkstra_heap


def dijkstra_opti_tests_mean(number_of_nodes: int, nb_of_try: int = 100) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs with max edges."""

    time_dijkstra_basic_array = []
    time_dijkstra_heap_array = []
    n_array = []
    for i in range(1, number_of_nodes):
        progressbar(i, number_of_nodes)
        n_array.append(i)
        # Generating a random graph and randomly choosing a vertex for dijkstra

        basic_values = []
        heap_values = []
        for j in range(nb_of_try):
            tested_graph = graph_generation.random_generation(i)
            chosen_vertex = rand.randint(0, i)
            result = dijkstra_time_both(tested_graph, chosen_vertex)
            basic_values.append(result[0])
            heap_values.append(result[1])
        time_dijkstra_basic_array.append(mean(basic_values))
        time_dijkstra_heap_array.append(mean(heap_values))

        # ploting
    plt.plot(n_array, time_dijkstra_basic_array, label="basic")
    plt.plot(n_array, time_dijkstra_heap_array, label="heap")
    plt.xlabel("Number of nodes")
    plt.ylabel(f"Mean time over {nb_of_try} essay(in seconds)")
    plt.title(f"Comparing for x nodes and max edges")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(f"../log/test_nodes_{number_of_nodes}_mean_{nb_of_try}.png")
    plt.close()


def dijkstra_opti_tests_41(number_of_node: int, nb_of_try: int = 100) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs."""

    time_dijkstra_basic_array = []
    time_dijkstra_heap_array = []
    n_array = []
    # Choosing alpha :
    alpha = rand.random()
    alpha = round(alpha, 3)
    while 5 > alpha * (5 * 4) // 2:
        alpha = round(rand.random(), 3)
    for i in range(1, number_of_node):
        progressbar(i, number_of_node)
        n_array.append(i)
        # Generating a random graph and randomly choosing a vertex for dijkstra

        basic_values = []
        heap_values = []
        for j in range(nb_of_try):
            tested_graph = graph_generation.generate_random_graph(i, round(alpha * (i * (i - 1) // 2)))
            chosen_vertex = rand.randint(0, i)
            result = dijkstra_time_both(tested_graph, chosen_vertex)
            basic_values.append(result[0])
            heap_values.append(result[1])
        time_dijkstra_basic_array.append(mean(basic_values))
        time_dijkstra_heap_array.append(mean(heap_values))

        # ploting
    plt.plot(n_array, time_dijkstra_basic_array, label="basic")
    plt.plot(n_array, time_dijkstra_heap_array, label="heap")
    plt.xlabel("Number of nodes")
    plt.ylabel(f"Mean time over {nb_of_try} essay(in seconds)")
    plt.title(f"For alpha = {alpha}")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(f"../log/test41_alpha_{alpha}_nodes_{number_of_node}_mean_{nb_of_try}.png")
    plt.close()


def dijkstra_opti_tests_42(number_of_node: int, nb_of_try: int = 100) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs."""

    time_dijkstra_basic_array = []
    time_dijkstra_heap_array = []
    n_array = []
    # Choosing edge number
    edges_number = number_of_node - 2
    max_edges = (number_of_node * (number_of_node - 1)) / 2
    # increment = round(1 / 100 * max_edges)
    while edges_number < max_edges:
        # edges_number += increment
        edges_number += 1
        progressbar(edges_number, max_edges)
        n_array.append(edges_number)

        basic_values = []
        heap_values = []
        for j in range(nb_of_try):
            tested_graph = graph_generation.generate_random_graph(number_of_node, edges_number)
            chosen_vertex = rand.randint(0, number_of_node)
            result = dijkstra_time_both(tested_graph, chosen_vertex)
            basic_values.append(result[0])
            heap_values.append(result[1])
        time_dijkstra_basic_array.append(mean(basic_values))
        time_dijkstra_heap_array.append(mean(heap_values))

        # ploting
    plt.plot(n_array, time_dijkstra_basic_array, label="basic")
    plt.plot(n_array, time_dijkstra_heap_array, label="heap")
    plt.xlabel("Edges number")
    plt.ylabel("Cumulated time (in seconds)")
    plt.title(f"Edges testing")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(f"../log/test42_edges_nodes_{number_of_node}_mean_{nb_of_try}.png")
    plt.close()


def dijkstra_opti_tests_43(number_of_node: int, nb_of_try: int = 100) -> None:
    """ Will do some tests to ensure which algorithm is better optimized, by using randomly generated graphs."""

    time_max = []
    time_min = []
    time_mean = []
    time_med = []
    n_array = []
    # Choosing alpha :
    alpha = rand.random()
    alpha = round(alpha, 3)
    while 5 > alpha * (5 * 4) // 2:
        alpha = round(rand.random(), 3)
    for i in range(1, number_of_node):
        progressbar(i, number_of_node)
        n_array.append(i)

        # Generating a random graph and randomly choosing a vertex for dijkstra
        heap_values = []
        for j in range(nb_of_try):
            tested_graph = graph_generation.generate_random_graph(i, round(alpha * (i * (i - 1) // 2)))
            chosen_vertex1 = rand.randint(0, i)
            chosen_vertex2 = rand.randint(0, i)
            result = dijkstra_time_best(tested_graph, chosen_vertex1, chosen_vertex2)
            heap_values.append(result)
        time_max.append(max(heap_values))
        time_min.append(min(heap_values))
        time_mean.append(mean(heap_values))
        time_med.append(median(heap_values))

        # ploting
    plt.plot(n_array, time_max, label="tmax")
    plt.plot(n_array, time_min, label="tmin")
    plt.plot(n_array, time_mean, label="tmean")
    plt.plot(n_array, time_med, label="tmed")
    plt.xlabel("Number of nodes")
    plt.ylabel(f"Mean time over {nb_of_try} essay(in seconds)")
    plt.title(f"For alpha = {alpha}")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(f"../log/test43_alpha_{alpha}_nodes_{number_of_node}_mean_{nb_of_try}.png")
    plt.close()

# dijkstra_opti_tests_mean(500)
# dijkstra_opti_tests_41(500)
# dijkstra_opti_tests_42(50)
# dijkstra_opti_tests_43(100)
