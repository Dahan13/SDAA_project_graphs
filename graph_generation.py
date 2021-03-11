from graph import *
import random as rd


def generate_random_graph(n_nodes: int, n_edges: int, directed: bool = False) -> UndirectGraph:
    """Generate a random connex graph directed or not"""
    assert n_nodes - 1 <= n_edges <= (n_nodes * (n_nodes - 1)) / 2
    if directed:
        graph = DirectedGraph()
    else:
        graph = UndirectGraph()
    remaining_edges = n_edges
    for node in range(n_nodes):
        graph.add_vertex(node)
    if n_nodes == 0 or n_nodes == 1:
        return graph
    graph.add_edge(0, 1)
    remaining_edges -= 1
    for node in range(2, n_nodes):
        arrival = rd.randint(0, node - 1)
        graph.add_edge(node, arrival)
    while graph.edges:
        departure = rd.randint(0, n_nodes - 1)
        arrival = rd.randint(0, n_nodes - 1)
        graph.add_edge(departure, arrival)
    return graph


# print(generate_random_graph(5,4))
# graph_1 = UndirectGraph({0: {}})
# graph_1_alt = generate_random_graph(1,0)
# test = graph_1 == graph_1_alt
# print(graph_1)
# print(graph_1_alt)
# print(test)
