class DFS():
    def __init__(self, graph):
        self.graph = graph
        self.visited = dict.fromkeys(graph, False)

    def _explore(self, v):
        '''
        What part of graph are reachable from
        a give vertex?
        '''
        self.visited[v] = True
        # previsit
        print(v)
        for u in self.graph[v]:
            if not self.visited[u]:
                self._explore(u)
        #postvisit
    
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

