class DFS():
    def __init__(self, graph):
        self.graph = graph
        self.visited = dict.fromkeys(graph, False)

        # id of connected component
        self.pre = dict.fromkeys(graph, -1)
        self.post = dict.fromkeys(graph, -1)
        self.clock = 0

        self.isdag = True

        self.postmaxtomin = []

        # strongly connected component
        self.cc = dict.fromkeys(graph, None)
        self.ccc = -1

    def _explore(self, v):
        '''
        What part of graph are reachable from
        a give vertex?
        '''
        self.visited[v] = True
        # previsit 
        self.cc[v] = self.ccc
        self.pre[v] = self.clock
        self.clock += 1
        for u in self.graph[v]:
            if not self.visited[u]:
                self._explore(u)
        #postvisit
        self.post[v] = self.clock
        self.postmaxtomin = [v] + self.postmaxtomin
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

    def reversed(self, graph):
        '''return the revered graph'''
        neo = {k: [] for k in self.graph}
        for u in graph:
            for v in graph[u]:
                neo[v].append(u)
        return neo

    def scc(self):
        '''
        get the strongly connected component in linear time
        '''
        rg = self.reversed(self.graph)
        neo = DFS(rg)
        neo.dfs()
        self.cc = dict.fromkeys(neo.postmaxtomin, None)
        for u in neo.postmaxtomin:
            if not self.visited[u]:
                self.ccc += 1
                self._explore(u)
        print(self.cc)



    def dfs(self):
        # self.visited = dict.fromkeys(graph, False)
        for u in self.graph:
            if not self.visited[u]:
                self._explore(u)

graph = {
    'A' : ['B'],
    'B' : ['C', 'D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['B','F'],
    'F' : ['C'],
    'G' : []
}

neo = DFS(graph)
neo.scc()
print(neo.is_dag())