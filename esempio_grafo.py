import networkx as nx
import flet as ft

from Amico import Amico

g = nx.Graph() # Grafo semplice

# g.add_node("abc")
# f.add_node(ft.Text())
# a = Amico(2345, "M. Rossi")
# g.add_node(a)

g.add_node(1)
g.add_node(2)

#g.add_edge(1, 2)
g.add_edge(1, 2, attributo = "pippo")
g.add_edge(2, 3)
# g.add_edge(2, 3) # Non avrebbe effetto su un grafo smeplice

print(f"Arco tra 1 e 2: {g[1][2]}")

altri_nodi = [4, 5, 8, 6, 7]
g.add_nodes_from(altri_nodi)

altri_archi = [ (2, 4), (4, 5), (6, 7), (6, 8) , (1,4) ]
g.add_edges_from(altri_archi)

print(g)

print(g.nodes)
print(g.edges)

primo_nodo = g[1] # Dizionario
print(primo_nodo)

if 12 in g:
    print("Nodo presente")
else:
    print("Nodo assente")

# Stampo i nodi
for nodo in g:
    print(nodo)

print("Stampo i vicini del nodo 1")
for nodo in g[1]:
    print(nodo)

densita = nx.density(g)
print(f"Densita: {densita}")

dg = nx.DiGraph() # Grafo diretto
dg.add_nodes_from(altri_nodi)
dg.add_edges_from(altri_archi)
print(dg.edges)
print(dg[4]) # Mi dice che esiste un archo verso 5
print(dg[5]) # Mi diche non esistono archi

mg = nx.MultiGraph()
mg.add_edge(1, 2, weight=5) #0
mg.add_edge(1, 2) #1
mg.add_edge(1, 2) #2
print(mg[1])
print(f"Arco tra 1 e 2 0-mo: {mg[1][2][0]}")