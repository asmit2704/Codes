def is_safe(node, color, colors, graph, n):
    for i in range(n):
        if graph[node][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring(node, colors, graph, m, n):

    if node == n:
        return True
    for color in range(1, m + 1):
        if is_safe(node, color, colors, graph, n):
            colors[node] = color
            if graph_coloring(node + 1, colors, graph, m, n):
                return True
            colors[node] = 0
    return False

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))
colors = [0] * n
if graph_coloring(0, colors, graph, m, n):

    print("\nSolution Exists")
    print("Assigned Colors are:")
    for i in range(n):
        print("Vertex", i, "-> Color", colors[i])
else:
    print("No Solution Exists")