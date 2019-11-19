class Item: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
# repr is good at helping to give devs more information / gives official deets of what value reps
# can help give info about the class, extra info that is useful to present
# i.e. 
    def __repr__(self):
        return f"(name info):{self.name}, (description info):{self.description}"
# str is usually meant for consumer 
    def __str__(self):
        return f"{self.name}, {self.description}"

    def on_take(self):
        print(f'You picked up {self.name}, which is {self.description}')

    def drop_item(self):
        print(f'You dropped item {self.name}!')
    
    def inventory(self, item):
        self.item = item
        for i in self.name:
            if i == item:
                ', '.join(self.name)
                print(f'{item}')

class Potion(Item):
    def __init__(self, name, description, color, heal):
        super().__init__(name, description)
        self.color = color
        self.heal = heal

    def on_take(self, player):
        player.health += self.heal

    

