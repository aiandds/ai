from collections import defaultdict 
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DLS(self,src,target,maxDepth):
        if src==target:return True
        if maxDepth <=0:return False
        for i in self.graph[src]:
            if(self.DLS(i,target,maxDepth-1)): 
                return True
        return False
    def IDDFS(self,src,target,maxDepth):
        for i in range(maxDepth):
            if(self.DLS(src,target,i)):
                return True
        return False
n=int(input("Enter the Number of Vertices:"))
g=Graph(n)
print("Enter Edges:")
for i in range(n):
    Edge=[]
    Edge=input().split()
    g.addEdge(Edge[0],Edge[1])
target=input("Enter Goal Node Value:\n").strip()
maxDepth=int(input("Enter Max Depth:\n"))       
src='A'
if g.IDDFS(src,target,maxDepth)==True:
    print("Target is reachable from source within max depth")


else:
    print("Target is NOT reachable from source within max depth")
