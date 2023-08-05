import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

G4 = nx.Graph()


G4.add_node('n0')
G4.add_node('n1')
G4.add_node('n2')
G4.add_node('n3')
G4.add_node('n4')
G4.add_node('n5')

G4.add_edge('n0','n5')
G4.add_edge('n0','n3')
G4.add_edge('n0','n4')
G4.add_edge('n1','n2')
G4.add_edge('n1','n5')
G4.add_edge('n1','n4')
G4.add_edge('n2','n5')
G4.add_edge('n2','n3')
G4.add_edge('n3','n4')

draw_graph(G4)

lists = [ # sequências de vértices a serem testadas
    ['n0', 'n3', 'n0', 'n5'],
    ['n0', 'n3', 'n2', 'n5'],
    ['n1', 'n4', 'n3', 'n2', 'n1'],
    ['n2', 'n0', 'n4']]
for l in lists:
  if nx.is_path(G4,l):
    print(f"{l} é um passeio", end="; ")
  else:
    print(f"{l} não é um passeio", end="; ")
  if nx.is_simple_path(G4,l):
    print(f"é um caminho\n")
  else:
    print(f"não é um caminho\n")