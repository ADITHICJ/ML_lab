from queue import PriorityQueue

def best_first_search(graph, heuristic, start, goal):
    pq = PriorityQueue()

    # (heuristic value, current node, path till current node)
    pq.put((heuristic[start], start, [start]))

    visited = set()

    while not pq.empty():
        h, current, path = pq.get()

        if current in visited:
            continue

        print("Visiting:", current)

        visited.add(current)

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor, path + [neighbor]))

    return None


graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")

    neighbors = input(f"Enter neighbors of {node} separated by comma: ")

    if neighbors.strip() == "":
        graph[node] = []
    else:
        graph[node] = [x.strip() for x in neighbors.split(",")]

print("\nEnter heuristic values:")

for node in graph:
    heuristic[node] = int(input(f"Enter heuristic for {node}: "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

path = best_first_search(graph, heuristic, start, goal)

if path:
    print("\nPath found:", " -> ".join(path))
else:
    print("\nNo path found")
    
"""
Enter number of nodes: 4

Enter node name: A
Enter neighbors of A separated by comma: B,C

Enter node name: B
Enter neighbors of B separated by comma: D

Enter node name: C
Enter neighbors of C separated by comma: D

Enter node name: D
Enter neighbors of D separated by comma:

Enter heuristic values:
Enter heuristic for A: 3
Enter heuristic for B: 1
Enter heuristic for C: 2
Enter heuristic for D: 0

Enter start node: A
Enter goal node: D

Visiting: A
Visiting: B
Visiting: D

Path found: A -> B -> D """