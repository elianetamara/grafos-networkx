import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(S):
    nx.draw_networkx(S)
    plt.show()

S = nx.Graph()
print(f"Grafo nulo: {S}")

S.add_nodes_from(['x','y','z','w'])
print(f"Vértices: {S.nodes}")

S.add_edges_from([('x','y'),('x','w'),('x','z'),('y','z')])
print(f"Arestas: {S.edges}")

draw_graph(S)
