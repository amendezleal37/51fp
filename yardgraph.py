# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 15:40:55 2014

@author: alex
"""
from graph import ListGraph as lg

# Initialize a new ListGraph object
graph = lg()

# Add Widener at (0,3) and intersection
graph.new_node((3,0),[1],"widener")
graph.new_node((3,2),[0,2,3,5],"intersection1")

# Add Sever
graph.new_node((6,5),[1,3],"sever")

# Add Mem Church
graph.new_node((3,10),[1,2,4],"memorialchurch")

# Add University Hall
graph.new_node((0,7),[3,5],"universityhall")

# Add Weld
graph.new_node((0,3),[1,4],"weld")

# Note: This is a very simplistic graph, A picture of which
# will be uploaded into the google doc if you need to see it