from room import Room
from player import Player
from item import Item
from item import Heal

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


# golden_rock =  Item('golden rock!', 'This might be special.. right?')
# rock = Item('random rock', 'is there  any use?')
# sword = Item('sword', 'a plain sword, looks useful')
# apple = Heal('apple', 'an apple, eat it to gain HP', 5)
# potion = Heal('potion', 'a green potion, heals 20HP', 10)

item = {
    'rock': Item('rock', """You find a random rock and pick it up in case you need it for later"""),
    'golden_rock': Item('golden rock!', 'This might be special.. right?'),
    'sword':  Item('sword', 'a plain sword, looks useful'),
    'apple': Heal('apple', 'an apple, eat it to gain HP', 5),
    'potion':  Heal('potion', 'a green potion, heals 10HP', 10)
}


# room['treasure'].items.append(golden_rock)
# room['foyer'].items.append(rock)
# room['overlook'].items.append(sword)
# room['overlook'].items.append(apple)
# room['foyer'].items.append(potion)

room['treasure'].items = [item["golden_rock"].name_only()]
room['overlook'].items = [item["sword"].name_only(), item['apple'].name_only()]
room['foyer'].items = [item['rock'].name_only(), item['potion'].name_only()]
room['narrow'].items = [item['potion'].name_only()]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Input name: '), room['outside'])
# player.items = [items['rock']]
# listing the player name after player gets created
print(f'Player\'s name is: {player.name}')
print(f'Player is in room: {player.current_room.name}')
print(f'Items in {player.current_room.name}: {player.current_room.check_item([])}')
# print(f'items in this room????: {player.current_room.print_item()}')
print(player.current_room.desc_only())

# Write a loop that:
#
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player_selection = ""

#LOOP
while True:

    print(player)
    # player.current_room.check_items3([])
    # player.current_room.check_item2([])
    print(f'Player is in room: {player.current_room.name}')
    print(f'Items in {player.current_room.name}: {player.current_room.print_item()}')
    # print(f'Description of items: {player.current_room.desc_only()}')
    # print(f'items in this room????: {player.current_room.print_item()}')
    print(player.current_room.desc_only())
    player.current_room.print_item
    # player.current_room.check_items3([])
    player.player_inventory()
    # print(player.room_info())
    
    # READ
    player_selection = input('Select a direction (n, e, s, w or q to quit), you can pick up items with get and drop too or enter to skip ').strip().split(' ')
    # .strip().split(' ')
    # EVALUATE
    try: 
        # player_selection = str(player_selection)
        if len(player_selection) == 1:
            if player_selection[0] == "n" or player_selection[0] == "north":
                if player.current_room.n_to is not None:
                    player.current_room = player.current_room.n_to
                print('player pressed north')
            elif player_selection[0] == "e" or player_selection[0] == "east":
                if player.current_room.e_to is not None:
                    player.current_room = player.current_room.e_to
                print('player pressed east')
            elif player_selection[0] == "s" or player_selection[0] == "south":
                if player.current_room.s_to is not None:
                    player.current_room = player.current_room.s_to
                print('player pressed south')
            elif player_selection[0] == "w" or player_selection[0] == "west":
                if player.current_room.w_to is not None:
                    player.current_room = player.current_room.w_to
                print('player pressed west')
            elif player_selection[0] == "i" or player_selection[0] == "inventory":
                print(player.current_room.player_inventory())
                print('inventory')
            elif player_selection[0] == "q" or player_selection[0] == "quit":
                print('thanks for playing!')
                break
            else: 
                print('please print valid key.. ')
        elif len(player_selection) == 2:
            if player_selection[0] == 'get':
                for i in player.current_room.items:
            
                    print('item object', i)
                    # print(i.name)
                    if i == player_selection[1]:
                        player.current_room.drop_item(i)
                        player.current_room.add_item(i)
                        player.add_item()
            elif player_selection[0] == 'drop':
                for i in player.current_room.items:
                    print('item object', i)
                    # print(i.name)
                    if i == player_selection[1]:
                        player.current_room.drop_item(i)
                        player.current_room.add_item(i)
                        player.drop_item()
        else: 
            print('not a valid room input')
    except ValueError:
        print("ValueError!! User input has to be string, not an integer")
