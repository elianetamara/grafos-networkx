import networkx as nx

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

