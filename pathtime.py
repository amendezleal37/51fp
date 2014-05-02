# -*- coding: utf-8 -*-
"""
Created on Fri May  2 15:33:02 2014

@author: alex
This function takes in a graph and a list of node ids that represents a
certain path, and returns the time (in minutes) and the distance (in miles)
according to our own representation of the yard.

The only reason that it is specialized to our yard graph is because of the
map scale that we happened to use. 
"""

def walktime(graph,idlist):
    path=idlist
    dist_f=0 # initial distance (feet/25)
    
    # Calculate the entire distance travelled on the path
    for k in range(len(path)-1):
        dist_f+=graph.distance(k,k+1)
    
    dist_f*=25
    dist_m=dist_f/5280. # in miles
    time=(dist_m/3.1)*60 # in minutes
    return round(time,2),round(dist_m,2)