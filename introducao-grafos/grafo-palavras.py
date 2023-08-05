import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

def adjacentes (p1,p2):
    lp1 = len(p1)
    lp2 = len(p2)
    limit = min(lp1,lp2)
    diff = abs(lp1-lp2)
    i = 0
    while diff<=1 and i < limit:
      if (p1[i]!=p2[i]):
          diff = diff + 1
      i = i + 1
    return diff==1 

def grafo_palavras (palavras):
  G = nx.Graph()
  palavras_unicas = list(set(palavras))
  G.add_nodes_from(palavras_unicas)
  for i in range(len(palavras_unicas)):
    for j in range(i+1,len(palavras_unicas)):
      if adjacentes(palavras_unicas[i],palavras_unicas[j]):
        G.add_edge(palavras_unicas[i],palavras_unicas[j])
  return G

GP = grafo_palavras(['caiado', 'cavado', 'cavalo', 'girafa', 'ralo', 'ramo', 'rata', 'rato', 'remo', 'reta', 'reto', 'rota', 'vaiado', 'varado', 'virada', 'virado', 'virava'])
draw_graph(GP,layoutid="circular_layout")