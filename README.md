# TBA

Ce repo contient un jeu d’aventure TBA, inspiré dl'univers du manga "Frieren : Au-delà de la fin du voyage".

## Guide utilisateur

Pour lancer la partie, faites la commande `python game.py` dans le terminal.

Ainsi, vous entrez dans l'univers du manga "Frieren". Vous pouvez vous déplacer entre différents lieux : la Capitale du Royaume Central, la cité de Strahl, le village de Heiter, une prairie florissante, un donjon, le domaine de Graf Grenat, les villages isolés du plateau du Nord, la cité de Ausserst, le Royaume du Nord et enfin Auréole, le royaume des défunts.

Le scénario gagnant du jeu est simplement d'accomplir toutes les quêtes proposées : _Récupérer le Sceptre_, _Vers Auréole_ et _Retrouver Himmel_.
En revanche votre partie sera perdu si vous allez dans le donjon sans être protégé...

### Description des quêtes

- _Récupérer le Sceptre_ : vous devez récupérer le sceptre qui vous permettra de rester protéger des dangers lors de votre aventure ;
- _Vers Auréole_ : vous devez visiter plusieurs lieux et rencontrer certains personnages pour pouvoir accéder à votre destionation : Auréole ;
- _Retrouver Himmel_ : une fois arrivé à Auréole, vous pourrez enfin retrouver votre compagnon perdu ;

### Description des commandes

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


## Guide développeur

![Diagramme de classes](assets/schema.png)


## Perspectives de développement

Pour améliorer cette version du jeu, quelques éléments pourraient être ajouter :
- des _démons_ contre qui le joueur devrait se battre : il faudrait ajouter des commandes qui permettent de faire des combats ;
- la possibilité de prendre des PNJ en compagnon de voyage ;
- rajouter dans l'interface graphique la possibilité de voir les PNJ auxquels on parle, les items qu'on a dans notre inventaire, etc...;