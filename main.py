import networkx as nx
G = nx.Graph()

G.add_node(1)
G.add_node(2)

print(G.nodes())

G.add_edge(1, 2)

nVertices = G.number_of_nodes()
nArestas = G.number_of_edges()

print('vertices: ', nVertices, '\narestas: ', nArestas)