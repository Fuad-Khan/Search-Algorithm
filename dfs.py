def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # To track visited nodes
    visited.add(start)  # Mark the current node as visited
    print(start, end=" ")  # Process the node (print it here)

    # Visit all unvisited neighbors recursively
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform DFS from node 'A'
dfs(graph, 'A')
