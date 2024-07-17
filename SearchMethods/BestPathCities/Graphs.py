class Node:
    def __init__(self, neighbours: dict[str, int]):
        self._neighbours = neighbours
        self._container = None

    def get_neighbours(self):
        return self._neighbours

    def get_container(self):
        return self._container


class Graph:
    def __init__(self):
        self._nodes = {
            "Arad": Node({"Zerind": 75, "Timisoara": 118, "Sibiu": 140}),
            "Bucharest": Node({"Urziconi": 85, "Pitesti": 101, "Giurgiu": 82, "Fagaras": 211}),
            "Craiova": Node({"Dobreta": 120, "Rimnicu": 146, "Pitesti": 138}),
            "Dobreta": Node({"Mehadia": 75, "Craiova": 120}),
            "Eforie": Node({"Hirsora": 86}),
            "Fagaras": Node({"Sibiu": 99, "Bucharest": 211}),
            "Giurgiu": Node({"Bucharest": 82}),
            "Hirsora": Node({"Urziconi": 98, "Eforie": 86}),
            "Iasi": Node({"Vaslui": 92, "Neamt": 78}),
            "Lugoj": Node({"Timisoara": 111, "Mehadia": 70}),
            "Mehadia": Node({"Lugoj": 70, "Dobreta": 75}),
            "Neamt": Node({"Iasi": 78}),
            "Oradea": Node({"Zerind": 71, "Sibiu": 151}),
            "Pitesti": Node({"Rimnicu": 97, "Bucharest": 101, "Craiova": 138}),
            "Rimnicu": Node({"Sibiu": 80, "Pitesti": 97, "Craiova": 146}),
            "Sibiu": Node({"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu": 80}),
            "Timisoara": Node({"Arad": 118, "Lugoj": 111}),
            "Urziconi": Node({"Bucharest": 85, "Hirsora": 98, "Vaslui": 142}),
            "Vaslui": Node({"Iasi": 92, "Urziconi": 142}),
            "Zerind": Node({"Arad": 75, "Oradea": 71})
        }
        self._air_distances_to_bucharest = {
            "Arad": 366,
            "Craiova": 160,
            "Dobreta": 242,
            "Eforie": 161,
            "Fagaras": 178,
            "Giurgiu": 77,
            "Hirsora": 151,
            "Iasi": 226,
            "Lugoj": 224,
            "Mehadia": 241,
            "Neamt": 234,
            "Oradea": 380,
            "Pitesti": 98,
            "Rimnicu": 193,
            "Sibiu": 253,
            "Timisoara": 329,
            "Urziconi": 80,
            "Vaslui": 199,
            "Zerind": 374
        }

    def get_neighbours_node(self, node):
        return self._nodes[node].get_neighbours()

    def get_cost(self, node: str):
        return self._nodes[node].get_container

    def get_heuristic(self, node: str):
        return self._air_distances_to_bucharest[node]

    def get_nodes(self):
        return self._nodes
