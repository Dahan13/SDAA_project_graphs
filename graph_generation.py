from source import graph as grp
import random as rd


def generate_random_graph(n_nodes: int, n_edges: int, directed: bool = False) -> 'grp.UndirectedGraph':
    """Generate a random connex graph directed or not"""
    
    if directed:
        assert n_nodes - 1 <= n_edges <= (n_nodes * (n_nodes - 1))
        graph = grp.DirectedGraph() # Curse the one who called variable like this -- from the module importation team
    else:
        assert n_nodes - 1 <= n_edges <= (n_nodes * (n_nodes - 1))/2
        graph = grp.UndirectedGraph()
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
        remaining_edges -= 1
    while remaining_edges > 0:
        departure = rd.randint(0, n_nodes - 1)
        arrival = rd.randint(0, n_nodes - 1)
        check = graph.add_edge(departure, arrival, checker=True)
        if check:
            remaining_edges -= 1
    return graph

def random_generation(max_nodes: int) -> 'grp.UndirectedGraph':
    """ Generate a fully randomized graph, only given the maximum numer of nodes, max_nodes should be >= 1 """

    # Checking user input
    if max_nodes < 1 :
        print("\nValue of random_generation argument should be >= 1 !\n")
        raise ValueError

    # Generating random values
    vertices_number = rd.randint(1, max_nodes)
    directed = rd.randint(0, 1)

    # Max number of edges change depending if the graph is directed or not !
    if directed :
        edges_number = rd.randint(vertices_number - 1, (vertices_number * (vertices_number -1)))
    else :
        edges_number = rd.randint(vertices_number - 1, (vertices_number * (vertices_number -1))/2)

    return generate_random_graph(vertices_number, edges_number, directed)
