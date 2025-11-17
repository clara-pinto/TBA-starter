# Define the Player class.
class Player():
    """
    This class represents a player. A player has a name and a current room.


    Attributes:
        name (str): The name of the player.
        current_room (Room): The current room the player is in.


    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : Move the player in a given direction.
    Examples:


    >>> player = Player("Alice")
    >>> player.name
    'Alice'
    >>> player.current_room is None
    True
    >>> type(player.move)
    <class 'function'>


    """


    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    