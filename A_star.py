import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        current_f, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, g_cost[goal]

        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            new_g = g_cost[current_node] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current_node

    return None, float("inf")


graph = {
    'S': [('A', 1), ('B', 2)],
    'A': [('X', 4), ('Y', 7)],
    'B': [('C', 7), ('D', 1)],
    'C': [('E', 5)],
    'D': [('E', 12)],
    'X': [('E', 2)],
    'Y': [('E', 3)],
    'E': []
}

heuristic = {
    'S': 15,
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 15,
    'X': 5,
    'Y': 8,
    'E': 0
}

start = 'S'
goal = 'E'

path, path_cost = a_star(graph, heuristic, start, goal)

print("Path Cost:", path_cost)
print("Path:", path)
