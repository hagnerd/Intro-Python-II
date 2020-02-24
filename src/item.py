class Item:
    """ Represents an item that can be picked up and used by the player """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have picked up {self.name}')

    def on_drop(self):
        print(f"You drop the {self.name} on the floor. It's not your floor so who cares if it's littering.")
