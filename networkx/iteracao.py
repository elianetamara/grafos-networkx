import networkx as nx
import sys
sys.path.append("/home/eliane/ufcg/grafos-networkx/utils")
from utils import draw_graph

# desenhando grafo pra iteração
grafo = nx.Graph()
grafo.add_nodes_from(['a','b','c','d', 'e', 'f', 'g'])
grafo.add_edges_from([('a','b'),('a','c'),('b','d'),
                      ('c','d'), ('d','g'), ('f','g'), 
                      ('e','g'), ('e', 'f')])
draw_graph(grafo,layoutid="kamada_kawai_layout")


# (1) Imprimindo os vizinhos de cada vértice
print("Vizinhos: ")
for v in grafo.nodes:
  # neighbors retorna um iterator; função list cria a lista dos elementos
  print(f"  {v}: {list(grafo.neighbors(v))}")

# (2) Iterando sobre as arestas (u,v)
print("\nVizinhos comuns ...")
for u,v,*k in grafo.edges: # k é o identificador de aresta em objetos MultiGraph
  # common_neighbors retorna um generator (tipo especial de iterator que é lazy)
  # list força a construção da lista de elementos
  print(f"...entre {u} e {v}: {list(nx.common_neighbors(grafo,u,v))}")

# (3) Usando list comprehension para imprimir os graus máximo, mínimo e médio
degrees = [grafo.degree(v) for v in grafo.nodes] # lista com os graus dos vértices
print(f"\nGrau máximo do grafo: {max(degrees)}")
print(f"Grau mínimo do grafo: {min(degrees)}")
print(f"Grau médio do grafo: {sum(degrees)/grafo.number_of_nodes():.2f}")
