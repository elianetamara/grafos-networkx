import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

pseudografo = nx.MultiGraph()
pseudografo.add_edges_from([('x','y'),('x','y'),('x','w'),
                   ('y','w'),('z','w'),('w','w')])
print(f"Vértices: {pseudografo.nodes}")
print(f"Arestas: {pseudografo.edges}")

draw_graph(pseudografo)