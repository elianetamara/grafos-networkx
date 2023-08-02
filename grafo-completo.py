import networkx as nx
from utils import draw_graph

n = 10 

CompleteGraph = nx.complete_graph(n)
draw_graph(CompleteGraph,title=f"K{n}")
print(f"Vértices = {CompleteGraph.nodes}")
print(f"Arestas = {CompleteGraph.edges}")

n =10

CompleteGraph = nx.complete_graph(n)
draw_graph(CompleteGraph,layoutid="kamada_kawai_layout",title=f"K{n}")
print(f"Vértices = {CompleteGraph.nodes}")
print(f"Arestas = {CompleteGraph.edges}")
