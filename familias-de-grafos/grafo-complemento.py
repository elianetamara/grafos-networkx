import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

grafo = nx.Graph()

grafo.add_nodes_from(['n0','n1','n2'])
grafo.add_edges_from([('n0','n1'),('n2','n1')])

print("\n grafo ex 1")
draw_graph(grafo,layoutid="circular_layout")

grafoComplemento = nx.complement(grafo)

print("\ncomplemento:")
draw_graph(grafoComplemento,layoutid="circular_layout")

#############################################################

grafoA = nx.Graph()

grafoA.add_nodes_from(['a','b','c','d', 'e', 'f', 'g'])
grafoA.add_edges_from([('a','b'),('a','c'),('b','d'),('c','d'), ('d','e'),
                   ('d','f'), ('f','g'), ('e','g')])

print("\n grafo ex 2")
draw_graph(grafoA,layoutid="kamada_kawai_layout")

grafoComplementoA = nx.complement(grafoA)

print("\ncomplemento:")
draw_graph(grafoComplementoA,layoutid="circular_layout")
