import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

grafo = nx.DiGraph() #or grafo = nx.MultiDiGraph()
grafo.add_node('A')
grafo.add_node('B')
grafo.add_edge('A', 'B', length = 2)
grafo.add_edge('B', 'A', length = 3)

draw_graph(grafo)