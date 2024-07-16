def dfs(graph, node, stack, visited):
    if node in stack:
        # Found a cycle
        cycle_start = stack.index(node)
        cycle = stack[cycle_start:]
        print("Directed Cycle:", cycle)
        return True

    if node in visited:
        # Already visited this node in a different path, no need to explore
        return False

    # Mark the node as visited and push it onto the stack
    visited.add(node)
    stack.append(node)

    # Explore neighbors
    for neighbor in graph.get(node, []):
        if dfs(graph, neighbor, stack, visited):
            return True

    # Backtrack: remove the current node from the stack
    stack.pop()
    return False


def find_directed_cycle(graph):
    """
    Goal: find a directed path in a graph
    """
    visited = set()  # Set to keep track of visited vertices
    stack = []       # Stack to keep track of the current path

    # Perform DFS for each unvisited vertex
    for vertex in graph:
        if vertex not in visited:
            stack = []
            if dfs(graph, vertex, stack, visited):
                return  # Stop early if a cycle is found


# Example usage:
graph = {
    1: [2],
    2: [3],
    3: [4, 1],
    4: []
}

graph = {
    0: [1, 4, 3],
    1: [2, 3],
    2: [],
    3: [2, 5],
    4: [0],
    5: [2, 4]
}

find_directed_cycle(graph)
