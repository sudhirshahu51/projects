class Vertex:                   # Class of vertex
    def __init__(self, key):
        self.id = key
        self.connected = {key: self}     # dictionary of all the connected vertices with tht vertice

    def add_neighbor(self, nbr):      # adding a adjacent neighbour where nbr is the vertex
        self.connected[nbr.id] = nbr


class Graph:
    def __init__(self):
        self.vertices_list = {}

    def add_vertex(self, key):          # Add a vertex in the graph
        new_vertex = Vertex(key)
        self.vertices_list[key] = new_vertex

    def add_edge(self, v1, v2):
        self.vertices_list[v1].add_neighbor(self.vertices_list[v2])
        self.vertices_list[v2].add_neighbor(self.vertices_list[v1])


def infected_planet(id):
    vertex = g.vertices_list[id]
    uninfected = g.vertices_list.keys() - vertex.connected.keys()
    for j in iter(pop):
        if temp_dict[j] in uninfected:
            return temp_dict[j]


t = int(input())        # No. of test cases
while t:
    temp_dict = {}
    n = int(input())    # No. of planets
    g = Graph()
    pop = list(map(int, input().split()))       # population on different planets
    for i, j in enumerate(pop):
        g.add_vertex(key=i+1)
        temp_dict[j] = i+1
    pop.sort(reverse=True)
    for _ in range(n-1):
        i, j = input().split()
        g.add_edge(int(i), int(j))
    for i in range(n):
        print(infected_planet(i+1), end=' ')
    print('')
    t -= 1
