from graph import DirectedGraph


def read_file(file_name):
    subreddit_file = open(file_name)
    subreddit_links_list = subreddit_file.readlines()[1:]
    subreddit_file.close()

    for i in range(0, len(subreddit_links_list)):
        split = subreddit_links_list[i].split('\t')
        split = (split[0], split[1])
        subreddit_links_list[i] = split
    return subreddit_links_list


def create_graph_from_edges(links_list):
    graph = DirectedGraph()
    for sub1, sub2 in set(links_list):
        if sub1 not in graph.edges:
            graph.add_vertex(sub1)
        if sub2 not in graph.edges:
            graph.add_vertex(sub2)
        graph.add_edge(sub1, sub2, 1)
    return graph


def create_graph(file_name):
    # Creates graph with no duplicate edge
    return create_graph_from_edges(set(read_file(file_name)))

