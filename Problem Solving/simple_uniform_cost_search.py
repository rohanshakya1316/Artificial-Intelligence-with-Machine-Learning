# Python Program for Uniform Cost Search (UCS)

import heapq

# Graph represented as an adjacency list with edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Uniform Cost Search Function
def uniform_cost_search(graph, start, goal):
    # Priority queue stores (cost, node)
    priority_queue = [(0, start)]

    # Keep track of visited nodes
    visited = set()

    while priority_queue:
        # Remove node with the lowest cost
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        print(f"Visited Node: {node}, Cost: {cost}")

        visited.add(node)

        # Goal test
        if node == goal:
            print("\nGoal Reached!")
            print("Minimum Cost =", cost)
            return

        # Add neighbors to the priority queue
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor))

    print("Goal not found.")

# Main Program
start = 'A'
goal = 'F'

print("Uniform Cost Search Traversal:\n")
uniform_cost_search(graph, start, goal)