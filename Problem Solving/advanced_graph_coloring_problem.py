def is_safe(graph, vertex, color_list, color):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color_list[i] == color:
            return False
    return True

def graph_coloring_util(graph, m, color_list, vertex):
    if vertex == len(graph):
        return True

    for color in range(1, m + 1):
        if is_safe(graph, vertex, color_list, color):
            color_list[vertex] = color
            
            if graph_coloring_util(graph, m, color_list, vertex + 1):
                return True

            color_list[vertex] = 0
    return False

def solve_graph_coloring(graph, m):
    color_list = [0] * len(graph)
    if not graph_coloring_util(graph, m, color_list, 0):
        print("Solution does not exist.")
        return False

    print("Solution exists. The assigned colors are:")
    for vertex in range(len(graph)):
        print(f"Vertex {vertex}: Color {color_list[vertex]}")
    return True

# A 4-vertex connected graph example
graph = [
    [0, 1, 0, 1],  # Vertex 0 connects to Vertex 1 and 3
    [1, 0, 1, 0],  # Vertex 1 connects to Vertex 0 and 2
    [0, 1, 0, 1],  # Vertex 2 connects to Vertex 1 and 3
    [1, 0, 1, 0]   # Vertex 3 connects to Vertex 0 and 2
]
m = 4 

solve_graph_coloring(graph, m)
