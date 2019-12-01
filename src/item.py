
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'{self.name}:---- {self.description}'

    def name_only(self):
        return f'{self.name}'

    def desc_only(self):
        return f'{self.description}'

    def on_take(self):
        return f'You took the item named: {self.name}'


class Heal(Item):
    def __init__(self, name, description, health_points):
        super().__init__(name, description)
        self.health_points = health_points


    def __str__(self):
        return f'{self.name}: {self.description} and has a HP of {self.health_points}'

