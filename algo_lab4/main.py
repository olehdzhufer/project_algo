from queue import Queue
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def collecting_vertex_in_graph(self):
        collections_vertex = set()
        for vertex in self.graph:
            collections_vertex.add(vertex)
        return collections_vertex

    def BFS(self, node):
        visited = set()
        queue = Queue()
        counter = 0
        pending_nodes = set()
        if node not in visited:
            queue.put(node)
            while not queue.empty():
                v = queue.get()
                visited.add(v)
                counter+=1

                for g in self.graph[v]:
                    if g not in visited:
                        if g not in pending_nodes:
                            queue.put(g)
                            pending_nodes.add(g)

            if len(self.graph.keys()) == counter:
                return node
        return -1


if __name__ == '__main__':
    g = Graph()

    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            u, v = map(int, line.split())
            g.addEdge(u, v)
        arg = g.collecting_vertex_in_graph()

    with open("output.txt", "w") as file:
        for node in arg:
            result = g.BFS(node)
            if result != -1:
                file.write(str(result))

