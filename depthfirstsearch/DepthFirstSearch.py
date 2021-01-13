class DFS():
    def __init__(self, graph):
        self.graph = graph
        self.visited = dict.fromkeys(graph, False)
        
    def explore(self, v):
        '''
        What part of graph are reachable from
        a give vertex?
        '''
        self.visited[v] = True
        # previsit
        print(v)
        for u in self.graph[v]:
            if not self.visited[u]:
                self.explore(u)
        #postvisit

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

neo = DFS(graph)
neo.explore('A')