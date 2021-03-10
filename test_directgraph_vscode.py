from  source.directgraph import DirectedGraph


def test_graph():
    graph = DirectedGraph()
    graph.add_vertex(1)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 1, 1)
    graph.add_edge(2, 3, 1)

    print("vertice\n", graph.vertices)
    print("len Graph\n", len(graph))
    print("Graph[2]\n", graph[2])
    print("Graph\n", graph)
    print("Vertex\n")
    for vertex in graph:
        print(vertex)
    # graph.remove_edge(1, 2)
    print(graph.dijkstra_basic_version(1))


test_graph()
