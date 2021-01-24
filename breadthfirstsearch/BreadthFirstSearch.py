class BFS():
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, s):
        '''
        Runs breath-first search on self.graph starting on node s. 
        For each node v in self.graph, we record its distance
        (aka. length of shortest path) from s to v.
        Proof of Correctness: Base case the trivial, as when dist = 0
        only node s has dist[s] = 0, rest is None.
        To record the nodes with n + 1 for dist, we find the 
        neighbours of the nodes with n for dist with dist as None.
         
        @input s: the starting node in self.graph
        '''
        dist = dict.fromkeys(self.graph, None)
        dist[s] = 0
        q = [s]
        while q:
            u = q.pop(0)
            for v in self.graph[u]: #for all neighbours of u
                if not dist[v]:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist


        

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : []
}

neo = BFS(graph)
print(neo.bfs('A'))

