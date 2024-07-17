class Node:
    def __init__(self):
        self._neighbours = None
        self._container = None

    def __hash__(self):
        return hash(tuple(self._neighbours.items()))

    def set_neighbours(self):


    def get_neighbours(self):
        return self._neighbours

    def get_container(self):
        return self._container


class Graph:
    def __init__(self, conexions: dict[Node, list[Node]]):
        self._conexions = conexions

    def get_neighbours_node(self, node):
        return self._conexions[node]
