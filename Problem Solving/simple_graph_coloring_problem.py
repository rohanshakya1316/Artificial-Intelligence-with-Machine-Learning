# Python Program for Graph Coloring using 4 Colors

# Function to check if assigning a color is safe
def is_safe(node, graph, colors, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

# Backtracking function
def graph_coloring(graph, m, colors, node):

    # If all vertices are colored
    if node == len(graph):
        return True

    # Try all colors
    for color in range(1, m + 1):
        if is_safe(node, graph, colors, color):
            colors[node] = color

            if graph_coloring(graph, m, colors, node + 1):
                return True

            # Backtrack
            colors[node] = 0

    return False


# Main Program

# Graph represented as adjacency list
graph = [
    [1, 2],        # Vertex 0
    [0, 2, 3],     # Vertex 1
    [0, 1, 3],     # Vertex 2
    [1, 2]         # Vertex 3
]

# Graph Used: Each connected vertex must have a different color. 
#       (0)
#      /   \
#    (1)---(2)
#       \   /
#        (3)

m = 4                      # Number of colors
colors = [0] * len(graph)  # Initially all vertices are uncolored

if graph_coloring(graph, m, colors, 0):
    print("Color Assignment:")
    for i in range(len(graph)):
        print("Vertex", i, "-> Color", colors[i])
else:
    print("No solution exists.")