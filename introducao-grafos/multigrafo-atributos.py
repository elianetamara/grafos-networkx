import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

G8 = nx.MultiGraph()

G8.add_node('n0', label ='a', fillcolor = 'grey')
G8.add_node('n1', label ='b', fillcolor = 'blue')
G8.add_node('n2', label ='c', fillcolor = 'darkgreen')
G8.add_node('n3', label ='d', fillcolor = 'red')

G8.add_edge('n0','n1',label = 'ab')
G8.add_edge('n1','n2',label = 'bc')
G8.add_edge('n0','n3',label = 'ad')
G8.add_edge('n1','n3',label = 'bd')
G8.add_edge('n2','n3',label = 'cd1')
G8.add_edge('n2','n3',label = 'cd2')

print(G8.nodes(data=True))
print(G8.edges)
print(G8.edges(data=True))

draw_graph(G8, node_labels=nx.get_node_attributes(G8,'label'))