from collections import deque

def bfs(graph, start_node):
    """
    Performs Breadth-First Search (BFS) traversal on a graph.
    
    :param graph: Dictionary representing the adjacency list.
    :param start_node: The node where the traversal begins.
    """
    # Track visited nodes to prevent infinite loops in cyclic graphs
    visited = set()
    
    # Initialize a FIFO queue with the starting node
    queue = deque([start_node])
    
    # Mark the start node as visited
    visited.add(start_node)
    
    print("BFS Traversal Order:", end=" ")
    
    # Loop continuously until there are no items left in the queue
    while queue:
        # Remove and return an item from the left side of the queue
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # Check all direct neighbors of the dequeued node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()  # Newline for cleaner output

# --- Example Usage ---
if __name__ == "__main__":
    # Define an unweighted graph using an adjacency list
    example_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Execute BFS starting from node 'A'
    bfs(example_graph, start_node='A')
