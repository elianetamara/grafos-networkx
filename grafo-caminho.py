import networkx as nx
from utils import draw_graph

n = 9 

PathGraph = nx.path_graph(n)
draw_graph(PathGraph,layoutid="kamada_kawai_layout", title="Grafo Caminho")
print(f"Vértices= {PathGraph.nodes}")
print(f"Arestas= {PathGraph.edges}")

PathGraph = nx.path_graph(n)
draw_graph(PathGraph, title="Grafo Caminho")
print(f"Vértices= {PathGraph.nodes}")
print(f"Arestas= {PathGraph.edges}")