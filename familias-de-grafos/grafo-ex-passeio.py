import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

grafo = nx.Graph()


grafo.add_nodes_from(['n0','n1','n2','n3', 'n4', 'n5'])

grafo.add_edges_from([('n0','n5'),('n0','n3'),('n0','n4'),('n1','n2'), ('n1','n5'),
                   ('n1','n4'), ('n2','n5'), ('n2','n3'), ('n3','n4')])


draw_graph(grafo)

lists = [ # sequências de vértices a serem testadas
    ['n0', 'n3', 'n0', 'n5'],
    ['n0', 'n3', 'n2', 'n5'],
    ['n1', 'n4', 'n3', 'n2', 'n1'],
    ['n2', 'n0', 'n4']]
for l in lists:
  if nx.is_path(grafo,l):
    print(f"{l} é um passeio", end="; ")
  else:
    print(f"{l} não é um passeio", end="; ")
  if nx.is_simple_path(grafo,l):
    print(f"é um caminho\n")
  else:
    print(f"não é um caminho\n")