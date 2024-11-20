
class Delegator:
    delegates: list

    def __init__(self):
        self.delegates = []

    def add_delegate(self, delegate):
        if not delegate in self.delegates:
            self.delegates.append(delegate)

    def remove_delegate(self, delegate):
        if delegate in self.delegates:
            self.delegates.remove(delegate)
