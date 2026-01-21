"""Actions module for game commands.

The actions module contains the functions that are called when a command
is executed. Each function takes 3 parameters:
- game: the game object
- list_of_words: the list of words in the command
- number_of_parameters: the number of parameters expected by the command

The functions return True if the command was executed successfully,
False otherwise. The functions print an error message if the number
of parameters is incorrect.
"""

import random

from item import DEBUG

# Error message when command takes no parameter
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# Error message when command takes 1 parameter
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


class Actions:
    """Container class for all game actions."""

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction_map = {
            "N": "N", "NORD": "N",
            "E": "E", "EST": "E",
            "S": "S", "SUD": "S",
            "O": "O", "OUEST": "O",
            "U": "U", "UP": "U", "HAUT": "U",
            "D": "D", "DOWN": "D", "BAS": "D"
        }

        if DEBUG:
            print(f"DEBUG: directions = {list_of_words} depuis "
                  f"{game.player.current_room.name}")

        input_dir = list_of_words[1].upper()

        # Move the player in the direction specified by the parameter.
        if input_dir not in direction_map:
            print("Cette direction n'est pas valide.")
            return False
        
        direction = direction_map[input_dir]

        if direction not in game.player.current_room.exits:
            print("Vous ne pouvez pas aller dans cette direction.")
            return False
        
        player.move(direction)
        player.get_history()
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        if DEBUG:
            print("DEBUG: Quitting the game.")

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        if DEBUG:
            print("DEBUG: Printing the list of available commands.")

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des lieux visités par le joueur.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if DEBUG:
            print("DEBUG: Affichage de l'historique des lieux "
                  "visités par le joueur.")

        if game.player is None:
            print("Aucun joueur n'est défini.")
            return False

        game.player.get_history()
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de revenir à la pièce précédente.

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if DEBUG:
            print("DEBUG: Revenir à la pièce précédente.")

        player = game.player
        if not player.history:
            print("Vous n'avez pas d'historique de pièces à revenir.")
            return False

        previous_room = player.history.pop()
        player.current_room = previous_room
        print(player.current_room.get_long_description())
        game.player.get_history()
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if DEBUG:
            print("DEBUG: Affichage de l'inventaire de la pièce "
                  "actuelle.")

        if game.player is None:
            print("Aucun item est défini.")
            return False

        game.player.current_room.get_inventory()
        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if DEBUG:
            print("DEBUG: Prendre un item de la pièce actuelle.")

        if game.player is None:
            print("Aucun item n'est défini.")
            return False

        item_name = list_of_words[1].lower()
        objet = game.player.current_room.inventory.pop(item_name) 
        game.player.inventory[item_name] = objet
        game.player.quest_manager.check_action_objectives("prendre", item_name)
        print("Vous avez pris l'item '{}'.".format(item_name))
        return True

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if DEBUG:
            print("DEBUG: Remettre un item dans la pièce actuelle.")

        if game.player is None:
            print("Aucun item n'est défini.")
            return False

        item_name = list_of_words[1].lower()
        objet = game.player.inventory.pop(item_name)
        return True

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """Check the inventory of the player."""
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if DEBUG:
            print("DEBUG: Affichage de l'inventaire du joueur.")

        if game.player is None:
            print("Aucun item n'est défini.")
            return False

        return True

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """Talk to a character."""
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if DEBUG:
            print("DEBUG: Parler à un personnage non joueur.")
            
        if game.player is None:
            print("Aucun personnage n'est défini.")
            return False

        character_name = list_of_words[1].lower()
        character = game.player.current_room.characters.get(character_name)
        if character is None:
            print(f"Il n'y a pas de personnage nommé '{character_name}' ici.")
            return False

        msgs = character.get_msgs()
        if not msgs:
            print(f"{character.name} n'a rien à dire.")
            return True

        message = random.choice(msgs)
        print(f"{character.name} dit : '{message}'")
        return True

    @staticmethod
    def quests(game, list_of_words, number_of_parameters):
        """
        Show all quests and their status.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quests(game, ["quests"], 0)
        <BLANKLINE>
        📋 Liste des quêtes:
          ❓ Grand Explorateur (Non activée)
          ❓ Grand Voyageur (Non activée)
          ❓ Découvreur de Secrets (Non activée)
        <BLANKLINE>
        True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        return True

    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
        """
        Show details about a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
        <BLANKLINE>
        📋 Quête: Grand Voyageur
        📖 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        Objectifs:
          ⬜ Se déplacer 10 fois (Progression: 0/10)
        <BLANKLINE>
        🎁 Récompense: Bottes de voyageur
        <BLANKLINE>
        True
        >>> Actions.quest(game, ["quest"], 1)
        <BLANKLINE>
        La commande 'quest' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Prepare current counter values to show progress
        current_counts = {
            "Se déplacer": game.player.move_count
        }

        return True

    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
        """
        Activate a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
        <BLANKLINE>
        🗡️  Nouvelle quête activée: Grand Voyageur
        📝 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        True
        >>> Actions.activate(game, ["activate"], 1)
        <BLANKLINE>
        La commande 'activate' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Try to activate the quest
        if game.player.quest_manager.activate_quest(quest_title):
            return True

        msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
        msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
        print(msg1 + msg2)
        return False

    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
        """
        Display all rewards earned by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.rewards(game, ["rewards"], 0)
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        True
        >>> Actions.rewards(game, ["rewards", "param"], 0)
        <BLANKLINE>
        La commande 'rewards' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all rewards
        game.player.show_rewards()
        return True
