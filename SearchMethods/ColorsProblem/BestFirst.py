class BestFirst:
    def __init__(self, graph: dict[str, list[str]], max_colors = float("inf")):
        self._graph = graph
        self._max_color = max_colors

        self._colors = {node: 0 for node in self._graph}
        self._nodes_visited = 0

    def _color(self, node):
        self._nodes_visited += 1
        color = self._pick_color(node)

        if color > self._max_color:  # There is no possible color for this node
            self._colors[node] = 0  # Reset the color of the node
            return False

        self._colors[node] = color

        next_node = self._get_next_node()
        if not next_node:
            return True  # There is no more nodes to color

        # Colour the next node in the list
        result = self._color(next_node)

        if not result:  # If the result was unsuccessful, that means, we
            # have not found a valid color for the next node given the current state
            # recolor this node and try again
            return self._color(node)

        return True  # If everything has been successful

    def _pick_color(self, node):
        i = self._colors[node] + 1  # Get the next color of the node (in case that a previous color didn't work)
        neighbour_colors = set(self._colors[neighbour] for neighbour in self._graph[node])
        while (i in neighbour_colors) and i <= self._max_color:
            i += 1

        return i

    def _get_next_node(self):
        try:
            return max((node for node in self._graph if self._colors[node] == 0), key=self._count_uncolored_neighbours)

        except ValueError as e:
            return None

    def _count_uncolored_neighbours(self, node):
        return len(list(neighbour for neighbour in self._graph[node] if self._colors[neighbour] == 0))

    def get_answer(self):
        # If coloring has been successful, then return the answer, else there is no answer
        return self._colors if self._color(self._get_next_node()) else None

    def get_nodes_visited(self):
        return self._nodes_visited
