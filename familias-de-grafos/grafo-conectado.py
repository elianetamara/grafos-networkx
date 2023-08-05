import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph


grafoA = nx.Graph()

grafoA.add_nodes_from(['a','b','c', 'd', 'e'])
grafoA.add_edges_from([('a','b'),('a','c'),('b','c'), ('d', 'e')])

print(f'Grafo é conectado? {"Sim" if nx.is_connected(grafoA) else "Não"}')
draw_graph(grafoA,layoutid="kamada_kawai_layout")


grafoB = nx.Graph()

grafoB.add_nodes_from(['a','b','c'])
grafoB.add_edges_from([('a','b'),('a','c'),('b','c')])

print(f'Grafo é conectado? {"Sim" if nx.is_connected(grafoB) else "Não"}')
draw_graph(grafoB,layoutid="kamada_kawai_layout")

grafoC = nx.Graph()

grafoC.add_nodes_from(['d', 'e'])
grafoC.add_edges_from([('d', 'e')])

print(f'Grafo é conectado? {"Sim" if nx.is_connected(grafoC) else "Não"}')
draw_graph(grafoC,layoutid="kamada_kawai_layout")

grafoD = nx.Graph()

grafoD.add_nodes_from(['a','b','c', 'd', 'e'])
grafoD.add_edges_from([('a','b'),('a','c'),('b','c'), ('d', 'e'), ('e', 'c')])

print(f'Grafo é conectado? {"Sim" if nx.is_connected(grafoD) else "Não"}')
draw_graph(grafoD,layoutid="kamada_kawai_layout")