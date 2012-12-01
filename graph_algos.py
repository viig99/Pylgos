G = {'A':['B','C','D'],
         'B':['A','C','D'],
         'C':['A','B','D'],
         'D':['A','B','C']}

G2 = {'A':['B','C'],
      'B':['A','C','D'],
      'C':['A','B','D'],
      'D':['B','C']}

G3 = {
      'A' : ['B','C'],
      'B' : ['D'],
      'D' : ['C']  
    }

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

print(find_shortest_path(G3,'A','D'))