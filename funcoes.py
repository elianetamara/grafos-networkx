import networkx as nx
import matplotlib.pyplot as plt
from utils import draw_graph

G = nx.Graph()
edges = [(1, 2), (1, 6), (2, 3), (2, 4), (2, 6), 
         (3, 4), (3, 5), (4, 8), (4, 9), (6, 7)]
  
G.add_edges_from(edges)

draw_graph(G)
print("Total number of nodes: ", G.number_of_nodes())
print("Total number of edges: ", G.number_of_edges())
print("List of all nodes: ", list(G.nodes()))
print("List of all edges: ", list(G.edges(data = True)))
print("Degree for all nodes: ", dict(G.degree()))
print("List of all nodes we can go to in a single step from node 2: ",
                                                 list(G.neighbors(2)))