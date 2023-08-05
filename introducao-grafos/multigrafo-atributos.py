import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

grafo = nx.MultiGraph()

grafo.add_node('n0', label ='a', fillcolor = 'grey')
grafo.add_node('n1', label ='b', fillcolor = 'blue')
grafo.add_node('n2', label ='c', fillcolor = 'darkgreen')
grafo.add_node('n3', label ='d', fillcolor = 'red')

grafo.add_edge('n0','n1',label = 'ab')
grafo.add_edge('n1','n2',label = 'bc')
grafo.add_edge('n0','n3',label = 'ad')
grafo.add_edge('n1','n3',label = 'bd')
grafo.add_edge('n2','n3',label = 'cd1')
grafo.add_edge('n2','n3',label = 'cd2')

print(grafo.nodes(data=True))
print(grafo.edges)
print(grafo.edges(data=True))

draw_graph(grafo, node_labels=nx.get_node_attributes(grafo,'label'))