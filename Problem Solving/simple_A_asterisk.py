import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue stores (f_cost, g_cost, current_node, path)
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while priority_queue:
        f_cost, g_cost, current_node, path = heapq.heappop(priority_queue)

        # Goal reached
        if current_node == goal:
            return path, g_cost

        if current_node in visited:
            continue

        visited.add(current_node)

        # Explore neighbors
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                new_g = g_cost + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(priority_queue,
                               (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')


# Sample Graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

path, cost = a_star(graph, start, goal, heuristic)

if path:
    print("Goal reached!")
    print("Path :", " -> ".join(path))
    print("Total Cost :", cost)
else:
    print("No path found.")