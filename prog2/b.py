import heapq

def a_star_search(graph, start, goal, heuristic, cost):
    # Priority queue for exploring nodes
    priority_queue = []
    heapq.heappush(priority_queue, (0 + heuristic[start], start)) #the priority is determined by the estimated total cost (current cost + heuristic)
    visited = set()
    g_cost = {start: 0} #g_cost stores the cost of the cheapest known path from the start node to each node.
    parent = {start: None}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor in graph[current_node]:
            new_cost = g_cost[current_node] + cost[(current_node, neighbor)]
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(priority_queue, (f_cost, neighbor))
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

# Example costs between nodes (assumed for demonstration)
cost = {
    ('A', 'B'): 1,
    ('A', 'C'): 1,
    ('B', 'D'): 1,
    ('B', 'E'): 3,
    ('C', 'F'): 5,
    ('C', 'G'): 2
}

start = 'A'
goal = 'D'

path = a_star_search(graph, start, goal, heuristic, cost)
print("A* Search Path:", path)

# def h(n):
#     H = {'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0, 'S': 5}
#     return H[n]

# def a_star_algorithm(graph, start, goal):

#     open_list = [start]
#     closed_list = set()

#     g = {start:0}

#     parents = {start:start}

#     while open_list:

#         open_list.sort(key=lambda v: g[v] + h(v), reverse=True)
#         n = open_list.pop()

#         # If node is goal then construct the path and return
#         if n == goal:
#             reconst_path = []

#             while parents[n] != n:
#                 reconst_path.append(n)
#                 n = parents[n]

#             reconst_path.append(start)
#             reconst_path.reverse()

#             print(f'Path found: {reconst_path}')
#             return reconst_path

#         for (m, weight) in graph[n]:
#         # if m is first visited, add it to open_list and note its parent
#             if m not in open_list and m not in closed_list:
#                 open_list.append(m)
#                 parents[m] = n
#                 g[m] = g[n] + weight

#             # otherwise, check if it's quicker to first visit n, then m
#             # and if it is, update parent and g data
#             # and if the node was in the closed_list, move it to open_list
#             else:
#                 if g[m] > g[n] + weight:
#                     g[m] = g[n] + weight
#                     parents[m] = n

#                     if m in closed_list:
#                         closed_list.remove(m)
#                         open_list.append(m)

#         # Node's neighbours are visited. Now put node to closed list.
#         closed_list.add(n)

#     print('Path does not exist!')
#     return None


# graph = {
#     'S': [('A', 1), ('G', 10)],
#     'A': [('B', 2), ('C', 1)],
#     'B': [('D', 5)],
#     'C': [('D', 3),('G', 4)],
#     'D': [('G', 2)]
# }

# a_star_algorithm(graph, 'S', 'G')
