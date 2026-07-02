import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue holds (cumulative_cost, current_node, path_taken)
    priority_queue = [(0, start, [start])]
    visited = set()
    
    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)
        
        if current_node == goal:
            return cost, path
            
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        # Explore neighbors, prioritizing lowest cost
        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))
                
    return float('inf'), []

# Sample Graph Implementation
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('G', 6)],
    'D': [('G', 3)],
    'E': [('D', 1), ('G', 5)]
}
start, goal = 'A', 'G'
cost, path = uniform_cost_search(graph, start, goal)
print(f"Path: {path}, Cost: {cost}")
