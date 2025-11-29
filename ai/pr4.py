def dfs_trav(graph, node, visited=None):
    if visited is None:
        visited = set()
        if node not in visited:
            print(node, end="")
            visited.add(node)
            for neigh in graph[node]:
                dfs_trav(graph, neigh, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': [],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': ['L'],
    'K': [],
    'L': []
}

print("Depth First Search starting from A:")

def dfs_trav(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            stack.extend(reversed(graph[node]))

dfs_trav(graph, 'A')
