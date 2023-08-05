import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

grafo = nx.Graph()
edges = [(1, 2), (1, 6), (2, 3), (2, 4), (2, 6), 
         (3, 4), (3, 5), (4, 8), (4, 9), (6, 7)]
  
grafo.add_edges_from(edges)

draw_graph(grafo)
print("Total number of nodes: ", grafo.number_of_nodes())
print("Total number of edges: ", grafo.number_of_edges())
print("List of all nodes: ", list(grafo.nodes()))
print("List of all edges: ", list(grafo.edges(data = True)))
print("Degree for all nodes: ", dict(grafo.degree()))
print("List of all nodes we can go to in a single step from node 2: ",
                                                 list(grafo.neighbors(2)))