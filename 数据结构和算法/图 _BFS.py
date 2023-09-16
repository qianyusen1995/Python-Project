from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

    def bfs(self, start):
        visited = set()          # 用集合记录已经访问过的节点
        queue = deque([start])   # 创建一个双端队列，并将起始节点放入队列
        visited.add(start)       # 标记起始节点为已访问

        while queue:
            vertex = queue.popleft()   # 弹出队首节点
            print(vertex, end=" ")    # 输出当前节点

            # 获取当前节点的邻居节点列表
            neighbors = self.graph.get(vertex, [])#尝试从字典self.graph中获取键 vertex 对应的值（即邻居节点列表），如果键不存在，则返回一个空列表 []。

            # 遍历邻居节点列表
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)  # 将未访问的邻居节点加入队列
                    visited.add(neighbor)   # 标记邻居节点为已访问

# 创建一个图实例
graph = Graph()

# 添加图的边
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# 从节点 'A' 开始进行广度优先搜索
#print (graph)
print("BFS starting from 'A':")
graph.bfs('A')
  #      A
  #    /   \
  #   B     C
  #  /       \
  # D         D
  #  \       /
  #   E     E