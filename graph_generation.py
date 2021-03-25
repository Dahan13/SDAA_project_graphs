from source import graph as grp
import random as rd
import networkx as nx


def generate_random_graph(n_nodes: int, n_edges: int, directed: bool = False) -> grp.UndirectedGraph:
    """Generate a random connex graph directed or not"""

    if directed:
        assert n_nodes - 1 <= n_edges <= (n_nodes * (n_nodes - 1))
        graph = grp.DirectedGraph()  # Curse the one who called variable like this -- from the module importation team
    else:
        assert n_nodes - 1 <= n_edges <= (n_nodes * (n_nodes - 1)) / 2
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


def random_generation(max_nodes: int) -> grp.UndirectedGraph:
    """ Generate a fully randomized graph, only given the maximum numer of nodes, max_nodes should be >= 1 """

    # Checking user input
    if max_nodes < 1:
        print("\nValue of random_generation argument should be >= 1 !\n")
        raise ValueError

    # Generating random values
    vertices_number = rd.randint(1, max_nodes)
    directed = bool(rd.randint(0, 1))

    # Max number of edges change depending if the graph is directed or not !
    if directed:
        edges_number = rd.randint(vertices_number - 1, (vertices_number * (vertices_number - 1)))
    else:
        edges_number = rd.randint(vertices_number - 1, (vertices_number * (vertices_number - 1)) // 2)

    return generate_random_graph(vertices_number, edges_number, directed)


def generate_random_community_graph(n_nodes_per_community: list, p_intra: float, p_inter: float) -> grp.UndirectedGraph:
    # Init
    the_graph = grp.UndirectedGraph()

    # Creating all the nodes
    for community in range(len(n_nodes_per_community)):
        for number in range(n_nodes_per_community[community]):
            the_graph.add_vertex((community, number))

    # Now adding edges
    for vertex1 in the_graph.edges:
        for vertex2 in the_graph.edges:

            # If in the same community
            if vertex1[0] == vertex2[0]:
                probability = rd.random()
                if probability <= p_intra:
                    the_graph.add_edge(vertex1, vertex2)

            # If not in the same community
            else:
                probability = rd.random()
                if probability <= p_inter:
                    the_graph.add_edge(vertex1, vertex2)

    return the_graph


graph = generate_random_graph(10, 15)
graph = graph.to_networkx()
nx.single_source_dijkstra(graph,0)
# print(test)
