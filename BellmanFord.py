# Created on Thur Apr 24 2014
# 
# Author: Zahra Mahmood

from graph import ListGraph
import yardgraphfull

map = yardgraphfull.graph

# template for node is (ID, pos, [edges])
nodes_list = map.list

vertices = [x[0] for x in nodes_list]
position = [x[1] for x in nodes_list]
edges = [x[2] for x in nodes_list]

edge_list = []
distance = []
for u in vertices: 
	for v in edges[u]:
		edge_list.append((u,v))

def BellmanFord(vertices, edges, vertex_source):
	weight = []
	predecessor = []
	for v in vertices:
		if v == vertex_source:
			weight.append(0)
			predecessor.append('null')
		else: 
			weight.append(float('inf'))
			predecessor.append('null')

	for i in xrange(len(vertices)):
		for edge, (u,v) in enumerate(edges):
			distance = map.distance(u,v)
			if weight[u] + distance < weight[v]:
				weight[v] = weight[u] + distance
				predecessor[v] = u

	for edge, (u,v) in enumerate(edges):
		distance = map.distance(u,v)
		if weight[u] + distance < weight[v]:
			return "There is a negative-weight cycle"


	return predecessor

def shortest_path(source, sink):
	prev_list = BellmanFord(vertices, edge_list, source)
	path = []
	while sink != source: 
		path.append(sink)
		sink = prev_list[sink]
	path.append(source)
	path.reverse()
	print path

shortest_path(0, 4)


