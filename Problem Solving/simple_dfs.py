# Python Program for Depth First Search (DFS)

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS function
def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)

        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Main Program
visited = set()

print("DFS Traversal:")
dfs(graph, 'A', visited)