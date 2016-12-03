# To implement modified Warshall or Floyd's Algorithm to find the shortest path


class Vertex:                   # Class of vertex
    def __init__(self, key):
        self.id = key
        self.connected = {}     # dictionary of all the connected vertices with tht vertice

    def add_neighbor(self, nbr, weight=0):      # adding a adjacent neighbour
        self.connected[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connected to' + str([x.id for x in self.connected])

    def get_connections(self):          # Get all the adjacent vertices
        return self.connected.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected[nbr]


class Graph:
    def __init__(self):
        self.vertices_list = {}
        self.vertices_num = 0

    def add_vertex(self, key):          # Add a vertex in the graph
        self.vertices_num += 1
        new_vertex = Vertex(key)
        self.vertices_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):          # To return the vertex with the specified key
        if key in self.vertices_list:
            return self.vertices_list[key]
        else:
            return None

    def __contains__(self, items):      # Returns all the vertices by calling in a loop
        return items in self.vertices_list

    def add_edge(self, v1, v2, weight):
        if v1 not in self.vertices_list:
            self.add_vertex(v1)
        if v2 not in self.vertices_list:
            self.add_vertex(v2)
        self.vertices_list[v1].add_neighbor(self.vertices_list[v2], weight)

    def get_vertices(self):
        return self.vertices_list.keys()

    def __iter__(self):
        return iter(self.vertices_list.values())


def shortest_path(a, b, B):
    temp = B[a][b]
    print('Moving from %s ' %a, end='')
    while temp != a:
        print('to %s' % temp)
        temp = B[a][temp]


def floyd_warshall(g):
    if isinstance(g, Graph):
        x = len(g.vertices_list)
        A = {}      # The matrix that will contain the shortest paths
        B = {}      # The matrix that will contain the predecessors
        for j in g.get_vertices():      # Implementing the adjacent matrix
            A[j] = {}
        for i in A:
            for j in g.get_vertices():
                A[i][j] = 99999999          # the infinity value to compare
        for z in g.get_vertices():
            for m in g.get_vertex(z).get_connections():
                di = m.get_id()
                A[z][di] = g.get_vertex(z).connected[m]
        for j in g.get_vertices():
            B[j] = {}
        for i in B:
            for j in g.get_vertices():
                if A[i][j] != 99999999:
                    B[i][j] = i              # Intially all the predecessors are none
                else:
                    B[i][j] = None
        for a in g.get_vertices():
            for b in g.get_vertices():
                for c in g.get_vertices():
                    if A[b][a] + A[a][c] < A[b][c]:
                        A[b][c] = A[b][a] + A[a][c]
                        B[b][c] = a
        return A, B
    else:
        raise NameError('The passed variable is not a Graph')


if __name__ == "__main__":
    g = Graph()
    for i in range(0, 4):
        g.add_vertex(i)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 9)
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 7)
    g.add_edge(1, 0, 3)
    g.add_edge(2, 1, 6)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 0, 14)
    g.add_edge(3, 2, 4)
    a,b = floyd_warshall(g)     # a contains the shortest path matrix and b contains the pred matrix
    shortest_path(3, 0, b)