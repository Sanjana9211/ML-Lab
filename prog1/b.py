#  Best First Search (BFS) Algorithm
#It gives the fastest solution which need not be optimal


import heapq
#Min-Heap Property: By default, heapq maintains a min-heap, meaning the smallest element is always at the root of the heap. 
#This ensures that the smallest element is the one that gets popped first.

def best_first_search(graph, start, goal, heuristic):
    # Priority queue for exploring nodes based on heuristic
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()
    parent = {start: None}

    while priority_queue:
        current_heuristic, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                parent[neighbor] = current_node

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Example heuristic values (assumed for demonstration)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 0,
    'E': 2,
    'F': 3,
    'G': 1
}

start = 'A'
goal = 'D'

path = best_first_search(graph, start, goal, heuristic)
print("Best First Search Path:", path)


# def best_first_search(graph,start,goal,heuristic, path=[]):
#     open_list = [(0,start)]
#     closed_list = set()
#     closed_list.add(start)

#     while open_list:
#         open_list.sort(key = lambda x: heuristic[x[1]],reverse=True)
#         cost, node = open_list.pop()
#         path.append(node)

#         if node==goal:
#             return cost, path

#         closed_list.add(node)
#         for neighbour, neighbour_cost in graph[node]:
#             if neighbour not in closed_list:
#                 closed_list.add(node)
#                 open_list.append((cost+neighbour_cost, neighbour))

#     return None


# graph = {
#     'A': [('B', 11), ('C', 14), ('D',7)],
#     'B': [('A', 11), ('E', 15)],
#     'C': [('A', 14), ('E', 8), ('D',18)],
#     'D': [('A', 7), ('C',18),('G',2)],
#     'E': [('B', 15), ('C', 8)],
#     'G':[]
# }

# start = 'A'
# goal = 'G'

# heuristic = {
#     'A': 40,
#     'B': 32,
#     'C': 25,
#     'D': 35,
#     'E': 19,
#     'F': 17,
#     'G': 0,
#     'H': 10
# }

# result = best_first_search(graph, start, goal, heuristic)

# if result:
#     print(f"Minimum cost path from {start} to {goal} is {result[1]}")
#     print(f"Cost: {result[0]}")
# else:
#     print(f"No path from {start} to {goal}")
