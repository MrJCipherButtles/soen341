from abc import ABC


class Item(ABC): # ABC is Abstract Base Class
    def __init__(self, id):
        self.id = id
