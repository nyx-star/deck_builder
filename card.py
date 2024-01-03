

class card:

    def __init__(self, name, actions, cost):
        self.name = name
        self.actions = actions
        self.coalcost = cost

    def getname(self):
        return self.name

    def getactions(self):
        return self.actions

    def getcoalcost(self):
        return self.coalcost