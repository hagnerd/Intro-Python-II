"""
The main gameplay loop
"""

import textwrap
from player import Player
from room import Room
from item import Item

# Declare all the rooms

items_1 = [
    Item('candle', 'The wick is still in good shape. If you had a match you might be able to light it'),
]

items_2 = [
    Item('torn map', 'A language you don\'t know is scrawled across the map.')
]

items_3 = [
    Item('match', 'As luck would have it, you found a match, but no striking box.')
]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items_1),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items_3),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items_2),
}

commands = {
    'n': 'Go to the north',
    's': 'Go to the south',
    'e': 'Go to the east',
    'w': 'Go to the west',
    'q': 'Quit the game',
    'help': 'Print the list of commands with description',
    'get': 'Picks up an item from the current room if any are available',
    'take': 'Picks up an item from the current room if any are available',
    'drop': 'Drops an item in the players possession',
    'inventory': 'Lists all items in a players inventory',
    'i': '',
}

def is_valid_command(command):
    global commands
    f_command = commands.get(command)
    return f_command is not None or command.startswith('get') or command.startswith('take') or command.startswith('drop')

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

def main_loop(player=None, proceed=True):
    if not proceed:
        print('Quitting the game now')
        return None

    if player is None:
        global room
        name = input("What is your name adventurer?\n")
        print(f"\nWell met {name}. You look rather weary from your adventures, but you have only just begun.\n")
        player = Player(name, room['outside'])
    print_current_info(player)
    get_next_move(player)


def print_items_in_room(room):
    if len(room.items) > 0:
        print("\nYou find the following items of value:")
        for item in room.items:
            print(f"A {item.name}. {item.description}\n")
    else:
        print("You find no items of use in this room")


def print_current_info(player):
    print(f"{player.current_room.name}:")
    print("=" * len(player.current_room.name))
    print("\n".join(
        textwrap.wrap(player.current_room.description, 80))
          )
    print_items_in_room(player.current_room)
    print("\n")

def get_next_move(player):
    print_instructions()
    instruction = input('\nWhat would you like to do next?\n').strip()
    should_continue = parse_input(instruction, player)
    print(f"{'-' * 80}\n")
    main_loop(player, should_continue)


def invalid_input():
    print('The input you entered is invalid')

def print_instructions():
    print("Instructions:")
    print("=" * len("Instructions:"))
    print("\n".join(textwrap.wrap("""Enter `n` to go north, `e` to go east, `s` to go south, or `w` to go west. Type help to a see a list of additional commands""", 80)))

def handle_get(item_name, player):
    if not player.current_room.has_item(item_name):
        print(f'The room you are in does not have the {item_name}')
        get_next_move(player)
    else:
        player.pick_up(item_name)

def handle_move(player, direction):
    next_room = player.current_room.get_room_to(direction)

    if next_room is None:
        print("\nNo room is available that way\n")
        get_next_move(player)
    else:
        print('\n')
        player.move_room(next_room)

def handle_drop(item_name, player):
    player.drop(item_name)


def is_move_command(user_input):
    return user_input in ['n', 'w', 'e', 's']

def parse_input(user_input, player):
    """ Parses the user's input """

    if user_input == 'q':
        return False

    if not is_valid_command(user_input):
        invalid_input()
        get_next_move(player)
    elif is_move_command(user_input):
        handle_move(player, user_input)
    elif user_input in ('inventory', 'i'):
        player.print_inventory()
    elif user_input.startswith('get'):
        item = user_input.split('get ')[1]
        handle_get(item, player)
    elif user_input.startswith('take'):
        item = user_input.split('take ')[1]
        handle_get(item, player)
    elif user_input.startswith('drop'):
        item = user_input.split('drop ')[1]
        handle_drop(item, player)

    return True


main_loop()

# Make a new player object that is currently in the 'outside' room.

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
