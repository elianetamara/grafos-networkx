import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

GRegular = nx.random_regular_graph(4,6)
draw_graph(GRegular,layoutid="circular_layout")

GPetersen = nx.petersen_graph()
draw_graph(GPetersen,layoutid="kamada_kawai_layout", title="Grafo de Petersen")

GCubico = nx.cubical_graph()
draw_graph(GCubico,layoutid="spring_layout", title="Cubo")

d = 2
n = 7 

try:
  GRegular2 = nx.random_regular_graph(d,n)
  draw_graph(GRegular2,nx.kamada_kawai_layout(GRegular2))
except:
  print("Erro de configuração: 0 <= d < n ou d*n é ímpar.")

# lança exceção
d = 3
n = 7 

try:
  GRegular2 = nx.random_regular_graph(d,n)
  draw_graph(GRegular2,nx.kamada_kawai_layout(GRegular2))
except:
  print("Erro de configuração: 0 <= d < n ou d*n é ímpar.")
  print(f'd={d} e n={n} -> d*n = {d*n}; d < n ? {"Sim" if d < n else "Não"}')
