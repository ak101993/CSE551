class Dijkrtas:

    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[]]

    def find_min(self,distance,visited):
        minimum_value=999999
        for i in range(self.vertices):
            if distance[i]<minimum_value and visited[i]==False:
                minimum_value=distance[i]
                min_index=i
        
        return min_index

    def dijktras(self,start):
        distance = [999999] * self.vertices
        distance[start] = 0
        visited = [False] * self.vertices 
        for cout in range(self.vertices):
            u=self.find_min(distance,visited)
            print("u",u)
            visited[u]=True

            for v in range(self.vertices):
                print("Graph Adjacency ",self.graph[u][v])
                if self.graph[u][v] >0 and visited[v]==False and distance[v]>distance[u]+self.graph[u][v]:
                    distance[v]=distance[u]+self.graph[u][v]
        
        self.printSolution(distance)

    def printSolution(self, distance):
        print("Vertex \tDistance from Source")
        for node in range(self.vertices): 
            print( distance[node])
  

g = Dijkrtas(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 

g.dijktras(0)