import heapq

def greedy_best_first_search(graph, start, goal, heuristics):
    """
    Implements the Greedy Best-First Search algorithm.
    
    :param graph: Dict representing the adjacency list {node: [neighbors]}
    :param start: The starting node
    :param goal: The target node
    :param heuristics: Dict containing straight-line distance estimates to the goal
    :return: A list of nodes forming the path from start to goal, or None if no path exists
    """
    # Priority Queue stores tuples format: (heuristic_value, current_node, path_taken)
    priority_queue = []
    
    # Push the initial state into the queue
    heapq.heappush(priority_queue, (heuristics[start], start, [start]))
    
    # Set to keep track of visited nodes to avoid infinite loops
    visited = set()
    
    while priority_queue:
        # Pop the node with the lowest heuristic value (greedy choice)
        h_val, current_node, path = heapq.heappop(priority_queue)
        
        # Check if we have reached our target
        if current_node == goal:
            return path
            
        # Process neighbors if the current node hasn't been visited yet
        if current_node not in visited:
            visited.add(current_node)
            
            # Explore all adjacent neighbors
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    # The cost is determined strictly by the neighbor's heuristic value
                    heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, path + [neighbor]))
                    
    return None  # Path not found


# --- Example Execution Workflow ---
if __name__ == "__main__":
    # Define a sample road map graph layout
    # Each key maps to an array of reachable neighboring nodes
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': ['H'],
        'F': [],
        'G': ['I'],
        'H': [],
        'I': []
    }
    
    # Define estimated heuristic costs (e.g., straight-line distance to goal 'I')
    heuristics = {
        'A': 40,
        'B': 32,
        'C': 25,
        'D': 35,
        'E': 19,
        'F': 17,
        'G': 10,
        'H': 12,
        'I': 0   # Goal state has a heuristic value of 0
    }
    
    start_node = 'A'
    goal_node = 'I'
    
    # Run the search algorithm
    result_path = greedy_best_first_search(graph, start_node, goal_node, heuristics)
    
    # Output the tracking results
    if result_path:
        print(f"Goal reached! Path taken: {' -> '.join(result_path)}")
    else:
        print("No path found to the goal node.")
