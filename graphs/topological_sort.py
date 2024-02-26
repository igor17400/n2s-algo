from collections import defaultdict, deque


def topological_sort_bfs(graph):
    # Step 1: Initialize
    inDegree = [0] * len(graph)
    print(inDegree)
    queue = deque()

    # Calculate incoming edge count for each vertex
    for vertices in graph.values():
        for v in vertices:
            inDegree[v] += 1

    # Enqueue vertices with no incoming edges
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            queue.append(i)

    # Step 2: BFS Loop
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)

        for v in graph[u]:
            inDegree[v] -= 1
            if inDegree[v] == 0:
                queue.append(v)

    # Step 3: Result
    return result


# Example usage
graph = {0: [3, 4], 1: [2], 2: [3], 3: [6], 4: [3, 5], 5: [6], 6: []}
sorted_order = topological_sort_bfs(graph)
print("Topological Order:", sorted_order)
