# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items
        # if items is None:
        #     self.items = []
        # else:
        #     self.items = items

    def __str__(self):
        return f'Our adventurer {self.name} is currently in {self.current_room}'

    # def get_item(self):
    #     for item in self.items:
    #         print(item)
    #         self.items.append(item)
    #     return None
    def get_item(self):
        if self.current_room.items:
            return f'there are {self.current_room.items} here.'

    def add_item(self):
        self.items.append(self.current_room.items)
        self.items.remove(self.current_room.drop_item)
        print(f'you have picked up {self.current_room.items}')

    def drop_item(self):
        self.items.remove(self.current_room.items)
        print(f'you have dropped {self.current_room.items}')

    def player_inventory(self):
        if len(self.items) != 0:
            ', '.join([str(i) for i in self.items])
            print(f' You have:  {self.items}')
            # return True
        else:
            print(f'{self.name} has no items...')
            # return False