"""
    Represents a player in the game
"""

class Player:
    """ Represents the player of our adventure game """
    def __init__(self, name, initial_room, inventory=[]):
        self.name = name
        self.current_room = initial_room
        self.inventory = inventory


    def move_room(self, next_room):
        """ Moves a player to the room that is passed in """
        self.current_room = next_room

    def pick_up(self, item_name):
        """ Adds an item to the players inventory """
        item = self.current_room.remove_item(item_name)
        self.inventory.append(item)
        item.on_take()

    def drop(self, item_name):
        """ Drops an item from the players inventory """
        found_item = None
        new_inventory = []

        for item in self.inventory:
            if item.name == item_name:
                found_item = item
            else:
                new_inventory.append(item)

        if found_item is not None:
            self.inventory = new_inventory

        if found_item is None:
            print(f"You do not have {item_name}")
            return None

        self.current_room.add_item(found_item)

    def print_inventory(self):
        print("")
        if len(self.inventory) > 0:
            print('You have the following items in your possesion:\n')
            for item in self.inventory:
                print(f'A single {item.name}')
        else:
            print('Your bags appear to be empty.\n')

