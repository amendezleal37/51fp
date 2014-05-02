# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:27:22 2014

@author: alex
"""
from graph import ListGraph

# graph will be an edge vertex representation of a map of Harvard Yard
graph = ListGraph()

# Lehman Dudley House
graph.new_node((6,16),[1,2,12,13],"dudley")

# Strauss
graph.new_node((5,22),[0,2,3],"strauss")

# Matthews
graph.new_node((9,21),[0,1,3,12,29,30],"matthews")

# Mass Hall
graph.new_node((8,26),[1,2,4,29,30],"masshall")

# Harvard Hall
graph.new_node((8,32),[3,5,6,7,28,29],"harvardhall")

# Lionel
graph.new_node((6.5,36),[4,6,7,8],"lionel")

# Holden
graph.new_node((8.5,38),[4,5,7,8,9,10,28],"holden chapel")

# Hollis
graph.new_node((12,35),[4,5,6,8,9,10],"hollis")

# Mower
graph.new_node((7.5,41),[5,6,7,9,10],"mower")

# Phillip Brooks House
graph.new_node((11,44),[6,8,10],"phillip brooks house")

# Stoughton
graph.new_node((13,40),[6,7,8,9,11,28],"stoughton")

# Holworthy
graph.new_node((17,42),[9,10,18,19,28],"holworthy")

# Grays
graph.new_node((14,16,5),[1,2,13,14,15,16,30],"grays")

# Wadsworth
graph.new_node((11,13),[0,2,12,14,15],"wadsworth")

# Boylston
graph.new_node((17,13),[12,13,15,16,21],"boylston")

# Wigglesworth
graph.new_node((24,9),[13,14,21,22,23],"wigglesworth")

# Weld
graph.new_node((19,20),[12,14,17,21,30,41,42],"weld")

# University Hall
graph.new_node((18,26),[16,18,20,21,28,29,30,39,41,42],"university hall")

# Thayer
graph.new_node((22,37),[11,17,19,20,28,29,42],"thayer")

# Canaday
graph.new_node((30,40),[11,18,20,27],"canaday")

# Mem Church
graph.new_node((28,33),[17,18,19,28,40,42],"memorial church")

# Widener
graph.new_node((26,15),[14,15,16,22,25,39],"widener library")

# Houghton Library
graph.new_node((30,12),[15,21,23,24,25],"houghton library")

# Lamont
graph.new_node((35,7),[15,22,24],"lamont library")

# Loeb House Library
graph.new_node((36,16),[21,22,23,25],"loeb house library")

# Emerson
graph.new_node((36,19),[21,24,26,39],"emerson")

# Sever
graph.new_node((34,26),[20,25,27,39,40],"sever")

# Robinson
graph.new_node((38,32),[19,20,26],"robinson")

# Intersections
graph.new_node((17,38),[4,6,7,10,11,17,18],"intersection28")
graph.new_node((14,29),[2,3,4,7,17,18],"intersection29")
graph.new_node((13,20),[0,2,3,12,16,17],"intersection30")
graph.new_node((26,21),[16,21,25,26,40,41],"intersection31")
graph.new_node((27,26),[20,26,39,41],"intersection32")
graph.new_node((24,24),[16,17,39,40,42],"intersection33")
graph.new_node((23,27),[17,18,20,41],"intersection34")