import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph
from functions import is_complete

n = 10 

CompleteGraph = nx.complete_graph(n)
draw_graph(CompleteGraph,title=f"K{n}")
print(f'É completo? {"Sim" if is_complete(CompleteGraph) else "Não"}')
print(f"Vértices = {CompleteGraph.nodes}")
print(f"Arestas = {CompleteGraph.edges}")

n =10

CompleteGraph = nx.complete_graph(n)
draw_graph(CompleteGraph,layoutid="kamada_kawai_layout",title=f"K{n}")
print(f'É completo? {"Sim" if is_complete(CompleteGraph) else "Não"}')
print(f"Vértices = {CompleteGraph.nodes}")
print(f"Arestas = {CompleteGraph.edges}")
