# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'Our adventurer {self.name} is currently in room {self.current_room}'

    def room_info(self):
        return f'player class has: Player({self.name}), Room name:{self.current_room.name}. description: {self.current_room.description}'

    
# print(Player.room_info)