# Graph Coloring using Backtracking

def is_safe(vertex, color, graph, colors):
    # Check all adjacent vertices
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True


def graph_coloring(vertex, graph, m, colors):
    # All vertices are colored
    if vertex == len(graph):
        return True

    # Try each color
    for color in range(1, m + 1):

        if is_safe(vertex, color, graph, colors):
            colors[vertex] = color

            # Recursively color the next vertex
            if graph_coloring(vertex + 1, graph, m, colors):
                return True

            # Backtrack
            colors[vertex] = 0

    return False


# 4-vertex graph
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# Number of vertices
n = 4

# Number of colors
m = 3

# Initially no vertex is colored
colors = [0] * n

# Run graph coloring
if graph_coloring(0, graph, m, colors):
    print("Valid coloring found!")
    for i in range(n):
        print("Vertex", i + 1, "-> Color", colors[i])
else:
    print("No valid coloring possible.")