import networkx as nx
from utils import draw_graph

n = 8

EmptyGraph = nx.empty_graph(n)
draw_graph(EmptyGraph,layoutid="kamada_kawai_layout", title="Grafo Vazio")
print(f"V = {EmptyGraph.nodes}")
print(f"E = {EmptyGraph.edges}")


n = 6

EmptyGraph = nx.empty_graph(n)
draw_graph(EmptyGraph, title="Grafo Vazio")
print(f"V = {EmptyGraph.nodes}")
print(f"E = {EmptyGraph.edges}")

