import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from functions import *

grafo = nx.Graph()
print(f"Grafo nulo: {grafo}")

grafo.add_nodes_from(['x','y','z','w'])
print(f"Vértices: {grafo.nodes}")

grafo.add_edges_from([('x','y'),('x','w'),('x','z'),('y','z')])
print(f"Arestas: {grafo.edges}")

draw_graph(grafo)
