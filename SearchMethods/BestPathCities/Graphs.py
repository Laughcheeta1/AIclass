from ..BaseClass.Node import Node


class City(Node):
    def __init__(self, state, value, operators, operator=None, parent=None, objective=None):
        super().__init__(state, value, operators, operator, parent, objective)

    def get_state(self):
        return self.state

