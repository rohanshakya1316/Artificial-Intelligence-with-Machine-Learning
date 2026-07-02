# Python Program for Breadth First Search (BFS)

from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS function
def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Create a queue and add the starting node
    visited.add(start)

    while queue:
        node = queue.popleft()   # Remove the first node from the queue
        print(node, end=" ")

        # Visit all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main Program
print("BFS Traversal:")
bfs(graph, 'A')