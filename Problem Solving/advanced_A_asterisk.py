import heapq

def a_star_search(graph, heuristics, start, goal):
    """
    Implements the A* Search Algorithm to find the shortest path.
    
    :param graph: Dictionary representing the adjacency list {node: [(neighbor, edge_cost)]}
    :param heuristics: Dictionary representing the heuristic estimate from each node to the goal
    :param start: The starting node
    :param goal: The target destination node
    :return: A list of nodes representing the path, and the total cost. Returns None if no path is found.
    """
    # Priority queue stores tuples of format: (f_score, current_node)
    # It sorts elements primarily by f_score.
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start], start))
    
    # Track the lowest cost g(n) found from start to each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    # Keep track of the node paths for reconstruction
    parent_map = {start: None}
    
    # Set to keep track of fully explored nodes
    closed_set = set()

    while priority_queue:
        # Pop the node with the minimum f_score value
        current_f, current_node = heapq.heappop(priority_queue)
        
        # Early exit if the goal is reached
        if current_node == goal:
            path = []
            total_cost = g_score[goal]
            while current_node is not None:
                path.append(current_node)
                current_node = parent_map[current_node]
            return path[::-1], total_cost  # Return reversed path and cost
            
        # Skip processing if we already found a better path for this node
        if current_node in closed_set:
            continue
            
        closed_set.add(current_node)
        
        # Explore neighbors of the current node
        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor in closed_set:
                continue
                
            # Calculate tentative g(n) score for the neighbor
            tentative_g = g_score[current_node] + edge_cost
            
            # If a shorter path to neighbor is found, update records
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                parent_map[neighbor] = current_node
                
                # f(n) = g(n) + h(n)
                f_score = tentative_g + heuristics.get(neighbor, 0)
                heapq.heappush(priority_queue, (f_score, neighbor))
                
    return None, float('inf')  # No path exists


# --- Example Execution Graph Setup ---
# The graph map weights and node relationships
example_graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

# Heuristic estimates h(n) to the goal node 'J'
example_heuristics = {
    'A': 11, 'B': 6, 'C': 5, 'D': 7, 'E': 3, 
    'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
}

# Run the algorithm from Node A to Node J
start_node = 'A'
goal_node = 'J'
optimal_path, path_cost = a_star_search(example_graph, example_heuristics, start_node, goal_node)

print(f"Optimal Path: {optimal_path}")
print(f"Total Cost: {path_cost}")
