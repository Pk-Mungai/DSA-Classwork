class Ge:
    def __init__(self, directed = False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_string = ""

        for node, neighbours in self.adj_list.items():
            graph_string += f"{node} -> {neighbours} \n"

        return graph_string



    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")


    def add_edge(self, from_node, to_node, weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None: # When the weight is none e.g. dict{A: B, C, D}
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)

        else: # When there is a weight e.g. dict{A: (B,2) , (C,24) , (D,98)}
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
        
        return order
    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)
                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        
        return order

    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())

if __name__ == "__main__":
    graph1 = Ge(directed=True)
    graph1.add_edge("A", "B" , 2)
    graph1.add_edge("A", "J", 2)
    graph1.add_edge("B", "D", )
    graph1.add_edge("A", "D", 4)
    graph1.add_edge("A", "C", 3)
    graph1.add_edge("C", "D", 7)

    print(graph1)
    print("BREADTH FIRST SEARCH:")
    print(graph1.bfs("A"))
    print("DEPTH FIRST SEARCH:")
    print(graph1.dfs("A"))

