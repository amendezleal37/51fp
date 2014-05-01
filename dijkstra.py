# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:33:43 2014

@author: Oscar

Dijkstra's Algorithm:
Reference: https://www.cs.princeton.edu/~rs/AlgsDS07/15ShortestPaths.pdf

"""

from graph import ListGraph

graph = ListGraph()

def dijkstra(graph, source, destination):
    unvisited = []
    