from heapq import heappush as push,heappop as pop

class Node():
  def __init__(self,i,j,cost,path=None):
    self.i = i
    self.j = j
    self._cost = cost + A[i][j]
    self.m = len(A) - 1
    self.n = len(A[0]) - 1
    if path is not None:
      self.path = path + [(i,j)]
    else:
      self.path = [(i,j)]

  def cost(self):
    return self._cost

  def heuristic(self):
    return ((self.i - self.m)**2 + (self.j - self.n)**2)**0.5

  def steps(self):
    result = []
    i,j,c,p = self.i,self.j,self._cost,self.path
    if i > 0:
      push(result,Node(i-1,j,c,p))
    if j > 0:
      push(result,Node(i,j-1,c,p))
    if i < self.m:
      push(result,Node(i+1,j,c,p))
    if j < self.n:
      push(result,Node(i,j+1,c,p))
    return result

  def __hash__(self):
    return (self.i,self.j).__hash__()

  def __eq__(self,other):
    return self.i == other.i and self.j == other.j

  def __lt__(self,other):
    return self.cost() + self.heuristic() < other.cost() + other.heuristic()

def loadgraph(filename):
  A = []
  f = open(filename)
  for l in f.readlines():
    sub = map(int,l.rstrip().split(','))
    A.append(sub)
  return A

def Astar(start,goal):
  q = [start]
  visited = {}
  while q:
    node = pop(q)
    if node == goal:
      return node
    for step in node.steps():
      if step not in visited or visited[step] > step:
        push(q,step)
        visited[step] = step

if __name__ == "__main__":
  A = loadgraph('matrix.txt')
  start = Node(0,0,0)
  goal = Node(len(A)-1,len(A[0])-1,0)
  result = Astar(start,goal)
  print(result.cost())