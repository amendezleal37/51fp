# Zahra Mahmood
# 
# Get user input to find path between two points
from yardgraphfull import graph
from BellmanFord import shortest_path
from dijkstra import dijkstra_path


print "Please input your starting point"
start = raw_input()
print "Please provide your destination"
end = raw_input()
print "Please choose your algorithm: \ninput 'd' for Dijkstra's algorithm or 'b' for Bellman-Ford algorithm"
algorithm = raw_input()

source = graph.name_to_id(start.lower())
sink = graph.name_to_id(end.lower())


if algorithm == "d" or "D":
	path_id = dijkstra_path(source, sink)
	print "\n"
	for k in range(len(path_id)):
		print graph.id_to_name(path_id[k])
	print "\n"
elif algorithm == "b" or "B":
	path_id = shortest_path(source, sink)
	print "\n"
	for k in range(len(path_id)):
		print graph.id_to_name(path_id[k])
	print "\n"