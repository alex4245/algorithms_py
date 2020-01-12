class Graph:
    def __init__(self):
        self._nodes = []
        self._edges = {}
        self._costs = {}

    def add_node(self, node):
        self._nodes.append(node)

    def add_edge(self, f_n, s_n, cost=0):
        self._edges.setdefault(f_n, []).append(s_n)
        self._costs[f_n, s_n] = cost

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges

    @property
    def costs(self):
        return self._costs
