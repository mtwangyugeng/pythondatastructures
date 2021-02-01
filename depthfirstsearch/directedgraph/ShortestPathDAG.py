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
        for u, _ in self.graph[v]:
            if not self.visited[u]:
                self._explore(u)
        #postvisit
        self.post[v] = self.clock
        self.postmaxtomin = [v] + self.postmaxtomin
        self.clock += 1

    def dag_shortest_path(self, s):
        """
        For all vertices u reachable from s in self.graph,
        dists[u] is set to the distance from s to u.
        Our update sequence is from the highest post 
        number to the lowest. i.e. the linearation of
        the dag.
        """ 
        dists = dict.fromkeys(self.graph, float('inf'))
        prevs = dict.fromkeys(self.graph, None)
        
        dists[s] = 0
        self.dfs()
        for u in self.postmaxtomin:
            for v,l in self.graph[u]:
                if dists[v] > dists[u] + l:
                    dists[v] = dists[u] + l
                    prevs[v] = u
        return dists, prevs

    def dfs(self):
        # self.visited = dict.fromkeys(graph, False)
        for u in self.graph:
            if not self.visited[u]:
                self._explore(u)

graph = {
    'A' : [('B',2),('C',3),('D',1)],
    'B' : [('D',4), ('E',-3)],
    'C' : [('F',1)],
    'D' : [],
    'E' : [('F', -7)],
    'F' : [],
    'G' : []
}

neo = DFS(graph)
print(neo.dag_shortest_path('A'))
