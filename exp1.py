# exp-1:BFS
from collections import deque

def bfs(graph, start):
    visited = set()              # To keep track of visited vertices
    queue = deque([start])       # Initialize queue with the starting vertex
    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:                 # Continue until the queue is empty
        vertex = queue.popleft() # Remove the first element from the queue
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Create the graph
graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").split()
    graph[vertex] = neighbors

start = input("Enter the starting vertex: ")

print("\nGraph:", graph)
bfs(graph, start)

''' -----OUTPUT-------
Enter the number of vertices: 8
Enter vertex 1: a
Enter neighbors of a (space-separated): b c d
Enter vertex 2: b
Enter neighbors of b (space-separated): e f
Enter vertex 3: c
Enter neighbors of c (space-separated): 
Enter vertex 4: d
Enter neighbors of d (space-separated): g h
Enter vertex 5: e
Enter neighbors of e (space-separated): 
Enter vertex 6: f
Enter neighbors of f (space-separated): 
Enter vertex 7: g
Enter neighbors of g (space-separated): 
Enter vertex 8: h
Enter neighbors of h (space-separated): 
Enter the starting vertex: a

Graph: {'a': ['b', 'c', 'd'], 'b': ['e', 'f'], 'c': [], 'd': ['g', 'h'], 'e': [], 'f': [], 'g': [], 'h': []}
BFS Traversal: a b c d e f g h 







'''