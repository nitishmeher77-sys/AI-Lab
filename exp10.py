# EXP-10 TRAVELLING SALESMAN PROBLEM


from itertools import permutations

# function to slove tsp
def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)

    min_cost = float('inf')
    best_path = None

    # generate all possible tours
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start

        for city in perm:
            current_cost += graph[k][city]
            current_path.append(city)
            k = city
        current_cost += graph[k][start]
        current_path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
    return best_path, min_cost

# main program
n = int(input("Enter the number of cities: "))

print("Enter the cost matrix:")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting city: "))

path, cost = travelling_salesman(graph, start)

print("\nOptimal path:", " -> ".join(map(str, path)))
print("Minimum cost:", cost)
'''-------OUTPUT----------
Enter the number of cities: 4
Enter the cost matrix:
0 10 15 20
10 0 35 25 
15  35 0 30 
20 25 30 0 
Enter the starting city: 0

Optimal path: 0 -> 1 -> 3 -> 2 -> 0
Minimum cost: 80
'''