# To implement Topological Sorting for directed graph
# Topological Sorting: if there is path from u to v then u comes before v in ordering


class Vertex:                   # Class of vertex
    def __init__(self, key):
        self.id = key
        self.connected = {}     # dictionary of all the connected vertices with tht vertice
        self.in_degree = 0
        self.status = 'tmp'

    def add_neighbor(self, nbr, weight=0):      # adding a adjacent neighbour where nbr is vertex
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

    def __contains__(self, items):      # Returns all the vertice by calling for i in g
        return items in self.vertices_list

    def add_edge(self, v1, v2, weight=1):
        if v1 not in self.vertices_list:
            self.add_vertex(v1)
        if v2 not in self.vertices_list:
            self.add_vertex(v2)
        self.vertices_list[v1].add_neighbor(self.vertices_list[v2], weight)
        g.get_vertex(v2).in_degree += 1

    def get_vertices(self):
        return self.vertices_list.keys()

    def __iter__(self):
        return iter(self.vertices_list.values())


class Queue:
    def __init__(self):
        self.items = []

    def __contains__(self, item):
        return item in self.items

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)

    def de_queue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[-1]

    def rare(self):
        return self.items[0]


def topological(g):
    if not isinstance(g, Graph):
        return
    q = Queue()
    order = []
    lst = list(g.vertices_list.keys())
    while len(lst) != 0:
        for x in lst:
            if g.get_vertex(x).in_degree == 0:
                q.enqueue(x)
                lst.remove(x)
        tmp = q.de_queue()
        order.append(g.get_vertex(tmp))
        for x in g.get_vertex(tmp).get_connections():
            x.in_degree -= 1
    return order


if __name__ == '__main__':
    g = Graph()
    for i in range(7):
        g.add_vertex(i)
    g.add_edge(0, 5)
    g.add_edge(0, 1)
    g.add_edge(1, 5)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 1)
    g.add_edge(3, 1)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(6, 5)
    g.add_edge(6, 4)
    print(topological(g))