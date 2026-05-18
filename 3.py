import sys

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Sorted Array:", arr)

def prim_mst(graph, n):
    selected = [False] * n
    selected[0] = True
    print("\nEdges in Prim's MST:")
    for i in range(n - 1):
        minimum = sys.maxsize
        x = 0
        y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if (not selected[j]) and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(x, "-", y, "=", graph[x][y])
        selected[y] = True

def dijkstra(graph, start):
    n = len(graph)
    distance = [sys.maxsize] * n
    visited = [False] * n
    distance[start] = 0
    for i in range(n):
        minimum = sys.maxsize
        u = -1
        for j in range(n):
            if not visited[j] and distance[j] < minimum:
                minimum = distance[j]
                u = j
        visited[u] = True
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]
    print("\nShortest Distances:")
    for i in range(n):
        print("Node", i, "=", distance[i])

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * max_deadline
    profit = 0
    for job in jobs:
        for j in range(job[1] - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job[0]
                profit += job[2]
                break
    print("\nJob Sequence:")
    for job in slots:
        if job != -1:
            print(job, end=" ")
    print("\nTotal Profit:", profit)

while True:
    print("\n===== GREEDY ALGORITHMS MENU =====")
    print("1. Selection Sort")
    print("2. Prim's Minimum Spanning Tree")
    print("3. Dijkstra Shortest Path")
    print("4. Job Scheduling")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        arr = list(map(int, input("Enter elements: ").split()))
        selection_sort(arr)
   
    elif choice == 2:
        n = int(input("Enter number of vertices: "))
        print("Enter adjacency matrix:")
        graph = []
        for i in range(n):
            row = list(map(int, input().split()))
            graph.append(row)
        prim_mst(graph, n)
    
    elif choice == 3:
        n = int(input("Enter number of vertices: "))
        print("Enter adjacency matrix:")
        graph = []
        for i in range(n):
            row = list(map(int, input().split()))
            graph.append(row)
        start = int(input("Enter starting node: "))
        dijkstra(graph, start)
    elif choice == 4:
        n = int(input("Enter number of jobs: "))
        jobs = []
        print("Enter JobID Deadline Profit")
        for i in range(n):
            job_id = input("Job ID: ")
            deadline = int(input("Deadline: "))
            profit = int(input("Profit: "))
            jobs.append((job_id, deadline, profit))
        job_scheduling(jobs)

    elif choice == 5:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")