
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'item {self.name} is {self.description}'


class Heal(Item):
    def __init__(self, name, description, health_points):
        super().__init__(name, description)
        self.health_points = health_points

    def __str__(self):
        return f'potion {self.name} is {self.description} and have a HP of {self.health_points}'

