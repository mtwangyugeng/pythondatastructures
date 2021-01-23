class DFS():
    '''
    Collection of algorithms that utilizes Depth-First Search.
    @input: A graph represented by an adjacency list.
    '''
    def __init__(self, graph):
        self.graph = graph
        self.visited = dict.fromkeys(graph, False)

        # pre[v]: when node v is visited
        # post[v]: when all of v's descendants are visited
        # type of edge u-v after dfs: 
            # Tree/forward = u v v u
            # back = v u u v
            # cross = v v u u
        self.clock = 0
        self.pre = dict.fromkeys(graph, None)
        self.post = dict.fromkeys(graph, None)
        
        # record the post number of nodes in decending order
        self.postmaxtomin = []

        # strongly connected component
        self.cc = dict.fromkeys(graph, None)
        self.ccc = -1


    def dfs(self):
        # self.visited = dict.fromkeys(graph, False)
        for u in self.graph:
            if not self.visited[u]:
                self.explore(u)

    def explore(self, v):
        '''
        Visit all decendents of node v.
        @input: v, a node in self.graph
        '''
        self.visited[v] = True # could be replced by pre[v]
        # previsit
        self.cc[v] = self.ccc
        self.pre[v] = self.clock
        self.clock += 1
        # ---------------------

        for u in self.graph[v]:
            if not self.visited[u]:
                self.explore(u)
        
        #postvisit
        self.post[v] = self.clock
        self.clock += 1
        self.postmaxtomin = [v] + self.postmaxtomin
        # ---------------------

    def is_dag(self):
        '''
        Check if the given graph is a directed acyclic graph (DAG)
        A graph is a DAG iff there is no backedge.
        '''
        self.dfs()
        for u in self.graph:
            for v in self.graph[u]:
                if self.pre[v] < self.pre[u] and self.post[u] < self.post[v]:
                    return False
        return True
    
    def reversed_graph(self):
        '''
        Return the reversed graph of self.graph
        '''
        neo = {k: [] for k in self.graph}
        for u in self.graph:
            for v in self.graph[u]:
                neo[v].append(u)
        return neo

    def scc(self):
        '''
        get the strongly connected components in linear time
        '''
        # get the reversed graph and run DFS
        rg = self.reversed_graph()
        neo = DFS(rg)
        neo.dfs()
        ###
            # The node with the largest post number (denoted as u) is 
            # for sure a node in one of the  
            # sources component of rg b/c suppose some node v
            # can get to u and v is not in the same strongly connected
            # component of u, then v will have bigger post number:
            #   case 1: v is explored before u in dfs. 
            #       self.explore(v) will visit u and give it a 
            #       post number smaller than v
            #   case 2: v is explored after u.
            #       It trivially follows that v will have a larger 
            #        post
        ###

        # The source component of rg is the sink component of 
        # self.graph, thus we start from a sink, run explore
        # then go to the next one, etc.
        self.cc = dict.fromkeys(neo.postmaxtomin, None)
        self.visited = dict.fromkeys(graph, False)
        for u in neo.postmaxtomin:
            if not self.visited[u]:
                self.ccc += 1
                self.explore(u)
        print(self.cc)


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
neo.scc()

