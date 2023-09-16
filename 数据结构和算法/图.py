class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

    def show_edges(self):
        for vertex in self.graph:
            neighbors = self.graph[vertex]
            for neighbor in neighbors:
                print(f"{vertex} -> {neighbor}")

# 创建一个图实例
graph = Graph()

# 添加图的边
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# 显示图的边
graph.show_edges()