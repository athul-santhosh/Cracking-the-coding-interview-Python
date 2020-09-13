# problem 4.1
# Route betweeen two nodes

visited = set()
path_found = False
def dfs(graph,cur_node,target):

	global path_found
	visited.add(cur_node)
	# if node we are at becomes equal to target , change path found to True
	if cur_node == target:
		path_found = True


	for neighbour in graph[cur_node]:
		
		if neighbour not in visited:
			visited.add(neighbour)

			dfs(graph,neighbour,target)

	return path_found


graph = {
	"A" : ["B","C"],
	"B" : [],
	"C" : ["H"],
	"I": ["H"],
	"H":[]
}
print(dfs(graph,"A","C"))

"""
Graph 
        A
       / \
      B   C   I
           \ /
            H
 


"""