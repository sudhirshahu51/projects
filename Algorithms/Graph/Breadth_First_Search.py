class Vertex:                   # Class of vertex
    def __init__(self, key):
        self.id = key
        self.connected = {}     # dictionary of all the connected vertices with tht vertice
        self.st = 'initial'
        self.predecessor = None
        self.distance = 0

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

    def state(self, new):
        self.st = new

    def status(self):
        return self.st



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


class Queue:
    def __init__(self):
        self.items = []

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


def breadth_first_search(a, g):     # a is the starting vertex and g is the graph
    b = Queue()
    traversal = []
    if isinstance(a, Vertex) and isinstance(g, Graph):
        b.enqueue(a)
        a.state('waiting')
        while not b.is_empty():
            temp = b.de_queue()
            for nbr in temp.get_connections():
                if nbr.status() == 'initial':
                    nbr.state('waiting')
                    nbr.predecessor = temp
                    nbr.distance = temp.distance + 1
                    b.enqueue(nbr)
            temp.state('visited')
            traversal.append(temp.get_id())
        return traversal
    else:
        raise NameError('The parsed variables are not of the graph and queue type')


def shortest_path(a, b):        # A is the starting point and b is the ending point
    if isinstance(a, Vertex) and isinstance(b, Vertex):
        breadth_first_search(a, g)
        temp = b
        print('Shortest path from %s to %s is of lenght %s' % (a.id, b.id, b.distance))
        while temp.predecessor is not None:
            print('Moving from %s ' % temp.id, end='')
            temp = temp.predecessor
            print('to %s' % temp.id)


def bfs_traversal(g):
    if isinstance(g, Graph):
        for i in g:
            print('Traversal for %s' % i.get_id())
            breadth_first_search(i, g)


if __name__ == "__main__":
    g = Graph()
    a = 3
    for i in range(0, 9):
        g.add_vertex(i)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 3, 1)
    g.add_edge(0, 4, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 4, 1)
    g.add_edge(2, 5, 1)
    g.add_edge(3, 4, 1)
    g.add_edge(3, 6, 1)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(6, 4, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 5, 1)
    g.add_edge(7, 8, 1)
    shortest_path(g.get_vertex(0), g.get_vertex(8))