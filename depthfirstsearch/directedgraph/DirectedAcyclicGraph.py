class DFS():
    '''
    Linearazation of a DAG with part of depth first search.
    To check the graph is a DAG we check that there is no back edge in the input graph.
    Then linearaze it by sorting self.post in the decreasing order.
    '''
    def __init__(self, graph):
        self.graph = graph
        self.visited = dict.fromkeys(graph, False)

        # id of connected component
        self.pre = dict.fromkeys(graph, -1)
        self.post = dict.fromkeys(graph, -1)
        self.clock = 0

        self.isdag = True

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
        
    def is_dag(self):
        '''
        Go find a back edge for all the edges...
        '''
        for u in self.graph:
            for v in self.graph[u]:
                if self.pre[v] < self.pre[u] and self.post[u] < self.post[v]:
                    return False
        return True


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
print(neo.is_dag())