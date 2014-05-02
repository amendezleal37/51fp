# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:33:43 2014

@author: Oscar

Dijkstra's Algorithm:

References: https://www.cs.princeton.edu/~rs/AlgsDS07/15ShortestPaths.pdf
http://en.wikipedia.org/wiki/Dijkstra's_algorithm

"""

# from graph import ListGraph
# map = ListGraph()

# map we are working with:
import yardgraph
map = yardgraph.graph

# start and end are the id's of the two nodes
# can be changed by the user
start = 0
end = 1

#def dijkstra(start, end):
  
# initializes unvisited to include all nodes
unvisited = range(map.ID)

# initializes list of known shortest distances from start
dist = [-1] * map.ID

# initializes the list of previous nodes for each node to keep track of paths
prev = [-1] * map.ID
    
# start node has 0 distance to itself
dist[start] = 0

# start node removed from unvisited
unvisited.remove(start)

current = start

while (end in unvisited):
    for neighbor in map.list[current][2]:
        if (neighbor in unvisited):
            new_dist = dist[current] + map.distance(current, neighbor)
            if (dist[neighbor]==-1) or (new_dist < dist[neighbor]):
                dist[neighbor] = new_dist
                prev[neighbor] = current
    unvisited.remove(current)
    current = map.list[current][2][0]
