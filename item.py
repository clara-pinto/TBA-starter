"""Item module for the game."""

DEBUG = True


class Item():
    """Represents an item in the game."""

    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """Return the string representation of the item."""
        return self.name + self.description
