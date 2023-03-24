'''#import dictionary for graph
from collections import defaultdict
#Add edge to graph:function
graph=defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
#function description
def generate_edges(graph):
    edges=[]
    # for each node in graph
    for node in graph:
        #for each neighbour node in a singlenode
        for neighbour in graph[node]:
            #if edge exists then append
            edges.append((node,neighbour))
    return edges
#DECLARING-graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
print(generate_edges(graph))

#adjacency matrix
class Graph(object):
    def __init__(self,size):
        self.adjMatrix=[]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
            self.size=size
    #Add edges
    def add_edge(self,v1,v2):
        if v1==v2:
            print("same vertex %d and %d" %(v1,v2))
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        #remove and __len__is not required to this program
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2]==0:
            print("No edges between %d and %d" %(v1,v2))
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
    def __len__(self):
        return self.size
    #print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val))
                
def main():
    g=Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.print_matrix()
if __name__=='__main__':
    main()

#Bfs using queue
graph={
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
    }
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end="")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,graph,'5')#function call'''

#dfs in binary tree
        
graph={
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}
visited=set()
def dfs(visited,graph,node):
    if node
    not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'5')
























        
