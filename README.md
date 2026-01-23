# TBA

Ce repo contient un jeu d’aventure TBA, inspiré dl'univers du manga "Frieren : Au-delà de la fin du voyage".

## Guide utilisateur

Pour lancer la partie, faites la commande `python game.py` dans le terminal.

Ainsi, vous entrez dans l'univers du manga "Frieren". Vous pouvez vous déplacer entre différents lieux : la Capitale du Royaume Central, la cité de Strahl, le village de Heiter, une prairie florissante, un donjon, le domaine de Graf Grenat, les villages isolés du plateau du Nord, la cité de Ausserst, le Royaume du Nord et enfin Auréole, le royaume des défunts.

Le scénario gagnant du jeu est simplement d'accomplir toutes les quêtes proposées : _Récupérer le Sceptre_, _Vers Auréole_ et _Retrouver Himmel_.
En revanche votre partie sera perdu si vous allez dans le donjon sans être protégé...

La commande `help` affichera toutes les commandes disponible, qui sont :
- `quit` : quitter le jeu ;
- `go` : se déplacer dans une direction cardinale ;
- `history` : accéder à l'historique des lieux ;
- `back` : revenir en arrière ;
- `look` : afficher la liste des items et des personnages présents dans le lieu actuel ;
- `take` : prendre les items dans le lieu actuel ;
- `drop` : remettre les items dans le lieu actuel ;
- `check` : vérifier l'inventaire ;
- `talk` : intéragir avec les personnages non joueurs ;
- `quests` : afficher la liste des quêtes ;
- `quest` : afficher les détails d'une quête ;
- `activate` : activer une quête ;
- `rewards` : afficher vos récompenses ;


## Structuration

Il y a 8 modules contenant chacun une classe.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : le joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les fonctions qui sont appelées lorsque une commande est exécutée ;
- `item.py`  / `Item` : représenter les différents objets que le joueur pourra trouver dans les différents lieux de la map ;
- `character.py` / `Character` : représenter les différents personnages non joueurs ;
- `quest.py` / `Quest` et `QuestManager`: création des quêtes et gestion des quêtes ;
