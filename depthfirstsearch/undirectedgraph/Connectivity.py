class DFS():
    '''
    This DFS show which connected component each nodes belongs.
    undirected graph only
    '''
    def __init__(self, graph):
        self.graph = graph
        self.visited = dict.fromkeys(graph, False)

        # id of connected component
        self.belong = dict.fromkeys(graph, -1)
        self.cc = 0

    def _explore(self, v):
        '''
        What part of graph are reachable from
        a give vertex?
        '''
        self.visited[v] = True
        # previsit 
        print(self.cc)
        self.belong[v] = self.cc # !!!
        for u in self.graph[v]:
            if not self.visited[u]:
                self._explore(u)
        #postvisit
    
    def dfs(self):
        # self.visited = dict.fromkeys(graph, False)
        for u in self.graph:
            if not self.visited[u]:
                self.cc += 1 # !!!
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
print(neo.belong)
