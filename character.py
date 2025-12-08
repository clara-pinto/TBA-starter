# Define the Character class.

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
        return self.msgs
