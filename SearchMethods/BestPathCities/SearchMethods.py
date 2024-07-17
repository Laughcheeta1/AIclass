from SearchMethods.BestPathCities.Graphs import Graph


class BFS:
    def __init__(self, start="Arad", goal="Bucharest"):
        self._graph = Graph()

        self._goal = goal
        self._current_node = start

        self._visited = set()
        self._best_path = list()
        self._queue = list()

        # Enter te starting city as already visited
        self._visited.add(start)

    def perform_search(self):
        while self._current_node != self._goal:
            # Add the current node
            self._queue.append(list(
                node for node in sorted(self._graph.get_neighbours_node(self._current_node))
                if node not in self._visited
                )
            )

            self.next_node()

            # TODO apply the logic to create the path

    def next_node(self):
        self._current_node = self._queue.pop(-1)
