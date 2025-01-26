class PVGraph:
    def __init__(self):
        self.nodes = set()
        self.connections = {}

    def add_node(self, node):
        self.nodes.add(node)
        self.connections[node] = []

    def add_edge(self, node1, node2, bidirectional=True):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Both nodes must exists in the graph.")

        self.connections[node1].append(node2)
        if bidirectional:
            self.connections[node2].append(node1)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.connections.pop(node, default=None)
            for neighbors in self.connections.values():
                if node in neighbors:
                    neighbors.remove(node)

    def remove_edge(self, node1, node2, bidirectional=True):
        if node1 in self.connections:
            if node2 in self.connections[node1]:
                self.connections[node1].remove(node2)
        if bidirectional and node2 in self.connections:
            if node1 in self.connections[node2]:
                self.connections[node2].remove(node1)

    def get_neighbors(self, node):
        return self.connections.get(node, [])

    def has_edge(self, node1, node2):
        return node1 in self.connections and node2 in self.connections

    def __str__(self):
        representation = []
        for node, neighbors in self.connections.items():
            representation.append(f"{node} -> {neighbors}")
        return "\n".join(representation)

# graph_test = PVGraph()
# graph_test.add_node("NODE1")
# graph_test.add_node("NODE2")
# graph_test.add_edge("NODE1", "NODE2")

# print(graph_test)


