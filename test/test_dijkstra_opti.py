import inspect
import os
import random as rand
import sys
import time
from statistics import mean, median
import networkx as nx
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import graph_generation


def progressbar(current, total, barlength=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * barlength - 1) + '>'
    spaces = ' ' * (barlength - len(arrow))
    print(f"Progress: [{arrow + spaces}]  {round(percent, 2)}%", end="\r")
    if percent >= 99:
        print("\n")


def time_basic(tested_graph, chosen_vertex):
    # For basic version of dijkstra :
    start = time.process_time()
    tested_graph.dijkstra_basic_version(chosen_vertex)
    end = time.process_time()
    return end - start


def time_heap(tested_graph, chosen_vertex, chosen_vertex2=False):
    # For heap version of dijkstra :
    start = time.process_time()
    tested_graph.dijkstra_heap_version(chosen_vertex, target_vertex=chosen_vertex2)
    end = time.process_time()
    return end - start


def time_nx_all_path(tested_graph, chosen_vertex):
    # For nx version of dijkstra :
    start = time.process_time()
    nx.single_source_dijkstra(tested_graph, chosen_vertex)
    end = time.process_time()
    return end - start


def time_nx_best(tested_graph, chosen_vertex, chosen_vertex2=None):
    # For nx version of better algo :
    start = time.process_time()
    nx.all_shortest_paths(tested_graph, chosen_vertex, chosen_vertex2)
    end = time.process_time()
    return end - start


def dijkstra_opti_tests_mean(number_of_nodes: int, nb_of_try: int = 10) -> None:
    time_basic_array = []
    time_heap_array = []
    time_nx_array_dj = []
    time_nx_array_best = []
    n_array = []
    for i in range(10, number_of_nodes, 25):
        progressbar(i, number_of_nodes)
        n_array.append(i)

        # Generating a random graph and randomly choosing a vertex for dijkstra
        tested_graph = graph_generation.generate_random_graph(i, int(i * (i - 1) // 2))
        tested_graph_nx = tested_graph.to_networkx()

        basic_values = []
        heap_values = []
        nx_values_dj = []
        nx_values_best = []
        for j in range(nb_of_try):
            chosen_vertex = rand.choice(list(tested_graph.vertices))

            basic_values.append(time_basic(tested_graph, chosen_vertex))
            heap_values.append(time_heap(tested_graph, chosen_vertex))
            nx_values_dj.append(time_nx_all_path(tested_graph_nx, chosen_vertex))
            nx_values_best.append(time_nx_best(tested_graph_nx, chosen_vertex))

        time_basic_array.append(mean(basic_values))
        time_heap_array.append(mean(heap_values))
        time_nx_array_dj.append(mean(nx_values_dj))
        time_nx_array_best.append(mean(nx_values_best))

    # ploting
    plt.plot(n_array, time_basic_array, label="basic")
    plt.plot(n_array, time_heap_array, label="heap")
    plt.plot(n_array, time_nx_array_dj, label="nx_dj")
    plt.plot(n_array, time_nx_array_best, label="nx_best")
    plt.xlabel("Number of nodes")
    plt.ylabel(f"Mean time over {nb_of_try} try(in seconds)")
    plt.title(f"Comparing for x nodes and max edges")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(f"../log/test_nodes_{number_of_nodes}_mean_{nb_of_try}.png")
    plt.close()


def dijkstra_opti_tests_41(number_of_nodes: int, nb_of_try: int = 10) -> None:
    time_basic_array = []
    time_heap_array = []
    time_nx_array_dj = []
    time_nx_array_best = []
    n_array = []
    alpha = round(rand.random(), 3)
    while 5 > alpha * (5 * 4) // 2:
        alpha = round(rand.random(), 3)
    for i in range(10, number_of_nodes, 25):
        progressbar(i, number_of_nodes)
        n_array.append(i)

        # Generating a random graph and randomly choosing a vertex for dijkstra
        tested_graph = graph_generation.generate_random_graph(i, round(alpha * int(i * (i - 1) // 2)))
        tested_graph_nx = tested_graph.to_networkx()

        basic_values = []
        heap_values = []
        nx_values_dj = []
        nx_values_best = []
        for j in range(nb_of_try):
            chosen_vertex = rand.choice(list(tested_graph.vertices))

            basic_values.append(time_basic(tested_graph, chosen_vertex))
            heap_values.append(time_heap(tested_graph, chosen_vertex))
            nx_values_dj.append(time_nx_all_path(tested_graph_nx, chosen_vertex))
            nx_values_best.append(time_nx_best(tested_graph_nx, chosen_vertex))

        time_basic_array.append(mean(basic_values))
        time_heap_array.append(mean(heap_values))
        time_nx_array_dj.append(mean(nx_values_dj))
        time_nx_array_best.append(mean(nx_values_best))

    # ploting
    plt.plot(n_array, time_basic_array, label="basic")
    plt.plot(n_array, time_heap_array, label="heap")
    plt.plot(n_array, time_nx_array_dj, label="nx_dj")
    plt.plot(n_array, time_nx_array_best, label="nx_best")
    plt.xlabel("Number of nodes")
    plt.ylabel(f"Mean time over {nb_of_try} try(in seconds)")
    plt.title(f"For alpha = {alpha}")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(f"../log/test41_nodes_{number_of_nodes}_mean_{nb_of_try}_alpha_{alpha}.png")
    plt.close()


def dijkstra_opti_tests_42(number_of_node: int, nb_of_try: int = 10) -> None:
    time_basic_array = []
    time_heap_array = []
    time_nx_array_dj = []
    time_nx_array_best = []
    n_array = []
    # Choosing edge number
    edges_number = number_of_node - 1
    max_edges = (number_of_node * (number_of_node - 1)) / 2
    print(max_edges)

    while edges_number < max_edges:

        progressbar(edges_number, max_edges)
        n_array.append(edges_number)

        tested_graph = graph_generation.generate_random_graph(number_of_node, edges_number)
        tested_graph_nx = tested_graph.to_networkx()

        basic_values = []
        heap_values = []
        nx_values_dj = []
        nx_values_best = []
        for j in range(nb_of_try):
            chosen_vertex = rand.choice(list(tested_graph.vertices))

            basic_values.append(time_basic(tested_graph, chosen_vertex))
            heap_values.append(time_heap(tested_graph, chosen_vertex))
            nx_values_dj.append(time_nx_all_path(tested_graph_nx, chosen_vertex))
            nx_values_best.append(time_nx_best(tested_graph_nx, chosen_vertex))

        time_basic_array.append(mean(basic_values))
        time_heap_array.append(mean(heap_values))
        time_nx_array_dj.append(mean(nx_values_dj))
        time_nx_array_best.append(mean(nx_values_best))
        edges_number += 10

        # ploting
    plt.plot(n_array, time_basic_array, label="basic")
    plt.plot(n_array, time_heap_array, label="heap")
    plt.plot(n_array, time_nx_array_dj, label="nx_dj")
    plt.plot(n_array, time_nx_array_best, label="nx_best")
    plt.xlabel("Edges number")
    plt.ylabel(f"Mean time over {nb_of_try} try(in seconds)")
    plt.title(f"Edges testing for {number_of_node} nodes")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(f"../log/test42_edges_nodes_{number_of_node}_mean_{nb_of_try}.png")
    plt.close()


def dijkstra_opti_tests_43(number_of_node: int, nb_of_try: int = 10) -> None:
    """ Test time for one algo for one specific path. Save a plot with max min mean and med time calculated over nb_of_try trial. Increment by number of node. Also save the data in a txt"""

    time_max = []
    time_min = []
    time_mean = []
    time_med = []
    n_array = []
    # Choosing alpha :
    alpha = 0.75
    for i in range(10, number_of_node, 25):
        progressbar(i, number_of_node)
        n_array.append(i)

        # Generating a random graph and randomly choosing a vertex for dijkstra
        tested_graph = graph_generation.generate_random_graph(i, round(alpha * int(i * (i - 1) // 2)))

        heap_values = []
        for j in range(nb_of_try):
            chosen_vertex = rand.choice(list(tested_graph.vertices))
            chosen_vertex2 = rand.choice(list(tested_graph.vertices))
            heap_values.append(time_heap(tested_graph, chosen_vertex, chosen_vertex2))

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
    plt.ylabel(f"Time over {nb_of_try} try(in seconds)")
    plt.title(f"For alpha = {alpha} with heap")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(f"../log/test43_nodes_{number_of_node}_mean_{nb_of_try}_alpha_{alpha}.png")
    plt.close()
    # f = open(f"../log/test43_nodes_{number_of_node}_mean_{nb_of_try}_alpha_{alpha}.txt", "w")
    # f.write(f"max   {time_max}\n")
    # f.write(f"min   {time_min}\n")
    # f.write(f"mean  {time_mean}\n")
    # f.write(f"med   {time_med}\n")
    # f.close()

# dijkstra_opti_tests_mean(1000)
# dijkstra_opti_tests_41(1000)
# dijkstra_opti_tests_42(200)
# dijkstra_opti_tests_43(1000)
