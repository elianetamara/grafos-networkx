import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph


grafo = nx.Graph()

grafo.add_nodes_from(['a','b','c','d', 'e', 'f', 'g'])

grafo.add_edges_from([('a','b'),('a','c'),('b','d'),('c','d'), ('d','e'),
                   ('d','f'), ('f','g'), ('e','g')])

draw_graph(grafo,layoutid="kamada_kawai_layout")
