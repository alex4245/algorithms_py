from graph import Graph

def build_graph():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')
    g.add_edge('a', 'b', 0)
    g.add_edge('b', 'd', 35)
    g.add_edge('d', 'f', 10)
    g.add_edge('a', 'c', 5)
    g.add_edge('c', 'e', 15)
    g.add_edge('e', 'f', 20)
    g.add_edge('b', 'e', 30)
    g.add_edge('c', 'd', 20)
    return g

def dijkstra(g, start, finish):
    def _find_lowest_node():
        lowest_node = None
        lowest_node_cost = float('inf')
        for node, cost in dct_costs.iteritems():
            if node not in visited and cost < lowest_node_cost:
                lowest_node, lowest_node_cost = node, cost
        return lowest_node

    def _find_shortest_way():
        shortest_way = [finish]
        n = parents[finish]
        while n:
            shortest_way.append(n)
            n = parents.get(n)
        shortest_way.reverse()
        return shortest_way

    parents = {}
    dct_costs = {}
    visited = []

    if start in g.nodes:
        dct_costs[start] = 0
    else:
        print "Can't find start node in graph"
        return

    c = start
    while c:
        node_cost = dct_costs[c]
        neighbors = g.edges.get(c, [])
        for n in neighbors:
            cost_n = g.costs[c, n] + node_cost
            old_cost_n = dct_costs.setdefault(n, float('inf'))
            if cost_n < old_cost_n:
                dct_costs[n] = cost_n
                parents[n] = c
        visited.append(c)
        c = _find_lowest_node()

    shortest_way = _find_shortest_way()
    return dct_costs[finish], shortest_way


g = build_graph()
start = input('Enter start node: ')
finish = input('Enter finish node: ')
print dijkstra(g, start, finish)
