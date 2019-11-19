from room import Room
from player import Player
from item import Item
from item import Potion

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

#instantiate the item class
rock = Item('rock', 'Just a rock.. or is it?!')
crown = Item('crown', 'It\'s a golden crown!')
magic_wand = Item('magic_wand', 'A magic wand appeared!')
potion = Potion('purple_potion', 'heals 25 HP', "purple", 50)

room['foyer'].items.append(potion)
room['foyer'].items.append(rock)
room['outside'].items.append(rock)
room['treasure'].items.append(crown)
room['overlook'].items.append(magic_wand)
room['narrow'].items.append(rock)
room['overlook'].items.append(rock)
room['treasure'].items.append(rock)
room['overlook'].items.append(potion)

#
# Main
# Just checking if the item crown will print
# print(f'check items: {crown.name}')
# Make a new player object that is currently in the 'outside' room.
player = Player(input('select name: '), room['outside'], [])
valid_directions = ['n', 's', 'e', 'w']
print("Welcome to J's Room Search Adventure! (Version 1)")
print('Current user: ', player.name)

print(player.current_room.name)
#we want to print the items in the room





#       
# * Prints the current room name
while True: 
    player.show_room()
    player.current_room.items_list()
    player.current_room.inventory_quantity()

#   selection = input("Select a room to enter! and an item to pick up!'get' or 'drop' or enter to skip: ")lower().split(' ')

    try: 
        selection = input("Select a room to enter! and an item to pick up!'get' or 'drop' or enter to skip: ").strip().split(' ')
        if len(selection) == 1:
            if selection[0] == "q" or selection[0] == "quit":
                print("Thanks for playing!")
                break
            elif selection[0] == "n" or selection[0]== "north":
                if player.current_room.n_to is not None:
                    player.current_room = player.current_room.n_to
                else:
                    print('Not sure where you are... try something else')
            elif selection[0] == "s" or selection[0] == "south":
                if player.current_room.s_to is not None:
                    player.current_room = player.current_room.s_to
                else:
                    print('Not sure where you are...')
            elif selection[0] == "w" or selection[0] ==  "west":
                if player.current_room.w_to is not None:
                    player.current_room = player.current_room.w_to
                else:
                    print('not sure where you are, try a different direction')
            elif selection[0] == "e" or selection[0] == "east":
                if player.current_room.e_to is not None:
                    player.current_room = player.current_room.e_to
                    print('not sure where you are, try a different direction')
            elif selection[0] == "pick" or selection[0] == "get":
                player.add_item()
            elif selection[0] == "drop" or selection[0] == "d":
                player.drop_item()
            elif selection[0] == "i" or selection[0] == "inventory":
                print(player.player_inventory())
        elif len(selection) == 2:
            if selection[0] == "get":
                for item in player.current_room.items:
                    if item.name == selection[1]:
                        player.current_room.drop_item(item)
                        player.current_room.add_item(item)
                        player.add_item()
                        # item.on_take()
                    else:
                        print("\nNo item by that name exists.")
            elif selection[0] == "drop":
                for item in player.items:
                    if item.name == selection[1]:
                        player.current_room.drop_item(item)
                        player.drop_item()
                        # player.current_room.add(item)
        else: 
            print ("You can only select 'n', 's','w', 'e', 'i', 'get', 'g', 'drop', 'd'. Press 'q' to quit ")

    except ValueError:
        print("You can only enter a string!")
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the self.
