from collections import defaultdict

class DetectCycle:

    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,s):
        print("Length of visted array   :",len(self.graph))
        self.visited=[False] * (len(self.graph))
        stack=[]
        stack.append(s)
        print(s)
        self.visited[s]=True
        isCycle=False
        while stack:
            s=stack.pop()
            for node in self.graph[s]:
                print("Node",node)
                if self.visited[node]==True:
                    isCycle=True
                    break
                else:
                    stack.append(node)
                    self.visited[node]=True
                
        if isCycle==True:
            print("There is cycle present")
        else:
            print("No cycle present in graph")

       
g = DetectCycle() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
# g.addEdge(2, 0) 
g.addEdge(2, 3) 
# g.addEdge(3, 3) 
  
g.DFS(0)
  
