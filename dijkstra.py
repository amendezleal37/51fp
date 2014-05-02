# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:33:43 2014

@author: Oscar Xia

Dijkstra's Algorithm:

References: https://www.cs.princeton.edu/~rs/AlgsDS07/15ShortestPaths.pdf
http://en.wikipedia.org/wiki/Dijkstra's_algorithm

"""

# from graph import ListGraph
# map = ListGraph()

# map we are working with:
import yardgraph
yardmap = yardgraph.graph

# start and end are the id's of the two nodes
# can be changed by the user
start = 4
end = 1

#def dijkstra(start, end):
  
# initializes unvisited to include all nodes
unvisited = range(yardmap.ID)

# initializes list of known shortest distances from start
dist = [float('inf')] * yardmap.ID

# initializes the list of previous nodes for each node to keep track of paths
prev = ['null'] * yardmap.ID
    
# start node has 0 distance to itself
dist[start] = 0

# start node removed from unvisited
unvisited.remove(start)

current = start

while (end in unvisited):
    for neighbor in yardmap.list[current][2]:
        if (neighbor in unvisited):
            new_dist = dist[current] + yardmap.distance(current, neighbor)
            if (new_dist < dist[neighbor]):
                dist[neighbor] = new_dist
                prev[neighbor] = current
    
    if (current in unvisited):
        unvisited.remove(current)
    
    if len(unvisited) != 0:
        current = unvisited[0]
        for i in unvisited:
            if dist[i] < current:
                current = i

"""
def update_neighbor(current, neighbor):
    if (neighbor in unvisited):
        new_dist = dist[current] + map.distance(current, neighbor)
        if (new_dist < dist[neighbor]) or (dist[neighbor]==-1):
            dist[neighbor] = new_dist
            prev[neighbor] = current

while (end in unvisited):
    for neighbor in map.list[current][2]:
        update_neighbors ...
    if (current in unvisited):
        unvisited.remove(current)
    for i in map.list[current][2]:
        if i in unvisited:
            current = i
            break
"""