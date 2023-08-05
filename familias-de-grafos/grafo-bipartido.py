import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph
from functions import is_complete_bipartite

grafo = nx.Graph()

grafo.add_nodes_from(['n0','n1','n2','n3', 'n4', 'n5'])

grafo.add_edges_from([('n0','n5'),('n0','n3'),('n0','n1'),('n1','n4'), ('n1','n2'),
                   ('n2','n5'), ('n2','n3'), ('n3','n4'), ('n5','n4')])


try:
  X,Y = nx.bipartite.sets(grafo)
except:
  c = nx.bipartite.color(grafo)
  X = {k for k in c.keys() if c[k]==0}
  Y = {k for k in c.keys() if c[k]==1}
draw_graph(grafo,layoutid="kamada_kawai_layout", title="Grafo Bipartido",
           nset=[X,Y], nsetcolor=["cyan",'pink'], nsetlabel=["X","Y"])


#exercicios

is_bc, X, Y = is_complete_bipartite(grafo)
if is_bc or X is not None:
  draw_graph(grafo,pos=nx.bipartite_layout(grafo,X),
               nset=[X,Y],nsetcolor=["cyan",'pink'],
               nsetlabel=["X","Y"])
  if is_bc:
    print("O grafo é bipartido completo.")
  else:
    print("O grafo é bipartido, mas não é bipartido completo.")
else:
    draw_graph(grafo)
    print("O grafo não é bipartido.")
