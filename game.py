# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : accéder à l'historique des lieux", Actions.history, 0)
        self.commands["history"] = history
        
        self.directions = []
        for i in self.rooms:
            for direction in i.get_exits().keys():
                if direction not in self.directions:
                    self.directions.append(direction)
    

        # Setup rooms

        capitale = Room("la Capitale du Royaume Central", "une grande cité humaine, centre politique et culturel du royaume.")
        self.rooms.append(capitale)
        strahl = Room("Strahl", "une ville religieuse.")
        self.rooms.append(strahl)
        village = Room("le village de Heiter", "le village où habite Heiter, notre ami prêtre.")
        self.rooms.append(village)
        prairie = Room("la prairie", "grande étendue de fleurs.")
        self.rooms.append(prairie)
        donjon = Room("un donjon", "un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(donjon)
        domaine = Room("le domaine de Graf Grenat", "une ville fortifiée dans les contrées du Nord, protégée par une barrière magique empechant les démons d'entrer dans la cité.\nCependant, bien que la ville reste prospère, ses environs sont une zone de guerre entre Aura et ses démons et les humains.")
        self.rooms.append(domaine)
        plateau = Room("un des villages isolés du Plateau du Nord", "plaines isolées où se trouvent des villages et de grandes forêts enneigées.")
        self.rooms.append(plateau)
        ausserst = Room("Ausserst", "la cité magique du Nord, siège de l'Association Magique Continentale.\nC'est aussi une ville réputée pour ses académies et infrastructures dédiées aux mages.")
        self.rooms.append(ausserst)
        royaume = Room("le Royaume du Nord", "Prenez garde ! Les routes sont dangereuses et infestées de montres.")
        self.rooms.append(royaume)
        aureole = Room("Auréole", "le royaume où reposerait les âmes des défunts.")
        self.rooms.append(aureole)

        # Create exits for rooms

        capitale.exits = {"N" : strahl, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        strahl.exits = {"N" : prairie, "E" : None, "S" : capitale, "O" : village, "U" : None, "D" : None}
        village.exits = {"N" : None, "E" : strahl, "S" : None, "O" : None, "U" : None, "D" : None}
        prairie.exits = {"N" : domaine, "E" : None, "S" : strahl, "O" : None, "U" : None, "D" : donjon}
        donjon.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : prairie, "D" : None}
        domaine.exits = {"N" : None, "E" : None, "S" : prairie, "O" : plateau, "U" : None, "D" : None}
        plateau.exits = {"N" : None, "E" : domaine, "S" : None, "O" : ausserst, "U" : None, "D" : None}
        ausserst.exits = {"N" : royaume, "E" : plateau, "S" : None, "O" : None, "U" : None, "D" : donjon}
        royaume.exits = {"N" : aureole, "E" : None, "S" : ausserst, "O" : None, "U" : None, "D" : None}
        aureole.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = capitale

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print('>')
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
        

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()