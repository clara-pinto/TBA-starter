from quest import QuestManager
# Define the Player class.

from quest import QuestManager

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
        self.history = []
        self.inventory = {}
        self.move_count = 0
        self.quest_manager = QuestManager(self)
        self.rewards = []   # List to store earned rewards
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        self.history.append(self.current_room)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            # Afficher un message d'erreur et la liste des sorties de la pièce courante
            print(f"\nVous ne pouvez pas aller dans cette direction.\n{self.current_room.get_exit_string()}\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())

        # Check room visit objectives
        self.quest_manager.check_room_objectives(self.current_room.name)

        # Increment move counter and check movement objectives
        self.move_count += 1
        self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)

        return True

    def get_history(self):
        if len(self.history) == 0:
            print("Vous n'avez visité aucun lieu.\n")
            return
        print("Vous avez déjà visité les lieux suivants :\n")
        for elt in self.history:
            print("\t-",elt.name,"\n")

    def get_inventory(self):
        if len(self.inventory) == 0:
            print("Votre inventaire est vide.\n")
            return
        print("Vous disposez des items suivants :\n")
        for item in self.inventory.values():
            print(f"\t- {item.name} : {item.description} ({item.weight} kg)\n")

    def add_reward(self, reward):
        if reward and reward not in self.rewards:
            self.rewards.append(reward)

            print(f"\n🎁 Vous avez obtenu: {reward}\n")

    def show_rewards(self):
        if not self.rewards:
            print("\n🎁 Aucune récompense obtenue pour le moment.\n")

            print( f"\n Vous avez obtenu: {self.reward}\n")

    def show_rewards(self):
        if not self.rewards:
            print( "\n Aucune récompense obtenue pour le moment.\n")

        else:
            print("\nVos récompenses:")
            for reward in self.rewards:
                print(f"  • {reward}")
            print()


