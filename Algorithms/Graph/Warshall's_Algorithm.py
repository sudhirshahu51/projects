import importlib.machinery
Graph = importlib.machinery.SourceFileLoader('Graph_dict', 'D:\WORK\Python\Main\Data Structures\Graph_dict.py').load_module()


def warshall(g):
    if isinstance(g, Graph.Graph):
        x = len(g.get_vertices())
        A = {}
        for j in g.get_vertices():      # Implementing the adjacent matrix
            A[j] = {}
        for i in A:
            for j in g.get_vertices():
                A[i][j] = 0
        for z in g.get_vertices():
            for m in g.get_vertex(z).get_connections():
                di = m.get_id()
                A[z][di] = 1
        for a in g.get_vertices():
            for b in g.get_vertices():
                for c in g.get_vertices():
                    if A[b][c] == 1:
                        pass
                    else:
                        if A[b][a] == 1 and A[a][b] == 1:
                            A[b][c] = 1
                        else:
                            A[b][c] = 0
        return A
    else:
        raise NameError('The passed variable is not a Graph')


if __name__ == "__main__":
    g = Graph.Graph()
    a = 3
    for i in range(0, 4):
        g.add_vertex(i)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 3, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(1, 0, 1)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 0, 1)
    g.add_edge(3, 2, 1)
    warshall(g)