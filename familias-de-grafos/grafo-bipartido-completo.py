import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

BipartidoCompleto = nx.complete_multipartite_graph(3,3)

X,Y = nx.bipartite.sets(BipartidoCompleto)
draw_graph(BipartidoCompleto,nx.bipartite_layout(BipartidoCompleto,X),
           title=f"K{3},{3}",
           nset=[X,Y],nsetcolor=["cyan","pink"],nsetlabel=["X","Y"])


BCEstrela = nx.complete_multipartite_graph(1,5)

X,Y = nx.bipartite.sets(BCEstrela)
draw_graph(BCEstrela,nx.bipartite_layout(BCEstrela,X),
           title=f"K{1},{5}",
           nset=[X,Y],nsetcolor=["cyan","pink"],nsetlabel=["X","Y"])