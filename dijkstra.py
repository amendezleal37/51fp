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
import yardgraph

map = yardgraph.graph

# start and end are the id's of the two nodes
start = 0
end = 1

#def dijkstra(start, end):
  
# first make unvisited include all nodes
unvisited = range(map.ID)

# initialize list of known shortest distances from start
dist = [None] * map.ID
    
# start node has 0 distance to itself
# dist[end] = 0