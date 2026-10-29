# EXP-2 DFS
def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Create the graph
graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ").strip()
    neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").strip().split()
    graph[vertex] = neighbors

# Starting vertex
start = input("Enter the starting vertex: ").strip()

print("\nGraph:", graph)

visited = set()

print("DFS Traversal:", end=" ")
dfs(graph, start, visited)
'''-----OUTPUT--------
Enter the number of vertices: 4
Enter vertex 1: A
Enter neighbors of A (space-separated): B C
Enter vertex 2: B
Enter neighbors of B (space-separated): D
Enter vertex 3: C
Enter neighbors of C (space-separated):
Enter vertex 4: D
Enter neighbors of D (space-separated):
Enter the starting vertex: A
Graph: {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
DFS Traversal: A B D C


'''