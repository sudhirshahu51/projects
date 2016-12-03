# To find the shortest path between the source point and all the remaining vertices for
# non-negative weight


class Vertex:                   # Class of vertex
    def __init__(self, key):
        self.id = key
        self.connected = {}     # dictionary of all the connected vertices with tht vertice
        self.st = 'temp'        # temporary or permanent
        self.predecessor = None
        self.distance = 0
        self.path_len = 99999999999         # this is infinity for comparison

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
        self.temp_list = {}     # Making a temp and perm list for all those with same status
        self.perm_list = {}

    def add_vertex(self, key):          # Add a vertex in the graph
        self.vertices_num += 1
        new_vertex = Vertex(key)
        self.vertices_list[key] = new_vertex
        self.temp_list[key] = new_vertex
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


def dijkstra(a, g):      # a is the starting vertex and g is the graph
    if not (isinstance(a, Vertex) and isinstance(g, Graph)):
        print('The entered values are not of correct type')
        return
    a.path_len = 0
    while len(g.temp_list) != 0:
        current = list(g.temp_list.keys())[0]
        for x in g.temp_list.keys():
            if g.get_vertex(current).path_len > g.get_vertex(x).path_len:
                current = x
        current = g.get_vertex(current)
        current.state('perm')
        for x in current.get_connections():
            if current.path_len + current.get_weight(x) < x.path_len and x.status() == 'temp':
                x.path_len = current.path_len + current.get_weight(x)
                x.predecessor = current
        g.perm_list[current.id] = g.temp_list.pop(current.id)


def shortest_path(a):       # To find the shortest path and path length
    pre = a.predecessor
    print('moving from %s to %s' %(a.id, pre.id))
    while pre.predecessor is not None:
        temp = pre
        pre = pre.predecessor
        print('moving from %s to %s' %(temp.id, pre.id))
    print('Path length:', a.path_len)

if __name__ == "__main__":
    g = Graph()
    for i in range(8):
        g.add_vertex(i)
    g.add_edge(0, 1, 8)
    g.add_edge(0, 2, 2)
    g.add_edge(0, 3, 7)
    g.add_edge(1, 5, 16)
    g.add_edge(2, 0, 5)
    g.add_edge(2, 6, 3)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(4, 0, 4)
    g.add_edge(4, 5, 5)
    g.add_edge(4, 7, 8)
    g.add_edge(6, 2, 6)
    g.add_edge(6, 4, 4)
    g.add_edge(6, 3, 3)
    g.add_edge(7, 6, 5)
    g.add_edge(7, 5, 2)
    dijkstra(g.get_vertex(0), g)
    shortest_path(g.get_vertex(3))
    print(g.vertices_list.keys())