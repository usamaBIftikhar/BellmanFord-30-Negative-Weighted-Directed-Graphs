class Vertex:
  def __init__(self, name):
    self.name = name
    self.distance = float('inf')  
    self.prev = None
  def getName(self):
    return int(self.name)

  def __repr__(self):
    return str(self.name)

class Edge:
  def __init__(self, source, destination, weight):
    self.source = source
    self.destination = destination
    self.weight = weight

class Bellman:
  def minWeight(self, source, edges, V,vert,graph):
    source.distance = 0
    tot = float(0)
    parent =[-1 for i in range(V+1)]
    for i in range(V-1):
      for edge in edges:
        if edge.source.distance + edge.weight < edge.destination.distance:
          edge.destination.distance = edge.source.distance + edge.weight
          edge.destination.prev = edge.source
          parent[edge.destination.getName()] = edge.source.getName()

    C = -1
    
    for edge in edges:
        if edge.source.distance + edge.weight < edge.destination.distance:
          C = edge.destination.getName()

    if (C != -1):       
        for i in range(V):       
            C = parent[C]
   
        # To store the cycle vertex
        cycle = []       
        v = C
          
        while (True):
            cycle.append(v)
            if (v == C and len(cycle) > 1):
                break
            v = parent[v]
   
        # Reverse cycle[]
        cycle.reverse()
        print(f"G{graph}'s shortest from v0 to v{numVertices-1}:")             
        self.printCycle(cycle, edges,vert)
        print(f"Negative cycle found at {cycle[0]}")
        return False  
        # else:
        #   tot += edge.w
        #   print(f"( {edge.src}, {edge.dest},  {edge.w}) --> {tot}")

    return True

  def shortestPath(self, source, destination):
    vertex = destination
    path = []

    while(vertex is not source):
      path.insert(0, vertex)
      vertex = vertex.prev
    path.insert(0, source)
    self.printPath(path,edges,vert)
    return path
  def printCycle(self, path,edges,vert):
    lpath = len(path)
    spath = []
    tot = float(0)
    for i in range(lpath):
      spath.append(path[i])
    for i in range(len(spath)-1):
      cost = self.getCost(vert[spath[i]], vert[spath[i+1]], edges)
      tot = tot + cost
      print(f"( {spath[i]}, {spath[i+1]},  {cost}) --> {tot}")
  def printPath(self, path,edges,vert):
    lpath = len(path)
    spath = []
    tot = float(0)
    for i in range(lpath):
      spath.append(path[i].getName())
    for i in range(len(spath)-1):
      cost = self.getCost(vert[spath[i]], vert[spath[i+1]], edges)
      tot = tot + cost
      print(f"( {spath[i]}, {spath[i+1]},  {cost}) --> {tot}")

  def getCost(self, src, dest, edges):
    for edge in edges:
      if edge.source == src and edge.destination == dest:
        return float(edge.weight)

  def isEdge(self, dest, edges):
    for edge in edges:
      if edge.source == dest or edge.destination == dest:
        return True

    return False
      
if __name__ == "__main__":
  
  edges = []
  vert = []
  graph = 0
  with open('/content/30-Neg-Weighted-Directed-Graphs.txt') as inpt:
    while True:
        data = inpt.readline() 
        if not data:
          break
        else:
          if(list(data)[0]=='*'):
            numVertices = int(data.split("=")[-1])
            for i in range(numVertices):
              vert.append(Vertex(i))
            inpt.readline()
            while True:
              vertices = inpt.readline()
              if(len(vertices)>25):
                vertexData = vertices.split(",")
                vertex = vertexData[0].split("(")
                weight = vertexData[2].split(")")
                w = float(weight[0][1:])
                v = int(vertexData[1][1:])
                u = int(vertex[1])
                edges.append(Edge(vert[u],vert[v], w))
                break
              else:
                vertexData = vertices.split(",")
                vertex = vertexData[0].split("(")
                weight = vertexData[2].split(")")
                w = float(weight[0][1:])
                v = int(vertexData[1][1:])
                u = int(vertex[1])
                edges.append(Edge(vert[u],vert[v], w))

            bellmanFord = Bellman()
            if bellmanFord.minWeight(vert[0], edges, numVertices-1,vert,graph):
              destin = numVertices-1
              if(graph<17):
                print(f"G{graph}'s shortest from v0 to v{numVertices-1}:")
                shortPath = bellmanFord.shortestPath(vert[0], vert[destin])
              elif bellmanFord.isEdge(destin,edges) and graph>17:
                print(f"G{graph}'s shortest from v0 to v{numVertices-1}:")
                shortPath = bellmanFord.shortestPath(vert[0], vert[destin])
              else:
                print(f"G{graph}'s has no shorter path.")
                
            edges= []
            vert = []
            graph += 1
    