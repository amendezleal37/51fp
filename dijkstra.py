# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:33:43 2014

@author: Oscar

Dijkstra's Algorithm:
Found example from https://gist.github.com/econchick/4666413
Reference: https://www.cs.princeton.edu/~rs/AlgsDS07/15ShortestPaths.pdf

Have to learn from this example and adapt to our data representation.
"""

from graph import ListGraph

graph = ListGraph()

def dijkstra(graph, initial):
  visited = {initial: 0}
  path = {}
 
  nodes = set(graph.nodes)
 
  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node
 
    if min_node is None:
      break
 
    nodes.remove(min_node)
    current_weight = visited[min_node]
 
    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node
 
return visited, path