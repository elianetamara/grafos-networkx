import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

# desenhando grafo pra iteração
grafo = nx.MultiGraph()

grafo.add_node('n0', label ='a')
grafo.add_node('n1', label ='b')
grafo.add_node('n2', label ='c')
grafo.add_node('n3', label ='d')
grafo.add_node('n4', label ='e')
grafo.add_node('n5', label ='f')

grafo.add_edge('n0','n1',label = 'ab')
grafo.add_edge('n2','n2',label = 'cc')
grafo.add_edge('n2','n1',label = 'cb')
grafo.add_edge('n4','n3',label = 'de')
grafo.add_edge('n4','n3',label = 'de')
grafo.add_edge('n3','n0',label = 'ad')
grafo.add_edge('n2','n4',label = 'ce')
grafo.add_edge('n1','n5',label = 'bf')
draw_graph(grafo,layoutid="spring_layout")

print(type(grafo))

# Imprimindo arestas (quando existir) entre os vértices u e v
# Se Graph, imprime o dicionário de atributos da aresta
# Se Multigraph, imprime um dicionário de arestas, indexado pelo identificador da aresta
u = list(grafo.nodes)[0]
v = list(grafo.nodes)[1]
if grafo.number_of_edges(u,v) >= 1:
  print(f"Aresta(s) entre {u} e {v}: {grafo[u][v]}") # a ordem em que u e v são considerados não importa

# Adicionando o atributo 'label' a arestas
print(f"\nDicionário com labels das arestas (antes): {nx.get_edge_attributes(grafo,'label')}")
if type(grafo) is nx.classes.multigraph.MultiGraph: #Class Multigraph
  for u,v,k in grafo.edges: # necessário referenciar também o id da aresta
    grafo[u][v][k]['label'] = grafo.nodes[u]['label'] + grafo.nodes[v]['label'] + str(k)
  print(f"Dicionário com labels das arestas (novo): {nx.get_edge_attributes(grafo,'label')}")
else: # Class Graph
  for u,v in grafo.edges: # arestas não têm id
    grafo[u][v]['label'] = grafo.nodes[u]['label'] + grafo.nodes[v]['label']
  print(f"Dicionário com labels das arestas (novo): {nx.get_edge_attributes(grafo,'label')}")
