def validPath(n, edges, source, destination):
    from collections import defaultdict, deque

    # Define a graph
    graph = defaultdict(list)

    # Add edges to the graph
    for u, v in edges:
        # Bidirectional edges
        graph[u].append(v)
        graph[v].append(u)

    # Define a visited set
    visited = set()

    # Define a BFS function
    def bfs(node):
        q = deque([node])

        while q:
            curr = q.popleft()

            # Reach the destination
            if curr == destination:
                return True

            # Mark the node as visited
            visited.add(curr)

            # Add neighbours
            for n in graph[curr]:
                if n not in visited:
                    q.append(n)

        return False

    return bfs(source)


print(validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
