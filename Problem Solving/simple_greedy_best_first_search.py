# Python Program for Greedy Best-First Search

import heapq

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic values (estimated cost to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

# Greedy Best-First Search Function
def greedy_best_first_search(graph, heuristic, start, goal):
    # Priority queue stores (heuristic, node)
    priority_queue = [(heuristic[start], start)]

    visited = set()

    while priority_queue:
        h, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        print("Visited:", node)

        visited.add(node)

        # Goal test
        if node == goal:
            print("\nGoal Reached!")
            return

        # Add neighbors based on heuristic value
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue,
                               (heuristic[neighbor], neighbor))

    print("Goal not found.")

# Main Program
start = 'A'
goal = 'G'

print("Greedy Best First Search Traversal:\n")
greedy_best_first_search(graph, heuristic, start, goal)