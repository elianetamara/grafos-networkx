import networkx as nx
import matplotlib.pyplot as plt
from utils import draw_graph

P = nx.MultiGraph()
P.add_edges_from([('x','y'),('x','y'),('x','w'),
                   ('y','w'),('z','w'),('w','w')])
print(f"Vértices: {P.nodes}")
print(f"Arestas: {P.edges}")

draw_graph(P)