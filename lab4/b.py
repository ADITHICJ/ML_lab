from queue import PriorityQueue

def a_star(graph, heuristic, start, goal):
    pq = PriorityQueue()

    # (f, g, current_node, path)
    pq.put((heuristic[start], 0, start, [start]))

    visited = set()

    while not pq.empty():
        f, g, current, path = pq.get()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, g

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                pq.put((new_f, new_g, neighbor, path + [neighbor]))

    return None, None


# Input Graph
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    graph[node] = []

    m = int(input(f"Enter number of neighbours of {node}: "))

    for j in range(m):
        neighbor = input("Enter neighbour name: ")
        cost = int(input("Enter cost: "))
        graph[node].append((neighbor, cost))

# Heuristic values
heuristic = {}

for node in graph:
    heuristic[node] = int(input(f"Enter heuristic value of {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, total_cost = a_star(graph, heuristic, start, goal)

if path:
    print("\nPath Found:")
    print(" -> ".join(path))
    print("Total Cost =", total_cost)
else:
    print("No path found")
    
"""Enter number of nodes: 6

Enter node name: A
Enter number of neighbours of A: 2
Enter neighbour name: B
Enter cost: 1
Enter neighbour name: C
Enter cost: 4

Enter node name: B
Enter number of neighbours of B: 2
Enter neighbour name: D
Enter cost: 2
Enter neighbour name: E
Enter cost: 5

Enter node name: C
Enter number of neighbours of C: 1
Enter neighbour name: F
Enter cost: 3

Enter node name: D
Enter number of neighbours of D: 0

Enter node name: E
Enter number of neighbours of E: 1
Enter neighbour name: F
Enter cost: 1

Enter node name: F
Enter number of neighbours of F: 0

Enter heuristic value of A: 7
Enter heuristic value of B: 6
Enter heuristic value of C: 2
Enter heuristic value of D: 1
Enter heuristic value of E: 1
Enter heuristic value of F: 0

Enter start node: A
Enter goal node: F

Path Found:
A -> B -> E -> F
Total Cost = 7"""