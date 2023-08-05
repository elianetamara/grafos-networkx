import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

G4 = nx.Graph()


G4.add_node('n0', label ='a', fillcolor = 'grey')
G4.add_node('n1', label ='b', fillcolor = 'blue')
G4.add_node('n2', label ='c', fillcolor = 'darkgreen')
G4.add_node('n3', label ='d', fillcolor = 'red')

G4.add_edge('n0','n1',label = 'ab')
G4.add_edge('n1','n2',label = 'bc')
G4.add_edge('n0','n3',label = 'ad')
G4.add_edge('n1','n3',label = 'bd')
G4.add_edge('n2','n3',label = 'cd')

print(G4.nodes(data=True))
print(G4.edges(data=True))
print(nx.get_node_attributes(G4,'label'))

draw_graph(G4, node_labels=nx.get_node_attributes(G4,'label'), edge_labels=nx.get_edge_attributes(G4,'label'))