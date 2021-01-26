class DistHeap():
    def __init__(self, graph, s):
        self.dists = dict.fromkeys(graph, float('inf'))
        self.pointer = dict.fromkeys(self.dists, None)
        self.Heap = [s]

        self.pointer[s] = 0
        self.dists[s] = 0
        i = 1
        for k in self.pointer:
            if k != s:
                self.pointer[k] = i
                self.Heap += [k]
                i += 1
        

    def parent(self, pos):
        return (pos-1)//2
 
    def leftChild(self, pos):
        return 2 * pos + 1

    def rightChild(self, pos):
        return (2 * pos) + 2

    def swap(self, fpos, spos):
        self.pointer[self.Heap[fpos]], self.pointer[self.Heap[spos]] = self.pointer[self.Heap[spos]], self.pointer[self.Heap[fpos]]
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def decreasekey(self,k):
        # if the parent's value is bigger, swap
        kpos = self.pointer[k]
        if kpos > 0: 
            parent = self.parent(kpos) # parent's pointer
            if self.dists[k] < self.dists[self.Heap[parent]]: #parent's value
                self.swap(kpos, parent)
                self.decreasekey(k)
    
    def popmin(self):
        self.swap(0, -1)
        poping = self.Heap.pop()
        del self.pointer[poping]
        # del self.dists[poping]
        if(self.Heap):
            self.downward(self.Heap[0])
        return poping
    
    def downward(self, k):
        leftpos = self.leftChild(self.pointer[k])
        rightpos = self.rightChild(self.pointer[k])
        candi = None
        if leftpos < len(self.Heap) and rightpos < len(self.Heap):
            if self.dists[self.Heap[leftpos]] < self.dists[self.Heap[rightpos]]:
                candi = leftpos
            else:
                candi = rightpos
        elif leftpos < len(self.Heap):
            candi = leftpos
        elif rightpos < len(self.Heap):
            candi = rightpos
        if candi and self.dists[self.Heap[candi]] < self.dists[k]:
            self.swap(candi, self.pointer[k])
            self.downward(k)


class BFS():
    def __init__(self, graph):
        self.graph = graph
    def dijkstra(self, s):
        prevs = dict.fromkeys(self.graph, None)
        # get priority queue
        pq = DistHeap(self.graph, s)
        while pq.Heap:
            u = pq.popmin()
            for e in self.graph[u]:
                if pq.dists[e[0]] > pq.dists[u] + e[1]:
                    pq.dists[e[0]] = pq.dists[u] + e[1]
                    prevs[e[0]] = u
                    pq.decreasekey(e[0])
        return pq.dists , prevs

graph = {
    'A' : [('B',2),('C',3),('D',1)],
    'B' : [('D',4), ('E',3)],
    'C' : [('F',1)],
    'D' : [],
    'E' : [('F', 7)],
    'F' : [],
    'G' : []
}

neo = BFS(graph)
print(neo.dijkstra('A'))
