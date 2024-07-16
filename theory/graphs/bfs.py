#!/usr/bin/env python3

# Reference:
# Introduction to Algorithms, Fourth edition
# Linda Xiao and Tom Cormen
# https://github.com/Ky-Ling/CLRS-Python-Implementation

import sys
sys.path.append('queue')  # Add the 'utils' directory to the path

from fifo_queue import Queue
from adjacency_list_graph import AdjacencyListGraph
from print_graph import print_path

WHITE = 0  # undiscovered
GRAY = 1  # discovered
BLACK = 2  # visited


def bfs(G, source):
    """
    Perform breadth-first search on a graph, filling in distances and predecessors

    Arguments:
    G -- the graph, implemented with adjacency list
    source -- index of the source vertex
    """
    # Initialize all vertices to white with distance of infinity and no predecessor,
    # except source is gray
    card_V = G.get_card_V()  # vertices are numbered, so that color[i] gives the color of the vertex i
    color = [WHITE] * card_V  # all unvisited
    dist = [float('inf')] * card_V  # card_V  # dist[i] holds the distance from the source vertex to vertex i 
    pi = [None] * card_V  # predecessor variable
    color[source] = GRAY
    dist[source] = 0

    q: Queue = Queue(card_V)
    q.enqueue(source)
    while not q.is_empty():
        u = q.dequeue()
        for edge in G.get_adj_list(u):  # Search the neighbors of u
            v = edge.get_v()
            if color[v] == WHITE:
                color[v] = GRAY
                dist[v] += 1
                pi[v] = u
                q.enqueue(v)
        color[u] = BLACK
    return dist, pi


# Testing
if __name__ == "__main__":
    import sys
    sys.path.append('utils')  # Add the 'utils' directory to the path

    import numpy as np
    from generate_random_graph import generate_random_graph

    # Directed.
    card_V = 10
    graph1 = generate_random_graph(card_V, 0.25, True)
    print(graph1)
    s = 5
    dist, predecessor = bfs(graph1, s)
    for i in range(card_V):
        print(str(i) + ": dist = " + str(dist[i]) + ", path = "
              + str(print_path(predecessor, s, i, lambda i: i)))
    print()

    # Undirected, textbook example.
    vertices = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    edges = [('r', 's'), ('r', 't'), ('r', 'w'), ('s', 'u'), ('s', 'v'),
             ('t', 'u'), ('u', 'y'), ('v', 'w'), ('v', 'y'), ('w', 'x'),
             ('w', 'z'), ('x', 'y'), ('x', 'z')]
    card_V = len(vertices)
    graph2 = AdjacencyListGraph(card_V, False)
    for edge in edges:
        graph2.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]))
    print(graph2.strmap(lambda i: vertices[i]))
    s = vertices.index('s')
    dist, predecessor = bfs(graph2, s)  # BFS from s
    for i in range(card_V):
        print(vertices[i] + ": dist = " + str(dist[i]) + ", path = "
              + str(print_path(predecessor, s, i, lambda i: vertices[i])))
