import networkx as nx
import matplotlib.pyplot as plt

#não aparecem arestas paralelas
def draw_graph(S):
    nx.draw_networkx(S)
    plt.show()

def has_parallel_edges (G):
  for u in G.nodes:
    for v in G.nodes:
      if G.number_of_edges(u,v) > 1:
        return True
  return False

M = nx.MultiGraph()
M.add_edges_from([('x','y'),('x','y'),('y','x'),('x','w'),
                   ('y','w'),('z','w'),('w','z')])

print(M.is_multigraph())

print(f"Vértices: {M.nodes}")
print(f"Arestas: {M.edges}")

# Testando função com grafos S, M e G criados nas seções anteriores
print(f"M possui arestas paralelas? {'Sim' if has_parallel_edges(M) else 'Não'}")

# Desenhando o grafo
draw_graph(M)
