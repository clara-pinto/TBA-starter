"""Character module for the game."""

import random


class Character:
    """
    This class represents a character. A character has a name and a description.

    Attributes:
        name (str): The name of the character.
        description (str): The description of the character.

    Methods:
        __init__(self, name, description) : The constructor.

    Examples:

    >>> character = Character("Goblin", "A small, green creature.")
    >>> character.name
    'Goblin'
    >>> character.description
    'A small, green creature.'
    >>> type(character.__init__)
    <class 'function'>

    """

    # Define the constructor.
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return f"Character: {self.name}, Description: {self.description}"

    def get_msgs(self):
        """Return the messages of the character."""
        return self.msgs

    def move(self):
        """Move the character to a random adjacent room."""
        exits = list(self.current_room.exits.values())
        if exits:
            new_room = random.choice(exits)
            if new_room is not None:
                self.current_room = new_room
                print(f"{self.name} se déplace vers {self.current_room.name}.\n")
                return True
        return False
