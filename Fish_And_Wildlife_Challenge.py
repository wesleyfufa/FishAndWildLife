from collections import defaultdict

from Edge import Edge
from Vertex import Vertex

def longest_path_dag(vertex):
    sorted_vertices = topological_sort(vertex)
    distances = defaultdict(lambda: float('-inf'))
    distances[vertex] = 0

    for v in sorted_vertices:
        for edge in v.adjacent_vertices:
            distances[edge.dest] = max(distances[edge.dest], distances[v] + 1)

    max_distance = max(distances.values())

    return max_distance

def topological_sort(vertex):
    visited = set()
    sorted_vertices = []

    def dfs(v):
        visited.add(v)
        for edge in v.adjacent_vertices:
            if edge.dest not in visited:
                dfs(edge.dest)
        sorted_vertices.append(v)

    dfs(vertex)
    sorted_vertices.reverse()
    return sorted_vertices

# Example usage:
if __name__ == "__main__":
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)

    e1 = Edge(v1, v2)
    e2 = Edge(v1, v3)
    e3 = Edge(v2, v4)
    e4 = Edge(v3, v4)

    v1.adjacent_vertices.extend([e1, e2])
    v2.adjacent_vertices.append(e3)
    v3.adjacent_vertices.append(e4)

    longest_path = longest_path_dag(v1)
    print("Longest directed path length:", longest_path)