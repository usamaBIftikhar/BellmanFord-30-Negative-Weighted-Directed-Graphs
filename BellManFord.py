class Vertex:
  def __init__(self, v):
    self.v = v
    self.d = float('inf')  
    self.prev = None
  def getV(self):
    return self.v

  def __repr__(self):
    return str(self.v)

class Edge:
  def __init__(self, src, dest, w):
    self.src = src
    self.dest = dest
    self.w = w

class Bellman:
  def minWeight(self, source, edges, v):
    source.d = 0
    for i in range(v-1):
      for edge in edges:
        if edge.src.d + edge.w < edge.dest.d:
          edge.dest.d = edge.src.d + edge.w
          edge.dest.prev = edge.src

    for edge in edges:
        if edge.src.d + edge.w < edge.dest.d:
          print(f"Negative cycle found at {edge.src}")
          return False

    return True

  def shortestPath(self, source, destination,edges,vert):
    vertex = destination
    path = []

    while(vertex is not source):
      path.insert(0, vertex)
      vertex = vertex.prev
    path.insert(0, source)

    lpath = len(path)
    spath = []
    tot = float(0)
    for i in range(lpath):
      spath.append(path[i].getV())
    for i in range(len(spath)-1):
      cost = self.getCost(vert[spath[i]], vert[spath[i+1]], edges)
      tot = tot + cost
      print(f"( {spath[i]}, {spath[i+1]},  {cost}) --> {tot}")

    return path

  def getCost(self, src, dest, edges):
    for edge in edges:
      if edge.src == src and edge.dest == dest:
        return float(edge.w)
      
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

          bellman = Bellman()
          if bellman.minWeight(vert[0], edges, len(vert)):
            print(f"G{graph}'s shortest from v0 to v{numVertices-1}:")
            graph += 1
            shortPath = bellman.shortestPath(vert[0], vert[numVertices-1],edges,vert)
           
    