from graph import DirectedGraph


def test_graph():
    graph = DirectedGraph()
    graph.add_vertex("banane")
    graph.add_edge("banane", 2, 3)
    graph.add_edge(2, "banane", 1)
    graph.add_edge(2, 3, 1)

    print("vertice\n", graph.vertices)
    print("len Graph\n", len(graph))
    print("Graph[2]\n", graph[2])
    print("Graph\n", graph)
    print("Vertex\n")
    for vertex in graph:
        print(vertex)
    # graph.remove_edge(1, 2)
    graph.remove_vertex("banane")
    print("Graph\n", graph)


test_graph()
