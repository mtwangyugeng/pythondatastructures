class DFS():
    '''
    This DFS show pre and post orderings.
    For any node u and v, the two intervals [pre[u], post[u]]
    [pre[v], post[v]] are either disjoint or on is contained
    within the other
    undirected graph only
    '''
    def __init__(self, graph):
        self.graph = graph
        self.visited = dict.fromkeys(graph, False)

        # id of connected component
        self.pre = dict.fromkeys(graph, -1)
        self.post = dict.fromkeys(graph, -1)
        self.clock = 0

    def _explore(self, v):
        '''
        What part of graph are reachable from
        a give vertex?
        '''
        self.visited[v] = True
        # previsit 
        self.pre[v] = self.clock
        self.clock += 1
        for u in self.graph[v]:
            if not self.visited[u]:
                self._explore(u)
        #postvisit
        self.post[v] = self.clock
        self.clock += 1
    def dfs(self):
        # self.visited = dict.fromkeys(graph, False)
        for u in self.graph:
            if not self.visited[u]:
                self._explore(u)

graph = {
    'A' : ['B','C'],
    'B' : ['A'],
    'C' : ['A'],
    'D' : [],
    'E' : ['F'],
    'F' : ['E'],
    'G' : []
}

neo = DFS(graph)
neo.dfs()
print(neo.pre)
print(neo.post)