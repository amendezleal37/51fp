# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 19:19:38 2014

@author: alex
"""

import math as m

def member(x,xs):
    if xs.count(x) == 0:
        return False
    else:
        return True
"""
# A graph implementation using a nested list of objects. As of
# yet, this module is incomplete. ListGraph seems like a better implementation
class Graph:
    
    #T his implementation of a graph uses a nested list of objects. This makes
    # the data structure more difficult to access from outside the module, but
    # can be inconvenient to modify later
    
    def __init__(self,ID,pos,edges):
        self.node = [ID,pos,edges]
        
    def edges(self):
        return self.node[2]
        
    def insert(self,ID,pos,edges):
        for i in range(len(self.node[2])):
            if self.node[2][i] == ID:
                self.node[2][i] = Graph(ID,pos,edges)
                
    def r(self):
        return self.node

x = Graph(0,(0,0),[1,2])
"""

# Could probably streamline the unpacking process
class ListGraph:
    """
    This implementation of a graph makes use of a list of 'nodes' and
    has the advantage of easy access, lookup, and modification.
    """
    def __init__(self):
        self.ID = 0
        self.list = []
    
    def new_node(self,pos,edges,name):
        # Creates a new node with the next ID
        list.append(self.list,(self.ID,pos,edges,name))
        self.ID += 1
    
    # Creates a new node with desired position, but also is pointed
    # to by the nodes specified in the third argument
    # def new_with_p(self,pos,edges,npointed):
            
    
    def edges(self,ID):
        x,y,z,n = self.list[ID]
        return z
    
    def distance(self,node1,node2):
        # Distance from node1 to node2 as longs as they're connected.
        # If not connected, throws an exception. This requires various
        # stages of unpacking
        i1,p1,e1,n1 = self.list[node1]
        i2,p2,e2,n2 = self.list[node2]
        x1,y1 = p1
        x2,y2 = p2
        # Check to see if node1 points to node2
        if e1.count(node2) >= 1:
            return m.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        else:
            # This will eventually be changed to raise an exception
            print "node1 doesn't point to node2"

    # both edge methods (Add and update) ensure a sorted list of edges
    # Add a single edge to a node
    def add_edge(self,ID,edge):
        node = self.list[ID]
        i,p,e,n = node
        # Only adds if not already in list
        if not(member(edge,e)):
            e.append(edge)
            e.sort()
            self.list[ID] = i,p,e
    
    # Add a single edge to multiple nodes (probably for updating purposes)
    def add_edges(self,IDs,edge):
        for i in IDs:
            self.add_edge(i,edge)

    def update_edges(self,ID,new_es):
        node = self.list[ID]
        i,p,e = node
        self.list[ID] = i,p,new_es

    # For test purposes. Will remove to maintain abstraction
    # barrier
    def r(self,ID):
        return self.list[ID]