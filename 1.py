from collections import deque

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

def bfs(graph, start):
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {}

n = int(input("Enter number of vertices: "))
for i in range(n):
    vertex = input("Enter vertex name: ")
    graph[vertex] = []

e = int(input("Enter number of edges: "))

print("Enter edges (vertex1 vertex2):")

for i in range(e):
    v1, v2 = input().split()
    graph[v1].append(v2)
    graph[v2].append(v1)

while True:
    print("\n--- MENU ---")
    print("1. DFS Traversal")
    print("2. BFS Traversal")
    print("3. Display Graph")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        start = input("Enter starting vertex for DFS: ")
        visited = set()

        print("DFS Traversal:")
        dfs(graph, start, visited)
        print()

    elif choice == 2:
        start = input("Enter starting vertex for BFS: ")

        print("BFS Traversal:")
        bfs(graph, start)
        print()

    elif choice == 3:
        print("Graph:")
        for vertex in graph:
            print(vertex, "->", graph[vertex])

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")