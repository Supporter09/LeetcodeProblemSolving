def distributeCoins(edges, cost):
    n = len(cost)
    graph = {i: [] for i in range(n)}

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    coins = [0] * n
    visited = [False] * n

    stack = [0]  # Start with the root node
    visited[0] = True

    while stack:
        node = stack[-1]

        # Check if all children are visited
        if all(visited[child] for child in graph[node]):
            stack.pop()

            # Leaf node, place 1 coin
            if not graph[node]:
                coins[node] = 1
                continue

            subtree_costs = [coins[child] for child in graph[node]]
            subtree_costs.sort(reverse=True)

            # Place coins based on the conditions
            if len(subtree_costs) < 3:
                coins[node] = 1
            else:
                coins[node] = subtree_costs[0] * subtree_costs[1] * subtree_costs[2]

        else:
            # Visit the next unvisited child
            for child in graph[node]:
                if not visited[child]:
                    stack.append(child)
                    visited[child] = True

    return coins

# Example usage:
edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
cost = [1,2,3,4,5,6]
print(distributeCoins(edges, cost))
