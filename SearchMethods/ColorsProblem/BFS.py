class BFS:
    def __init__(self, graph: dict[str, list[str]], max_colors = float("inf")):
        self._graph = graph
        self._max_color = max_colors

        self._colors = {node: 0 for node in self._graph}
        self._queue = list(sorted(graph.keys()))
        self._changed_nodes = list()

    def color(self, node):
        color = self.pick_color(node)

        if color > self._max_color:  # There is no possible color for this node
            self._colors[node] = 0  # Reset the color of the node
            return False

        self._colors[node] = color

        # After we have coloured the current node, we have to add the neighbours to the queue
        self._queue.extend(sorted(self._graph[node]))

        # Colour the next node in the list
        result = self.color(self._queue.pop(0))

        if not result:  # If the result was unsuccessfull, that means, we
            # have not found a valid color for the next node given the current state
            # re color this node and try again
            return self.color(node)


    def pick_color(self, node):
        i = self._colors[node] + 1  # Get the next color of the node (in case that a previous color didn't work)
        neighbour_colors = set(self._colors[neighbour] for neighbour in self._graph[node])
        while (i in neighbour_colors) and i <= self._max_color:
            i += 1

        return i



