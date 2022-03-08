from typing import Dict, List, Callable
from Vertex import *
from Edge import *
from EdgeType import *
from Queue import *
import networkx as nx
import matplotlib.pyplot as plt


from networkx.drawing.nx_agraph import view_pygraphviz


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, adjacencies = None) -> None:
        if adjacencies is None:
            adjacencies = {}
        self.adjacencies = adjacencies

    def create_vertex(self, data: Any, index: Any) -> Vertex:
        newVertex = Vertex(data, index)
        self.adjacencies[newVertex] = []
        return newVertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        newEdge = Edge(source, destination, weight)
        newEdge.type = EdgeType.directed
        self.adjacencies[source].append(newEdge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        newEdge = Edge(source, destination, weight)
        newEdge.type = EdgeType.undirected
        self.adjacencies[source].append(newEdge)
        newEdge = Edge(destination, source, weight)
        newEdge.type = EdgeType.undirected
        self.adjacencies[destination].append(newEdge)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if type(edge) is EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        if type(edge) is EdgeType.undirected:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        first = list(self.adjacencies.keys())[0]
        odwiedzone = [first]
        queue = Queue()
        queue.enqueue(first)
        while (len(queue) > 0):
            v = queue.dequeue()
            visit(v)
            for wieszholeg in self.adjacencies[v]:
                if wieszholeg.destination not in odwiedzone:
                    odwiedzone.append(wieszholeg.destination)
                    queue.enqueue(wieszholeg.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        v = list(self.adjacencies.keys())[0]
        odwiedzone = []
        self.dfs(v, odwiedzone, visit)
        
    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        visited.append(v)
        visit(v)
        for somsiad in self.adjacencies[v]:
            if somsiad.destination not in visited:
                self.dfs(somsiad.destination, visited, visit)

    def all_edges(self):
        edges = []
        for Vertex in self.adjacencies:
            for Edge in self.adjacencies[Vertex]:
                if (Edge.destination.data, Vertex.data) not in edges:
                    edges.append((Vertex.data, Edge.destination.data))
        return edges

    def show(self):
        G = nx.DiGraph()
        G.add_edges_from(self.all_edges())
        def czyDirect():
            for Vertex in self.adjacencies:
                for Edge in self.adjacencies[Vertex]:
                    if Edge.type == EdgeType.directed:
                        return True
            return False

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_shape='o', node_color = "white",
                            edgecolors="black", node_size = 500)
        nx.draw_networkx_labels(G, pos)
        if czyDirect():
            nx.draw_networkx_edges(G, pos, arrows=True)
        else:
            nx.draw_networkx_edges(G, pos, arrows=False)
        plt.show()


    def __str__(self):
        s = ""
        for Vertex in self.adjacencies:
            edges = []
            s += "-" + str(Vertex.index) +": " +str(Vertex.data)+ " ------>"
            for Edge in self.adjacencies[Vertex]:
                if Edge.destination not in edges:
                    edges.append(Edge.destination)
            for vertex in self.adjacencies:
                for edge in self.adjacencies[vertex]:        
                    if Vertex == edge.destination :
                            if vertex not in edges:
                                edges.append(vertex)
            s += "["
            for Vertex in edges:
                s += str(Vertex.index) + ": " + str(Vertex.data) + ", "
            s = s[:-2]
            s+= "]" + "\n"
        return s


graf1 = Graph()
v0 = graf1.create_vertex("v0",0)
v1 = graf1.create_vertex("v1",1)
v2 = graf1.create_vertex("v2",2)
v3 = graf1.create_vertex("v3",3)
v4 = graf1.create_vertex("v4",4)
v5 = graf1.create_vertex("v5",5)

graf1.add_undirected_edge(v0, v1)
graf1.add_undirected_edge(v0, v2)
graf1.add_undirected_edge(v0, v3)
graf1.add_undirected_edge(v0, v4)
graf1.add_undirected_edge(v0, v5)



graf = Graph()
v0 = graf.create_vertex("v0",0)
v1 = graf.create_vertex("v1",1)
v2 = graf.create_vertex("v2",2)
v3 = graf.create_vertex("v3",3)
v4 = graf.create_vertex("v4",4)
v5 = graf.create_vertex("v5",5)

graf.add_directed_edge(v0, v1)
graf.add_directed_edge(v0, v5)

graf.add_directed_edge(v2, v1)
graf.add_directed_edge(v2, v3)

graf.add_directed_edge(v3, v4)

graf.add_directed_edge(v4, v1)
graf.add_directed_edge(v4, v5)

graf.add_directed_edge(v5, v1)
graf.add_directed_edge(v5, v2)

