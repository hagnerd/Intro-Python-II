"""
Reperents a room in our adventure game
"""


class Room:
    """ Represents a room in our adventure game """
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def add_item(self, item):
        self.items.append(item)
        item.on_drop()

    def get_room_to(self, direction):
        room = None

        if direction == 'n':
            room = self.n_to
        elif direction == 'e':
            room = self.e_to
        elif direction == 's':
            room = self.s_to
        elif direction == 'w':
            room = self.w_to

        return room

    def has_item(self, item_name):
        has_item = False
        for item in self.items:
            if item.name == item_name:
                has_item = True
        return has_item

    def get_item(self, item_name):
        f_item = None
        for item in self.items:
            if item.name == item_name:
                f_item = item
        return f_item

    def remove_item(self, item_name):
        item = self.get_item(item_name)
        if item is not None:
            self.items = list(filter(lambda item: item.name != item_name,
                                     self.items))
        return item
