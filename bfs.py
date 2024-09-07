from collections import deque


def bfs(graph, start):
    visited = set()  # To track visited nodes
    queue = deque([start])  # Use deque for efficient queue operations
    visited.add(start)  # Mark the starting node as visited

    while queue:
        node = queue.popleft()  # Dequeue a node
        print(node, end=" ")  # Process the node (print it here)

        # Visit all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS from node 'A'
bfs(graph, 'A')
