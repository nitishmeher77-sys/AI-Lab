
# EXP -4 A* ALGORTHIM


import heapq

# Graph represented as an adjacency list
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 5)],
    'D': [('G', 3)],
    'G': []
}

# Heuristic values
heuristic = {
    'S': 6,
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'G': 0
}

def a_star(graph, start, goal, heuristic):
    # Priority queue: (f_cost, node)
    open_list = [(heuristic[start], start)]

    # Cost from start to each node
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    # Store parent of each node
    parent = {start: None}

    while open_list:
        f, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[goal]

        # Explore neighbors
        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))

    return None, float('inf')

# Run A* algorithm
path, cost = a_star(graph, 'S', 'G', heuristic)

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)
'''-------OUTPUT--------

Shortest Path: S -> A -> C -> G
Total Cost: 8

'''