class Vertex:                   # Class of vertex
    def __init__(self, key):
        self.id = key
        self.connected = {}     # dictionary of all the connected vertices with tht vertice
        self.st = 'initial'
        self.discovery = 0
        self.finish = 0

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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)


def bf_traversal(a):
    if isinstance(a, Vertex):
        while a in g:
            if a.status == 'initial':
                depth_first_search_recursive(a)


def depth_first_search_recursive(a):    # To find the discovery time and finishing time with dynamic programming
    global trav
    global t
    t += 1
    if isinstance(a, Vertex):
        a.state('visited')
        a.discovery = t
        for nbr in a.get_connections():
            if nbr.status() == 'initial':
                trav.append(nbr.id)
                depth_first_search_recursive(nbr)
        a.state('finished')
        t += 1
        a.finish = t


def depth_first_search_stack(a, g):  # Implementing the search with a as vertex and g graph
    if isinstance(a, Vertex) and isinstance(g, Graph):
        s = Stack()
        traversal = []
        s.push(a)
        while not s.isEmpty():
            current = s.pop()
            for nbr in current.get_connections():
                if nbr.status() == 'initial':
                    nbr.state('visited')
                    s.push(nbr)
            current.state('finished')
            traversal.append(current.id)
        print(traversal)


if __name__ == '__main__':
    g = Graph()
    t = 0
    trav = []
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
depth_first_search_stack(g.get_vertex(0), g)