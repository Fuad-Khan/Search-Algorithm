import heapq  # For priority queue


def a_star(graph, start, goal, h):
    pq = []
    heapq.heappush(pq, (0 + h[start], 0, start))  # (f(n), g(n), node)
    visited = set()
    parent = {start: None}  # To track the path

    while pq:
        f, g, node = heapq.heappop(pq)  # Get the node with the lowest f(n) value

        if node == goal:
            print("\nGoal reached!")
            return reconstruct_path(parent, goal)

        if node not in visited:
            visited.add(node)

            # Expand the neighbors
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    new_g = g + cost
                    new_f = new_g + h[neighbor]
                    heapq.heappush(pq, (new_f, new_g, neighbor))
                    parent[neighbor] = node

    return None  # If no path found


def reconstruct_path(parent, node):
    path = []
    while node:
        path.append(node)
        node = parent[node]
    return path[::-1]  # Reverse the path


# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values (h(n)): Estimated cost to reach goal 'G'
h = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 7,
    'E': 2,
    'F': 2,
    'G': 0  # Goal node has heuristic value of 0
}

# Perform A* Search from node 'A' to goal 'G'
path = a_star(graph, 'A', 'G', h)
if path:
    print("Path:", path)
else:
    print("No path found")
