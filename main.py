# Leitura do arquivo .txt
with open("graph.txt", "r") as arquivo:
	text = arquivo.read()

# Função para criar a lista de vértices
def createListOfNodes(graph):
	nodes = graph[0].split(' ')
	return nodes

# Função para criar a lista de arestas
def createListOfEdges(graph):
	listofedges = graph[1:]
	edges = []
	for i in listofedges:
		e = i.split(' ')
		edge = tuple(e)
		edges.append(edge)
	return edges

graph = text.split('\n')

nodes = createListOfNodes(graph)
edges = createListOfEdges(graph)

# Função para criar a matriz de adjacência
def adjacency_matrix(nodes, edges):
    matrix = []
    line = []
    i = 0
    j = 0

    while i < len(nodes):
        while j < len(nodes):
            if ((nodes[i], nodes[j]) in edges or (nodes[j], nodes[i]) in edges):
                line.append(1)
            else:
                line.append(0)
            j += 1
        matrix.append(line)
        line = []
        i += 1
        j = 0

    return matrix

print(adjacency_matrix(nodes, edges))