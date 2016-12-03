# To find the minimum no. of dices required to get from starting point 1 to the finishing point
# With using ladders to climb up and snakes to slide down


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

    def add_edge(self, v1, v2, weight):     # v1 and v2 are the keys
        if v1 not in self.vertices_list:
            self.add_vertex(self, v1)
        if v2 not in self.vertices_list:
            self.add_vertex(self, v2)
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
        temp = b
        lst = []
        while temp.predecessor is not None:
            lst.append(temp.id)
            temp = temp.predecessor
        lst.append(1)
        lst.reverse()
        return lst


n = int(input('Enter the cells of the board'))              # int(input('Enter the no. of cells for the board'))
move = [-1 for x in range(n)]
z = int(input('Enter the no. of ladders'))
print('Enter the ladders by entering the starting point and ending point with a space')
for x in range(z):
    a, b = map(int, input().split())
    move[a-1] = b
z = int(input('Enter the no. of snakes'))
print('Enter the snakes by entering the starting point and ending point with a space')
for x in range(z):
    a, b = map(int, input().split())
    move[a-1] = b
'''
move[3-1] = 22
move[5-1] = 8
move[11-1] = 26
move[20-1] = 29
move[27-1] = 1
move[21-1] = 9
move[17-1] = 4
move[19-1] = 7
'''
g = Graph()
for i in range(1, n+1):
    g.add_vertex(i)
for i in range(1, n+1):
    if n - i >= 6:
        for j in range(i+1, i+7):
            if move[j-1] != -1:
                g.add_edge(i, j, 1)
                g.add_edge(j, move[j-1], 1)
            else:
                g.add_edge(i, j, 1)
    else:
        for j in range(i+1, i+(n-i+1)):
            if move[j-1] != -1:
                g.add_edge(i, move[j-1], 1)
            else:
                g.add_edge(i, j, 1)
breadth_first_search(g.get_vertex(1), g)
t = shortest_path(g.get_vertex(1), g.get_vertex(n))
for i in range(len(t)-1):
    j = i+1
    if t[j] - t[i] <= 6:
        print('Throw a dice of %s' %(t[j]-t[i]))
        print('To reach %s' %t[j])
    else:
        print('To reach %s' %t[j])