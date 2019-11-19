# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room_player):
        self.name = name
        self.current_room_player = current_room_player

    def __str__(self):
        return f'Our adventurer {self.name} is currently in room {self.current_room_player}'