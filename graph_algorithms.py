from collections import deque
from graph import graph

def breadth_first_search(gr, s):
    """ Returns a list of nodes that are "findable" from s """
    if not gr.has_node(s):
        raise Exception("Node %s not in graph" % s)
    else:
        gr.clear_node_attributes()
        q = deque([s])
        gr.add_node_attribute(s, "explored")
        path = [s]
        while len(q) != 0:
            node = q.popleft()
            for each in gr.neighbors(node):
                if gr.node_attributes( each ) != "explored":
                    gr.add_node_attribute(each, "explored")
                    path.append(each)
                    q.append(each)
        return path

def shortest_path(gr, s):
    """ Finds the shortest number of hops required
    to reach a node from s. Returns a dict with mapping:
    destination node from s -> no. of hops
    """
    if not gr.has_node(s):
        raise Exception("Node %s is not in graph" % s)
    else:
        dist = {}
        gr.clear_node_attributes()
        q = deque(s)
        gr.add_node_attribute(s, "explored")
        # initialize dist
        for n in gr.nodes():
            if n == s: dist[n] = 0
            else: dist[n] = float('inf')
        while len(q) != 0:
            node = q.popleft()
            for each in gr.neighbors(node):
                if gr.node_attributes(each) != "explored":
                    gr.add_node_attribute(each, "explored")
                    q.append(each)
                    dist[each] = dist[node] + 1
        return dist

if __name__ == "__main__":
    gr = graph()
    gr.add_nodes(["s", "a", "b", "c", "d", "e", "f", "g", "h"])
    gr.add_edges([("s", "a"), ("s", "b"), ("b", "c"), ("a", "c"), ("b", "d")])
    gr.add_edges([("c", "d"), ("d", "e"), ("c", "e")])
    gr.add_edges([("g", "h"), ("f", "g")])
    print breadth_first_search(gr, "s")
    print breadth_first_search(gr, "g")
    print shortest_path(gr, "s")
