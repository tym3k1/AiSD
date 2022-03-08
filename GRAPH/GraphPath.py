

from Graph import *
from Vertex import *
from Queue import *
import math
from matplotlib import colors
import matplotlib.pyplot as plt


class GraphPath:
    

    def algorytmDijkstry(self, graph: Graph, startVertex: Vertex, endVertex: Vertex):
        tablicaKosztow = {}
        visited = []
        path = {}
        path[startVertex] = 0
        for edges in graph.adjacencies[startVertex]:
            tablicaKosztow[edges.destination] = edges.weight
        tablicaKosztow[endVertex] = math.inf
        tablcaRodicow = {}
        for edges in graph.adjacencies[startVertex]:
            tablcaRodicow[edges.destination] = startVertex
        tablcaRodicow[endVertex] = None
        v = self.najmniejszyKoszt(visited, tablicaKosztow)
        while(v is not None):
            c = tablicaKosztow.get(v)
            path[v]=c
            for neighbour in graph.adjacencies[v]:
                nc = c + neighbour.weight
                if tablicaKosztow[neighbour.destination] > nc:
                    tablicaKosztow[neighbour.destination] = nc
                tablcaRodicow[neighbour.destination] = v
            visited.append(v)
            v = self.najmniejszyKoszt(visited, tablicaKosztow)
        return list(path.keys())

    def najmniejszyKoszt(self, odwiedzone: List[vars], tablicaKosztow: Dict[vars, vars]):
        lc = math.inf
        for vertex in tablicaKosztow:
            if tablicaKosztow.get(vertex) < lc and vertex not in odwiedzone:
                lc = tablicaKosztow.get(vertex)
        for vertex, value in tablicaKosztow.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            if value == lc:
                return vertex
    
    def przechodzenieWszerz(self, graph: Graph, startVertex: Vertex, endVertex: Vertex):
        road = [startVertex]
        visited = []
        queue = Queue()
        queue.enqueue(road)
        while(len(queue)>0):
            current = queue.dequeue()
            currentV = current[-1]
            for n in graph.adjacencies[currentV]:
                if n.destination in visited:
                    break
            road.append(n.destination)  
            visited.append(n.destination)
            queue.enqueue(road)
            if endVertex == n.destination: return road
        return False

    def __str__(self):
        return str(self.graphPath)

    def pathEdges(self, lista: List[Vertex]):
        edges = []
        edges_finale = []
        for item in lista:
            edges.append(item.data)
        for x in range(len(edges)-1):
            edges_finale.append((edges[x], edges[x+1]))
        return edges_finale

    def showw(self, graf: Graph, lista: List[Vertex]):
        G = nx.DiGraph()
        G.add_edges_from(graf.all_edges())
        pos = nx.spring_layout(G)
        path_edges = self.pathEdges(lista)
        print(path_edges)
        nx.draw_networkx_nodes(G, pos, node_shape='o', node_color = "white",
                            edgecolors="black", node_size = 500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r',width=10, arrows=True)
        nx.draw_networkx_edges(G, pos, edge_color='b', arrows=True)
        plt.show()


    def __init__(self,graph: Graph, startVertex: Vertex, endVertex: Vertex):
        edg = graph.adjacencies.get(startVertex)[0]
        if edg.weight != None:
            self.graphPath = self.algorytmDijkstry(graph, startVertex, endVertex)
            print(self.graphPath)
            self.showw(graph, self.graphPath)
        else:
            self.graphPath = self.przechodzenieWszerz(graph, startVertex, endVertex)
            self.showw(graph, self.graphPath)

graf_test_weighted = Graph()
A = graf_test_weighted.create_vertex("A",0)
B = graf_test_weighted.create_vertex("B",1)
C = graf_test_weighted.create_vertex("C",2)
D = graf_test_weighted.create_vertex("D",3)
E = graf_test_weighted.create_vertex("E",4)
F = graf_test_weighted.create_vertex("F",5)


graf_test_weighted.add_directed_edge(A, B, 30)
graf_test_weighted.add_directed_edge(A, C, 10)
graf_test_weighted.add_directed_edge(C, B, 5)
graf_test_weighted.add_directed_edge(B, D, 2)
graf_test_weighted.add_directed_edge(C, D, 9)
graf_test_weighted.add_directed_edge(D, F, 3)
graf_test_weighted.add_directed_edge(C, E, 9)
graf_test_weighted.add_directed_edge(E, F, 1)


print(GraphPath(graf_test_weighted, A, D))

''' graf_test = Graph()
A = graf_test.create_vertex("A",0)
B = graf_test.create_vertex("B",1)
C = graf_test.create_vertex("C",2)
D = graf_test.create_vertex("D",3)


graf_test.add_directed_edge(A, B)
graf_test.add_directed_edge(A, C)
graf_test.add_directed_edge(C, B)
graf_test.add_directed_edge(B, D)
graf_test.add_directed_edge(C, D)

print(GraphPath(graf_test, A, D)) '''

