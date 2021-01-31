class BFS():
    def __init__(self, graph):
        self.graph = graph
    def bellman_ford(self, s):
        """Find the shortest path of self.graph.
        Usable with negative edges.
        the update section of the loop has two properties:
        1. It gives the correct distance for the end node of e (denoted v),
            if u is the second-last node in the shortest path to v;
            and u is correctly set.
        2. It will never make the dist[v] too small.
        
        Also, notice that the shortest path consists at most |V| - 1
        edges. Because o/w there will be a cycle, but a path cannot have a cycle.
        
        Thus by updating dists of all nodes for |V| - 1 times, the shortest path
        for all nodes from s will be updated according to the correct sequence of
        updating
        
        Args:
            s ([string]): the starting node of the shortest path.

        Returns:
            [dict, dict]: the distance and the path of the shortest path
            of each node.
        """ 
        prevs = dict.fromkeys(self.graph, None)
        dists = dict.fromkeys(self.graph, float('inf'))

        dists[s] = 0
        
        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                for e in self.graph[u]: # for all edges in self.graph
                    # Update start
                    if dists[e[0]] > dists[u] + e[1]:
                        dists[e[0]] = dists[u] + e[1]
                        prevs[e[0]] = u
                    # Update end
        
        return dists, prevs
graph = {
    'A' : [('B',2),('C',3),('D',1)],
    'B' : [('D',4), ('E',-3)],
    'C' : [('F',1)],
    'D' : [],
    'E' : [('F', -7)],
    'F' : [],
    'G' : []
}

neo = BFS(graph)
print(neo.bellman_ford('A'))
