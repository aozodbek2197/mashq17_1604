# 1-mashq
class WriteRepo:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

class ReadRepo:
    def __init__(self, source):
        self.source = source

    def get_all(self):
        return self.source.data
# 2-mashq
class EventStore:
    def __init__(self):
        self.events = []

    def save(self, event):
        self.events.append(event)

    def replay(self):
        for e in self.events:
            print(e)
# 3-mashq
class User:
    def __init__(self, name):
        self.name = name

    def change_name(self, new):
        self.name = new
# 4-mashq
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount
# 5-mashq
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
