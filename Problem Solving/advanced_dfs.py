#      A
#     / \
#    B   C
#   / \   \
#  D   E   F


class Graph:
    def __init__(self):
        # Use a dictionary to store the adjacency list of the graph
        self.graph = {}

    def add_edge(self, u, v):
        # Add vertex v to u's list. If u doesn't exist, initialize it.
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
            
        self.graph[u].append(v)
        # Uncomment the line below if you want an undirected graph
        # self.graph[v].append(u)

    def dfs_recursive(self, start_node, visited=None):
        # Initialize the visited set on the first call
        if visited is None:
            visited = set()

        # Mark the current node as visited and process it
        visited.add(start_node)
        print(start_node, end=" ")

        # Recur for all adjacent vertices that haven't been visited
        for neighbor in self.graph.get(start_node, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start_node):
        visited = set()
        # Use a standard list as a LIFO stack
        stack = [start_node]

        while stack:
            # Pop the last element added (LIFO)
            node = stack.pop()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                # Add unvisited neighbors to the stack in reverse order 
                # to maintain the same traversal order as the recursive approach
                neighbors = self.graph.get(node, [])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)


# --- Driver Code to Test the Implementation ---
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    print("DFS Traversal (Recursive) starting from node 'A':")
    g.dfs_recursive('A')
    print("\n")

    print("DFS Traversal (Iterative) starting from node 'A':")
    g.dfs_iterative('A')
    print()
