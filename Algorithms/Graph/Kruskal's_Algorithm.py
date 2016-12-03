# To find the minimum spanning tree by kruskal's method


class Vertex:                   # Class of vertex
    def __init__(self, key):
        self.id = key
        self.connected = {}     # dictionary of all the connected vertices with tht vertice
        self.father = None
        self.root = key

    def add_neighbor(self, nbr, weight=0):      # adding a adjacent neighbour where nbr is the vertex
        self.connected[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connected to' + str([x.id for x in self.connected])

    def get_connections(self):          # Get all the adjacent vertices
        return self.connected.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected[nbr]

    def find_root(self):      # here nbr is a vertex
        tmp = self.father
        pre = tmp
        if tmp is None:
            return self.root
        else:
            while tmp:
                pre = tmp
                tmp = tmp.father
        return pre.root


class Graph:
    def __init__(self):
        self.vertices_list = {}
        self.vertices_num = 0
        self.edges = {}         # contains the weight of the edges in the form 'v1:v2':weight

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
        self.vertices_list[v2].add_neighbor(self.vertices_list[v1], weight)
        self.edges[str(v1)+':'+str(v2)] = weight

    def get_vertices(self):
        return self.vertices_list.keys()

    def __iter__(self):
        return iter(self.vertices_list.values())


def lst(d):     # gives the ordered list of the edges with non decreasing order with weight
    l = []
    if not isinstance(d, dict):
        return
    for x in d.keys():
        if len(l) == 0:
            l.append(x)
        else:
            flag = 0
            for y in range(len(l)):
                if d[l[y]] <= d[x]:
                    pass
                else:
                    l.insert(y, x)
                    flag = 1
                    break
            if flag == 0:
                if d[l[y]] <= d[x]:
                    l.append(x)
    return l


def kruskal(a, g):
    if not isinstance(a, Vertex) and isinstance(g, Graph):
        print('passed parameters not of correct type')
        return
    n = Graph()
    l = lst(g.edges)
    for i in l:
        x, y = map(int, i.split(':'))
        root_x = g.get_vertex(x).find_root()
        root_y = g.get_vertex(y).find_root()
        if root_x != root_y:
            n.add_edge(x, y, g.edges[i])
            g.get_vertex(root_y).father = g.get_vertex(root_x)
        else:
            pass
    return n


if __name__ == '__main__':
    g = Graph()
    for x in range(9):
        g.add_vertex(x)
    g.add_edge(0, 1, 9)
    g.add_edge(0, 4, 2)
    g.add_edge(0, 3, 4)
    g.add_edge(1, 4, 8)
    g.add_edge(1, 2, 10)
    g.add_edge(2, 5, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 3)
    g.add_edge(3, 6, 18)
    g.add_edge(4, 5, 6)
    g.add_edge(4, 6, 11)
    g.add_edge(4, 7, 12)
    g.add_edge(4, 8, 15)
    g.add_edge(5, 8, 16)
    g.add_edge(6, 7, 14)
    g.add_edge(7, 8, 20)
    n = kruskal(g.get_vertex(0), g)
