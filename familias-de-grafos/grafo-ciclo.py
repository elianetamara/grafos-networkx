import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

GrafoCiclo = nx.cycle_graph(10)
draw_graph(GrafoCiclo,title="Grafo Ciclo")
print(f"V = {GrafoCiclo.nodes}")
print(f"E = {GrafoCiclo.edges}")

GrafoCiclo = nx.cycle_graph(2)
draw_graph(GrafoCiclo,title="Grafo Ciclo")
print(f"V = {GrafoCiclo.nodes}")
print(f"E = {GrafoCiclo.edges}")

print("\ntestando layouts:")

GrafoCiclo = nx.cycle_graph(100)
draw_graph(GrafoCiclo,title="Grafo Ciclo")
print(f"V = {GrafoCiclo.nodes}")
print(f"E = {GrafoCiclo.edges}")

GrafoCiclo = nx.cycle_graph(100)
draw_graph(GrafoCiclo,layoutid="kamada_kawai_layout",title="Grafo Ciclo")
print(f"V = {GrafoCiclo.nodes}")
print(f"E = {GrafoCiclo.edges}")
