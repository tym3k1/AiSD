from Graph import *

def mutal_friends(g: Graph, f0: Any, f1:Any) -> List[Any]:
    listaPierwszegoJegomoscia = []
    listaZwracana = []
    for edge in g.adjacencies[f0]:
        if edge.destination is not f1:
            listaPierwszegoJegomoscia.append(edge.destination)
    for edge in g.adjacencies[f1]:
        if edge.destination in listaPierwszegoJegomoscia and edge.destination.data not in listaZwracana:
            listaZwracana.append(edge.destination.data)
    return listaZwracana

grafTestowy_1 = Graph()
VI = grafTestowy_1.create_vertex("VI",0)
RU = grafTestowy_1.create_vertex("RU",1)
PA = grafTestowy_1.create_vertex("PA",2)
CO = grafTestowy_1.create_vertex("CO",3)
CH = grafTestowy_1.create_vertex("CH",4)
RA = grafTestowy_1.create_vertex("RA",5)
SU = grafTestowy_1.create_vertex("SU",6)
KE = grafTestowy_1.create_vertex("KE",7)

grafTestowy_1.add_undirected_edge(VI, CH)
grafTestowy_1.add_undirected_edge(VI, RU)
grafTestowy_1.add_undirected_edge(VI, PA)
grafTestowy_1.add_undirected_edge(RU, RA)
grafTestowy_1.add_undirected_edge(RU, SU)
grafTestowy_1.add_undirected_edge(RU, VI)
grafTestowy_1.add_undirected_edge(PA, CO)
grafTestowy_1.add_undirected_edge(PA, KE)
grafTestowy_1.add_undirected_edge(CO, RU)
grafTestowy_1.add_undirected_edge(CO, VI)
print(mutal_friends(grafTestowy_1, CO, RU))


grafTestowy_2 = Graph()
VI = grafTestowy_2.create_vertex("VI",0)
RU = grafTestowy_2.create_vertex("RU",1)
PA = grafTestowy_2.create_vertex("PA",2)
CO = grafTestowy_2.create_vertex("CO",3)
CH = grafTestowy_2.create_vertex("CH",4)

grafTestowy_2.add_undirected_edge(VI, CH)
grafTestowy_2.add_undirected_edge(VI, RU)
grafTestowy_2.add_undirected_edge(VI, CO)
grafTestowy_2.add_undirected_edge(VI, PA)
grafTestowy_2.add_undirected_edge(RU, PA)
grafTestowy_2.add_undirected_edge(RU, CH)
grafTestowy_2.add_undirected_edge(RU, CO)
grafTestowy_2.add_undirected_edge(PA, CH)
grafTestowy_2.add_undirected_edge(PA, CO)
grafTestowy_2.add_undirected_edge(CO, CH)
print(mutal_friends(grafTestowy_2, VI, RU))

grafTestowy_3 = Graph()
Vi = grafTestowy_3.create_vertex("Vitold",0)
Ru = grafTestowy_3.create_vertex("Ruslan",1)
Pa = grafTestowy_3.create_vertex("Paolo",2)
Co = grafTestowy_3.create_vertex("Cocojumbo",3)
Ch = grafTestowy_3.create_vertex("Chorazy",4)
Ra = grafTestowy_3.create_vertex("Racibor",5)
Su = grafTestowy_3.create_vertex("Sukkub",6)
Ke = grafTestowy_3.create_vertex("Keisuke",7)

grafTestowy_3.add_undirected_edge(Vi, Ru)
grafTestowy_3.add_undirected_edge(Ru, Pa)
grafTestowy_3.add_undirected_edge(Ru, Co)
grafTestowy_3.add_undirected_edge(Pa, Ch)
grafTestowy_3.add_undirected_edge(Pa, Ra)
grafTestowy_3.add_undirected_edge(Co, Su)
grafTestowy_3.add_undirected_edge(Co, Ke)
print(mutal_friends(grafTestowy_3, Pa, Ke))

grafTestowy_1.show()
grafTestowy_2.show()
grafTestowy_3.show()