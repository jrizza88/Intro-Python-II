# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.health = 150
        if items is None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f'{self.name}, {self.current_room}'
        
    def show_room(self):
        print (f'{self.name} is in room {self.current_room.name}. Description: {self.current_room.description}')

    def add_item(self):
        self.items.append(self.current_room.items)
        self.items.remove(self.current_room.drop_item)
        print(f'you have picked up {self.current_room.items}')

    def drop_item(self):
        self.items.remove(self.current_room.items)
        print(f'you have dropped {self.current_room.items}')

    def health_meter(self):
        print(f'{self.name}\'s health is: {self.health}')

    def player_inventory(self):
        if len(self.items) != 0:
            ', '.join([str(i) for i in self.items])
            print(f' You have:  {self.items}')
            # return True
        else:
            print(f'{self.name} has no items! Find some!')
            # return False