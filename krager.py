import math
from copy import deepcopy
class Graph():
  def __init__(self,G):
    self._G = G
  def krager(self):
    G = deepcopy(self._G)
    R = math.ceil(((len(G)*(len(G)-1)) / 2) * math.log(len(G)))
    _min = float('inf')
    for z in xrange(0,int(R)):
      while len(G) > 2:
        from random import choice,randint
        v1 = choice(G.keys())
        v2 = G[v1][randint(1,len(G[v1])-1)]
        G[v1].extend(G[v2])
        for x in G[v2]:
          v3=G[x]
          for i in range(0,len(v3)):
            if v3[i]==v2: v3[i]=v1
        while v1 in G[v1]:
          G[v1].remove(v1)
        del G[v2]
      min_cut = len(G[G.keys()[0]])
      if min_cut < _min: 
        _min = min_cut
        _G = G
    return (_G,_min)

if __name__ == "__main__":
  G2 = {'A':['B','C'],
        'B':['A','C','D'],
        'C':['A','B','D'],
        'D':['B','C']}
  m = Graph(G2)
  print(m.krager()[1])
