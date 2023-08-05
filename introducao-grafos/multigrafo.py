import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from functions import *


multigrafo = nx.MultiGraph()
multigrafo.add_edges_from([('x','y'),('x','y'),('y','x'),('x','w'),
                   ('y','w'),('z','w'),('w','z')])

print(multigrafo.is_multigraph())

print(f"Vértices: {multigrafo.nodes}")
print(f"Arestas: {multigrafo.edges}")
print(f"multigrafo possui arestas paralelas? {'Sim' if has_parallel_edges(multigrafo) else 'Não'}")

draw_graph(multigrafo)
