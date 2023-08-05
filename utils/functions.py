import networkx as nx
import matplotlib.pyplot as plt

def is_complete_bipartite(G):
  if nx.bipartite.is_bipartite(G):
    X,Y = nx.bipartite.sets(G)
    if nx.bipartite.density(G,X) == 1:
      return True, X, Y
    else:
      return False, X, Y
  else:
    return False, None, None
  
def is_complete (G):
  return all(G.number_of_edges(x,y)==1 for x in G.nodes for y in G.nodes if x != y)

def has_parallel_edges (G):
  for u in G.nodes:
    for v in G.nodes:
      if G.number_of_edges(u,v) > 1:
        return True
  return False

#não aparecem arestas paralelas
def draw_graph(S):
    nx.draw_networkx(S)
    plt.show()