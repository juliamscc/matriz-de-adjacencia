import networkx as nx
G = nx.Graph()

G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('e')

print(G.nodes())

G.add_edge('a','b')
G.add_edge('a','e')
G.add_edge('b','c')
G.add_edge('c','c')

nVertices = G.number_of_nodes()
nArestas = G.number_of_edges()

print('vertices: ', nVertices, '\narestas: ', nArestas)