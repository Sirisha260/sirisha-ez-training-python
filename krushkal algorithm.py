class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph =[]
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

        #search function
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    def apply_union(self,parent,rank,x,y):
        print("rank",rank)
    # to avoid cycle attach smaller rank tree under high rank tree,if both same make anyone asparent  and
    #make its rank as 1 union can be in 2 disjoint sets
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
        #applying Krushkal algorithm
    def  krushkal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph,key=lambda item:item[2])
        #means taking edgesand sorting in terms of weight weight at index2.
        #like in graph u,v,w...position 0,1,2
        parent=[]
        rank=[]
        for node in range(self.v):
            print("Node",node)
            print()
            parent.append(node)
            rank.append(0)
        print("parent",parent)
        print("rank",rank)
        while e< self.v-1:#bcz mst should have n-1 edges
            u,v,w = self.graph[i]
            print("U:",u,"V:",v,"W:",w)
            i=i+1
            x = self.find(parent,u)
            print("X:",x,"Parent of u:",u)
            y=self.find(parent,v)
            print("Y:",y)
            if x!=y:
                e=e+1
                result.append([u,v,w])
                #we are discarding eges which frames cycle
                self.apply_union(parent,rank,x,y)
        for u,v,weight in result:
            print("%d -- %d : %d" %(u,v,weight))
g=Graph(6)
g.add_edge(0,1,4)
g.add_edge(0,2,4)
g.add_edge(1,2,2)
g.add_edge(1,0,4)
g.add_edge(2,0,4)
g.add_edge(2,1,2)
g.add_edge(2,3,3)
g.add_edge(2,5,2)
g.add_edge(2,4,4)
g.add_edge(3,2,3)
g.add_edge(3,4,3)
g.add_edge(4,2,4)
g.add_edge(4,3,3)
g.add_edge(5,2,2)
g.add_edge(5,4,3)
g.krushkal_algo()












        







        
