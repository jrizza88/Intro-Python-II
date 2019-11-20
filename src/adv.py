from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Input name: '), room['outside'])

# listing the player name after player gets created
print(f'Player\'s name is: {player.name}')
print(f'Player is in room: {player.current_room_player.name}')

print(f'player.room_info()')
# Write a loop that:
#
# * Prints the current room name
# while True: 
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player_selection = ''

#LOOP
while player_selection != "q" or player_selection != "quit":

    # player.room_info()
    # READ
    player_selection = input('Select a direction (n, e, s, w or q to quit)')
    # EVALUATE
    try: 
        player_selection = str(player_selection)
        if player_selection == "n" or player_selection == "north":
            print('player pressed north')
        elif player_selection == "e" or player_selection == "east":
            print('player pressed east')
        elif player_selection == "s" or player_selection == "south":
            print('player pressed south')
        elif player_selection == "w" or player_selection == "west":
            print('player pressed west')
        elif player_selection == "q" or player_selection == "quit":
            print('thanks for playing!')
        else: 
            print('not a valid room input')
    except ValueError:
        print("ValueError!! User input has to be string, not an integer")


