from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, name, pos, total,icon=""):
        self.name = name
        self.pos = pos
        self.total = total
        self.icon = icon

class Composite(Component):
    def __init__(self, name, pos, total, icon):
        super().__init__(name, pos, total, icon)
        self.children = []

    def add(self, component):
        self.children.append(component)

class Leaf(Component):
    def __init__(self, name, pos, total, icon, value=None):
        super().__init__(name, pos, total, icon)
        self.value = value
