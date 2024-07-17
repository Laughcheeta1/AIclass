class DFS:
    def __init__(self, graph: dict[str, list[str]], max_colors=float("inf")):
        self._graph = graph
        self._max_colors = max_colors

        self._colors = {color: 0 for color in graph}
        self._nodes_visited = 0

    def color(self, node):
        self._nodes_visited += 1
        # Try to get the first available color
        color = self.pick_color(node)

        if color > self._max_colors:  # This means that no color is valid for this node
            self._colors[node] = 0  # Reset the color to cero (in case it was different before)
            return False

        # If the color indeed is valid, then set the current color for that node
        self._colors[node] = color

        # Now check for the neighbours
        valid_color = True  # Initially, that the current color is valid

        for neighbour in sorted(self._graph[node]):
            if self._colors[neighbour] != 0:  # Already has been assigned a color
                continue

            if not (valid_color := self.color(neighbour)):  # If a given neighbour cannot be assigned a color
                # then stop the execution of more neighbours
                break

        """
        If the neighbour cannot be assigned a color with this current state, then we have to try another color
        for this node
        """
        if not valid_color:
            return self.color(node)

        return True  # Assigned a color successfully

    def pick_color(self, node):
        i = self._colors[node] + 1  # Get the next color of the node (in case that a previous color didn't work)
        neighbour_colors = set(self._colors[neighbour] for neighbour in self._graph[node])
        while (i in neighbour_colors) and i <= self._max_colors:
            i += 1

        return i

    def get_answer(self):
        """
        I'm using a validation function for all the nodes instead of using a flag
        (like I was using before, that changed itself everytime a correct color was found)
        because in average, the validation function is more efficient than the flag.

        The validation will take exactly n iterations, while the flag will change n or more times.
        """
        return self._colors if self.color(min(self._graph.keys())) else None

    def get_nodes_visited(self):
        return self._nodes_visited
