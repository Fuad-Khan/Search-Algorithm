import heapq  # For priority queue


def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic[start], start))  # Push the start node with its heuristic value

    while pq:
        current_heuristic, node = heapq.heappop(pq)  # Get the node with the lowest heuristic value
        print(node, end=" ")

        if node == goal:  # If the goal is reached, stop
            print("\nGoal reached!")
            return

        visited.add(node)

        # Expand the neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))  # Add neighbors based on heuristic value


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Heuristic values (straight-line distance to the goal node 'G')
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 7,
    'E': 2,
    'F': 4,
    'G': 0  # Goal node has a heuristic value of 0
}

# Perform Greedy Best-First Search from node 'A' to goal 'G'
greedy_best_first_search(graph, 'A', 'G', heuristic)
