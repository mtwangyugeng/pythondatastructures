class DFS():
    '''
    Only traverses the graph in the order given in input.
    For any node u and v, the two intervals [pre[u], post[u]]
    [pre[v], post[v]] are either disjoint or on is contained
    within the other
    what pre/post looks like based on types of edges u-v
    Tree/forard = u v v u
    back = v u u v
    cross = v v u u
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
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : []
}

neo = DFS(graph)
neo.dfs()
print(neo.pre)
print(neo.post)