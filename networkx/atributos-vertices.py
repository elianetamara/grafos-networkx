import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

# desenhando grafo pra iteração
grafo = nx.Graph()

grafo.add_node('n0', label ='a')
grafo.add_node('n1', label ='b')
grafo.add_node('n2', label ='c')
grafo.add_node('n3', label ='d')
grafo.add_node('n4', label ='e')
grafo.add_node('n5', label ='f')

grafo.add_edge('n0','n1',label = 'ab')
grafo.add_edge('n1','n2',label = 'bc')
grafo.add_edge('n2','n3',label = 'cd')
grafo.add_edge('n3','n4',label = 'de')
grafo.add_edge('n2','n4',label = 'ce')
grafo.add_edge('n4','n5',label = 'ef')
draw_graph(grafo,layoutid="spring_layout")


# G.nodes[v][attr]
# Acessando e modificando o atributo label dos vértices
print(f"Dicionário com labels dos vértices (antes): {nx.get_node_attributes(grafo,'label')}")
# Alterando o label dos vértices
for v in grafo.nodes:
  grafo.nodes[v]['label'] = 'v' + grafo.nodes[v]['label']
print(f"Dicionário com labels dos vértices (novo): {nx.get_node_attributes(grafo,'label')}\n")

